#!/usr/bin/env python3
"""fit_params.py — replace guessed parameters with fitted ones.

The model contains a number of constants I chose by judgement rather than
measurement: dispersion parameters for strikeouts, RBI and H+R+RBI, the
first-inning dispersion, and the shrinkage anchors. The NRFI case showed
what that is worth — the guess was 1.45, the fitted value was 3.36, and the
error made the board call YRFI on 79% of games and go 34-53.

This script fits each of them against real distributions pulled from MLB
StatsAPI, reports how far each guess was from the fitted value, and writes
docs/FIT.md plus a machine-readable docs/fitted_params.json that the model
reads at runtime (falling back to the current constants when absent).

METHOD. For each count statistic we collect the empirical distribution over
completed games, then solve for the negative-binomial dispersion d such that
Var = d * mean matches the observed variance. Where a distribution is
zero-inflated (first-inning runs especially) we fit d to reproduce the
observed P(0) instead, because P(0) is the quantity the model actually uses.

Shrinkage anchors are fitted by split-half reliability: the k that makes a
player's first-half rate best predict his second-half rate is the k that
correctly balances signal against noise.

Costs no odds credits — MLB StatsAPI only.

Run:  python fit_params.py [--days 60] [--players 150]
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import statistics
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

# the values currently hard-coded in the model — what we are checking
CURRENT = {
    "FI_LAMBDA_SCALE": 1.00,
    "HR_CALIBRATION": 1.00,
    "FI_DISPERSION": 3.36,
    "K_DISPERSION": 1.30,
    "RBI_DISPERSION": 1.50,
    "HRR_DISPERSION": 1.35,
    "SHRINK_avg": 200.0,
    "SHRINK_k_pa": 150.0,
}


def nb_p0(mean, d):
    if mean <= 0 or d <= 1.0:
        return None
    var = d * mean
    r = mean * mean / (var - mean)
    return (r / (r + mean)) ** r


def fit_dispersion_to_p0(mean, p0_target):
    """Solve for d such that NB(mean, d) reproduces the observed P(0)."""
    lo, hi = 1.001, 20.0
    for _ in range(120):
        mid = (lo + hi) / 2
        v = nb_p0(mean, mid)
        if v is None:
            return None
        if v < p0_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def fit_dispersion_to_var(values):
    """d = Var / mean, the direct moment estimator."""
    if len(values) < 30:
        return None
    m = statistics.mean(values)
    if m <= 0:
        return None
    v = statistics.pvariance(values)
    return v / m


def report_row(name, guessed, fitted, n, note=""):
    if fitted is None:
        return f"| `{name}` | {guessed} | — | {n} | insufficient data {note} |"
    ratio = fitted / guessed if guessed else float("inf")
    verdict = ("close" if 0.85 <= ratio <= 1.18
               else "**materially wrong**" if (ratio > 1.5 or ratio < 0.67)
               else "off")
    return (f"| `{name}` | {guessed} | **{fitted:.3f}** | {n} | "
            f"{ratio:.2f}x — {verdict} {note} |")


# --------------------------------------------------------------------------
# data collection
# --------------------------------------------------------------------------

def first_inning_runs(client, days, out_stats):
    """Every completed game's first-inning runs, per half-inning and combined."""
    end = date.today()
    start = end - timedelta(days=days)
    halves, combined = [], []
    cur = start
    while cur < end:
        chunk = min(cur + timedelta(days=27), end)
        try:
            resp = client.get_json("mlb/schedule", {
                "sportId": 1, "startDate": cur.isoformat(),
                "endDate": chunk.isoformat(), "hydrate": "linescore"})
        except Exception:
            resp = None
        for day in ((resp or {}).get("dates") or []):
            for g in (day.get("games") or []):
                if ((g.get("status") or {}).get("abstractGameState")) != "Final":
                    continue
                inns = ((g.get("linescore") or {}).get("innings") or [])
                if not inns:
                    continue
                first = sorted(inns, key=lambda i: i.get("num") or 0)[0]
                if (first.get("num") or 0) != 1:
                    continue

                def r(side):
                    v = (first.get(side) or {}).get("runs")
                    return v if isinstance(v, (int, float)) else 0
                a, h = r("away"), r("home")
                halves.extend([a, h])
                combined.append(a + h)
        cur = chunk + timedelta(days=1)
    out_stats["fi_games"] = len(combined)
    return halves, combined


def player_game_counts(client, season, group, stat_keys, limit, sort_stat):
    """Per-game values of a stat across a sample of players."""
    try:
        resp = client.get_json("mlb/stats", {
            "stats": "season", "group": group, "sportId": 1, "season": season,
            "limit": limit, "sortStat": sort_stat, "order": "desc",
            "playerPool": "ALL"})
    except Exception:
        return [], 0
    ids = []
    for blk in ((resp or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            pid = ((sp.get("player") or {}).get("id"))
            if pid:
                ids.append(pid)
    vals = []
    for pid in ids:
        try:
            log = client.get_json(f"mlb/people/{pid}/stats", {
                "stats": "gameLog", "group": group, "season": season})
        except Exception:
            continue
        for blk in ((log or {}).get("stats") or []):
            for sp in (blk.get("splits") or []):
                st = sp.get("stat") or {}
                if group == "pitching":
                    try:
                        if int(st.get("gamesStarted") or 0) < 1:
                            continue
                    except (TypeError, ValueError):
                        continue
                else:
                    try:
                        if int(st.get("plateAppearances") or 0) < 1:
                            continue
                    except (TypeError, ValueError):
                        continue
                tot = 0
                ok = False
                for k in stat_keys:
                    try:
                        tot += int(st.get(k) or 0)
                        ok = True
                    except (TypeError, ValueError):
                        pass
                if ok:
                    vals.append(tot)
    return vals, len(ids)


def split_half_k(client, season, limit=200):
    """Fit the shrinkage anchor by split-half reliability.

    The correct k is the one where a player's first-half rate, shrunk by k,
    best predicts his second-half rate. Too small and noise carries through;
    too large and real differences are erased."""
    try:
        resp = client.get_json("mlb/stats", {
            "stats": "season", "group": "hitting", "sportId": 1, "season": season,
            "limit": limit, "sortStat": "plateAppearances", "order": "desc",
            "playerPool": "ALL"})
    except Exception:
        return None, None, 0
    ids = []
    for blk in ((resp or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            pid = ((sp.get("player") or {}).get("id"))
            if pid:
                ids.append(pid)
    pairs_avg, pairs_k = [], []
    for pid in ids:
        try:
            log = client.get_json(f"mlb/people/{pid}/stats", {
                "stats": "gameLog", "group": "hitting", "season": season})
        except Exception:
            continue
        games = []
        for blk in ((log or {}).get("stats") or []):
            for sp in (blk.get("splits") or []):
                st = sp.get("stat") or {}
                try:
                    pa = int(st.get("plateAppearances") or 0)
                    if pa < 1:
                        continue
                    games.append((sp.get("date") or "", pa,
                                  int(st.get("atBats") or 0),
                                  int(st.get("hits") or 0),
                                  int(st.get("strikeOuts") or 0)))
                except (TypeError, ValueError):
                    continue
        if len(games) < 60:
            continue
        games.sort(key=lambda g: g[0])
        mid = len(games) // 2
        for half_pair, idx in ((pairs_avg, 3), (pairs_k, 4)):
            f = games[:mid]
            s = games[mid:]
            if idx == 3:
                fd = sum(g[2] for g in f); sd = sum(g[2] for g in s)
            else:
                fd = sum(g[1] for g in f); sd = sum(g[1] for g in s)
            if fd < 100 or sd < 100:
                continue
            half_pair.append((sum(g[idx] for g in f) / fd, fd,
                              sum(g[idx] for g in s) / sd))
    def best_k(pairs, league):
        if len(pairs) < 20:
            return None
        best, bk = None, None
        for k in range(20, 801, 10):
            err = 0.0
            for r1, d1, r2 in pairs:
                shrunk = (r1 * d1 + league * k) / (d1 + k)
                err += (shrunk - r2) ** 2
            if best is None or err < best:
                best, bk = err, k
        return bk
    la = statistics.mean([p[0] for p in pairs_avg]) if pairs_avg else 0.243
    lk = statistics.mean([p[0] for p in pairs_k]) if pairs_k else 0.225
    return best_k(pairs_avg, la), best_k(pairs_k, lk), len(pairs_avg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--players", type=int, default=120)
    ap.add_argument("--season", type=int, default=date.today().year)
    args = ap.parse_args()

    client = WorkerClient()
    stats = {}
    fitted = {}

    out = ["# Fitted model parameters", "",
           f"Fitted {date.today().isoformat()} against real distributions from MLB "
           "StatsAPI. Every value below was previously chosen by judgement. The NRFI "
           "dispersion showed why that matters: the guess was 1.45, the fitted value "
           "3.36, and the error made the board call YRFI on 79% of games and go 34-53.",
           "",
           "| Parameter | Guessed | Fitted | Sample | Verdict |",
           "|---|---|---|---|---|"]

    # ---- first-inning dispersion (fit to P(0), the quantity actually used) ----
    halves, combined = first_inning_runs(client, args.days, stats)
    if combined:
        mean_c = statistics.mean(combined)
        p0 = sum(1 for v in combined if v == 0) / len(combined)
        d_fi = fit_dispersion_to_p0(mean_c, p0)
        fitted["FI_DISPERSION"] = d_fi
        out.append(report_row("FI_DISPERSION", CURRENT["FI_DISPERSION"], d_fi,
                              f"{len(combined)} games",
                              f"(mean {mean_c:.2f}, P(0)={p0:.1%})"))
        stats["fi_mean"] = mean_c
        stats["fi_p0"] = p0
    else:
        out.append(report_row("FI_DISPERSION", CURRENT["FI_DISPERSION"], None, "0 games"))

    # ---- strikeouts ----
    ks, npit = player_game_counts(client, args.season, "pitching",
                                  ("strikeOuts",), args.players, "strikeOuts")
    d_k = fit_dispersion_to_var(ks)
    fitted["K_DISPERSION"] = d_k
    out.append(report_row("K_DISPERSION", CURRENT["K_DISPERSION"], d_k,
                          f"{len(ks)} starts",
                          f"(mean {statistics.mean(ks):.2f})" if ks else ""))

    # ---- RBI and H+R+RBI ----
    rbis, _ = player_game_counts(client, args.season, "hitting",
                                 ("rbi",), args.players, "rbi")
    d_rbi = fit_dispersion_to_var(rbis)
    fitted["RBI_DISPERSION"] = d_rbi
    out.append(report_row("RBI_DISPERSION", CURRENT["RBI_DISPERSION"], d_rbi,
                          f"{len(rbis)} games",
                          f"(mean {statistics.mean(rbis):.2f})" if rbis else ""))

    hrr, _ = player_game_counts(client, args.season, "hitting",
                                ("hits", "runs", "rbi"), args.players, "hits")
    d_hrr = fit_dispersion_to_var(hrr)
    fitted["HRR_DISPERSION"] = d_hrr
    out.append(report_row("HRR_DISPERSION", CURRENT["HRR_DISPERSION"], d_hrr,
                          f"{len(hrr)} games",
                          f"(mean {statistics.mean(hrr):.2f})" if hrr else ""))

    # ---- first-inning lambda scale ----
    # The dispersion fit shapes the distribution; this anchors its CENTRE.
    # We compare the model's own average implied lambda (recovered from the
    # NRFI board it has already published) against the league mean measured
    # above. A model whose centre is off will call one side relentlessly
    # regardless of how well the tails are fitted.
    try:
        import math as _m
        board = [json.loads(l) for l in open("docs/nrfi_board.jsonl") if l.strip()]
        recent = [b for b in board if b.get("model_p") is not None][-200:]
        d_fi = fitted.get("FI_DISPERSION") or CURRENT["FI_DISPERSION"]

        def _p0(lam):
            var = d_fi * lam
            r = lam * lam / (var - lam)
            return (r / (r + lam)) ** r

        def _inv(p):
            lo, hi = 0.05, 6.0
            for _ in range(60):
                mid = (lo + hi) / 2
                if _p0(mid) > p:
                    lo = mid
                else:
                    hi = mid
            return (lo + hi) / 2

        lams = []
        for b in recent:
            p_nrfi = b["model_p"] if b.get("call") == "NRFI" else 1 - b["model_p"]
            if 0.02 < p_nrfi < 0.98:
                lams.append(_inv(p_nrfi))
        if len(lams) >= 30 and stats.get("fi_mean"):
            model_mean = statistics.mean(lams)
            scale = stats["fi_mean"] / model_mean
            scale = max(0.5, min(1.5, scale))
            fitted["FI_LAMBDA_SCALE"] = scale
            out.append(f"| `FI_LAMBDA_SCALE` | 1.000 | **{scale:.3f}** | "
                       f"{len(lams)} board calls | model mean lambda {model_mean:.3f} "
                       f"vs league {stats['fi_mean']:.3f} |")
    except Exception as exc:
        out.append(f"| `FI_LAMBDA_SCALE` | 1.000 | — | — | not fitted ({exc}) |")

    # ---- HR board calibration ----
    try:
        hrows = [json.loads(l) for l in open("docs/hr_board.jsonl") if l.strip()]
        gh = [r for r in hrows if r.get("result") in ("HIT", "MISS")]
        if len(gh) >= 60:
            act = sum(1 for r in gh if r["result"] == "HIT") / len(gh)
            pred = sum(r.get("p_hr") or 0 for r in gh) / len(gh)
            PA = 4.2
            if 0 < act < 1 and 0 < pred < 1:
                p_act = 1 - (1 - act) ** (1 / PA)
                p_pred = 1 - (1 - pred) ** (1 / PA)
                raw = p_act / p_pred if p_pred else 1.0
                k = 200.0
                sc = (raw * len(gh) + 1.0 * k) / (len(gh) + k)
                sc = max(0.3, min(1.5, sc))
                fitted["HR_CALIBRATION"] = sc
                out.append(f"| `HR_CALIBRATION` | 1.000 | **{sc:.3f}** | {len(gh)} graded "
                           f"| board predicted {pred:.1%}, delivered {act:.1%} "
                           f"(raw {raw:.2f}, shrunk k={k:.0f}) |")
    except Exception as exc:
        out.append(f"| `HR_CALIBRATION` | 1.000 | — | — | not fitted ({exc}) |")

    # ---- shrinkage anchors ----
    k_avg, k_k, n_pairs = split_half_k(client, args.season)
    fitted["SHRINK_avg"] = float(k_avg) if k_avg else None
    fitted["SHRINK_k_pa"] = float(k_k) if k_k else None
    out.append(report_row("SHRINK_avg", CURRENT["SHRINK_avg"], k_avg,
                          f"{n_pairs} players", "(split-half)"))
    out.append(report_row("SHRINK_k_pa", CURRENT["SHRINK_k_pa"], k_k,
                          f"{n_pairs} players", "(split-half)"))

    out.append("")
    out.append("## What to do with this")
    out.append("")
    out.append("Values marked **materially wrong** are off by more than 1.5x and are "
               "distorting every probability derived from them — in the direction of "
               "manufactured edge if the fitted dispersion is HIGHER than the guess "
               "(the model is overstating its confidence in outer outcomes), or of "
               "missed opportunity if LOWER.")
    out.append("")
    out.append("The model reads `docs/fitted_params.json` at runtime and uses these "
               "values in place of the hard-coded constants. Re-run this script "
               "periodically — these are seasonal quantities, not universal ones.")
    out.append("")

    os.makedirs("docs", exist_ok=True)
    with open("docs/FIT.md", "w") as f:
        f.write("\n".join(out))
    clean = {k: v for k, v in fitted.items() if v is not None}
    clean["_fitted_on"] = date.today().isoformat()
    clean["_stats"] = stats
    with open("docs/fitted_params.json", "w") as f:
        json.dump(clean, f, indent=2)
    print("Wrote docs/FIT.md and docs/fitted_params.json")
    for k, v in clean.items():
        if not k.startswith("_"):
            g = CURRENT.get(k)
            print(f"  {k}: guessed {g} -> fitted {v:.3f} ({v/g:.2f}x)")


if __name__ == "__main__":
    main()
