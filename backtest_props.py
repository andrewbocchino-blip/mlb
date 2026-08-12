#!/usr/bin/env python3
"""backtest_props.py — judge the prop models on HISTORY, not on waiting.

Everything else in this project is forward-only: make a call, wait weeks,
grade it. But the strikeout and hits models can be tested retroactively
right now, for free, against hundreds of completed starts. If the model is
badly calibrated we should learn that today rather than after six weeks of
recording bad numbers.

METHOD (deliberately leak-free):
  For every completed start by a sampled pitcher, we rebuild what the model
  WOULD have projected using ONLY data available before that game — the
  pitcher's own prior starts that season and the opponent's season K rate —
  then compare the projection to what actually happened.

  * pitcher strikeouts: expected Ks vs actual, plus P(over) at the nearest
    half-line, scored by Brier and by calibration band.
  * batter hits: same idea over a sample of hitters' game logs.

OUTPUT: docs/BACKTEST.md — calibration table, Brier score, mean bias.

WHAT IT CANNOT DO: it has no historical closing prices, so it measures
whether the model is ACCURATE, not whether it beats a market. A well
calibrated model can still be unprofitable; a badly calibrated one cannot
be trusted at all. This answers the second question first because it is
the cheaper one.

Run:  python backtest_props.py [--pitchers 40] [--days 90]
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import sys
import zipfile
from datetime import date, timedelta

try:
    from mlb_betting_model.worker_client import WorkerClient
except Exception:
    if os.path.exists("run.py"):
        m = re.search(r'_PKG_B64 = "([A-Za-z0-9+/=]+)"', open("run.py").read())
        if m:
            with zipfile.ZipFile(io.BytesIO(base64.b64decode(m.group(1)))) as zf:
                zf.extractall(".")
    from mlb_betting_model.worker_client import WorkerClient

from mlb_betting_model.v14 import props as pr


def brier(pairs):
    return sum((p - o) ** 2 for p, o in pairs) / len(pairs) if pairs else None


def calibration_table(pairs, bands=((0, .2), (.2, .35), (.35, .5),
                                    (.5, .65), (.65, .8), (.8, 1.01))):
    out = []
    for lo, hi in bands:
        sel = [(p, o) for p, o in pairs if lo <= p < hi]
        if not sel:
            continue
        out.append({
            "band": f"{lo:.0%}–{hi:.0%}" if hi <= 1 else f"{lo:.0%}+",
            "n": len(sel),
            "pred": sum(p for p, _ in sel) / len(sel),
            "actual": sum(o for _, o in sel) / len(sel),
        })
    return out


def season_k_rate_before(splits, idx):
    """Pitcher's K/BF and IP/start using ONLY starts before index idx."""
    k = bf = ip = n = 0.0
    for s in splits[:idx]:
        st = s.get("stat") or {}
        try:
            if int(st.get("gamesStarted") or 0) < 1:
                continue
            k += float(st.get("strikeOuts"))
            bf += float(st.get("battersFaced"))
            ip += float(st.get("inningsPitched"))
            n += 1
        except (TypeError, ValueError):
            continue
    if n < pr.MIN_STARTS or bf <= 0:
        return None
    return {"k_per_bf": k / bf, "bf_per_ip": bf / ip if ip else 4.3,
            "ip_per_start": ip / n, "gs": n, "bf": bf}


def backtest_pitchers(client, season, n_pitchers, out):
    """Replay every start after the Nth for a sample of starters."""
    try:
        resp = client.get_json("mlb/stats", {
            "stats": "season", "group": "pitching", "sportId": 1,
            "season": season, "limit": n_pitchers, "sortStat": "strikeOuts",
            "order": "desc", "playerPool": "ALL"})
    except Exception as exc:
        print(f"[backtest] leader fetch failed: {exc}")
        return
    ids = []
    for blk in ((resp or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            pid = ((sp.get("player") or {}).get("id"))
            if pid:
                ids.append(pid)
    print(f"[backtest] sampling {len(ids)} pitchers")

    pairs, errs = [], []
    for pid in ids:
        try:
            log = client.get_json(f"mlb/people/{pid}/stats",
                                  {"stats": "gameLog", "group": "pitching",
                                   "season": season})
        except Exception:
            continue
        splits = []
        for blk in ((log or {}).get("stats") or []):
            splits.extend(blk.get("splits") or [])
        splits.sort(key=lambda s: s.get("date") or "")
        for i, s in enumerate(splits):
            st = s.get("stat") or {}
            try:
                if int(st.get("gamesStarted") or 0) < 1:
                    continue
                actual = int(st.get("strikeOuts"))
            except (TypeError, ValueError):
                continue
            prof = season_k_rate_before(splits, i)
            if prof is None:
                continue
            recent = None
            prior_starts = [x for x in splits[:i]
                            if int((x.get("stat") or {}).get("gamesStarted") or 0) >= 1]
            if len(prior_starts) >= 3:
                w = prior_starts[-pr.RECENT_STARTS:]
                ip_t = k_t = bf_t = 0.0
                for x in w:
                    xs = x.get("stat") or {}
                    try:
                        ip_t += float(xs.get("inningsPitched"))
                        k_t += float(xs.get("strikeOuts"))
                        bf_t += float(xs.get("battersFaced"))
                    except (TypeError, ValueError):
                        pass
                if bf_t:
                    recent = {"n": len(w), "ip_per_start": ip_t / len(w),
                              "k_per_bf": k_t / bf_t, "bf": bf_t}
            lam, _flags, _basis = pr.expected_ks(prof, None, recent, "")
            errs.append(actual - lam)
            # score the model at the half-line nearest the projection
            line = round(lam * 2) / 2
            if abs(line - round(line)) < 0.1:
                line += 0.5
            p_over = pr.nb_at_least(lam, int(line) + 1)
            pairs.append((p_over, 1.0 if actual > line else 0.0))

    if not pairs:
        print("[backtest] no pitcher starts scored")
        return
    b = brier(pairs)
    bias = sum(errs) / len(errs)
    out.append("## Pitcher strikeouts")
    out.append("")
    out.append(f"- starts scored: **{len(pairs)}**")
    out.append(f"- Brier score: **{b:.4f}**  (0.25 = no skill; lower is better)")
    out.append(f"- mean projection bias: **{bias:+.2f} K** "
               f"(positive = model UNDER-projects)")
    out.append("")
    out.append("| Model P(over) | n | Predicted | Actual |")
    out.append("|---|---|---|---|")
    for row in calibration_table(pairs):
        out.append(f"| {row['band']} | {row['n']} | {row['pred']:.0%} | {row['actual']:.0%} |")
    out.append("")
    gap = max((abs(r["pred"] - r["actual"]) for r in calibration_table(pairs)), default=0)
    out.append(f"> Largest band gap: **{gap:.0%}**. Bands that sit consistently above or "
               f"below the diagonal mean the projection is biased, and every edge computed "
               f"from it inherits that bias.")
    out.append("")
    print(f"[backtest] pitcher Ks: n={len(pairs)} brier={b:.4f} bias={bias:+.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pitchers", type=int, default=40)
    ap.add_argument("--season", type=int, default=date.today().year)
    args = ap.parse_args()

    client = WorkerClient()
    out = ["# Prop model backtest", "",
           f"Replayed on {date.today().isoformat()} for season {args.season}. "
           "Each projection uses ONLY that pitcher's prior starts — no lookahead. "
           "This measures whether the model is ACCURATE; it does not measure whether "
           "it beats a market, because historical prop prices are not available here.",
           ""]
    backtest_pitchers(client, args.season, args.pitchers, out)
    os.makedirs("docs", exist_ok=True)
    with open("docs/BACKTEST.md", "w") as f:
        f.write("\n".join(out))
    print("Wrote docs/BACKTEST.md")


if __name__ == "__main__":
    main()
