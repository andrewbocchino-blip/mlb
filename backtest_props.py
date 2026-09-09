#!/usr/bin/env python3
"""backtest_props.py — judge EVERY prop market on history, not on waiting.

The previous version replayed one market: pitcher strikeouts. That left
fourteen others running live on reasoning alone. Reasoning is not evidence,
and shipping a market unmeasured is how the NRFI board ran for three weeks
with an inverted confidence tier before anyone noticed.

This replays every market the board prices, walk-forward and leak-free: for
each completed game the projection is rebuilt from ONLY that player's prior
games, then scored against a ladder of realistic book lines around it.

THE THREE NUMBERS THAT MATTER, per market:

  Brier        calibration. Compare against the BLIND benchmark, never
               against 0.25 — a model that ignores the player entirely and
               projects the league mean scores close to 0.247 on these
               ladders, so 0.247 means no information about the individual.
  separation   discrimination. Hit rate when the model says 60%+ minus the
               rate when it says 40%-. A model can be perfectly calibrated
               at a constant 50% and still be useless; separation is what
               says it can tell games apart.
  bias         whether the projection systematically over- or under-shoots,
               in the stat's own units.

WHAT THIS CANNOT DO. There are no historical prop prices available here, so
it measures whether a market is ACCURATE, not whether it beats a book. A
well calibrated market can still be unprofitable. It answers the cheaper
question first — and answers it for fifteen markets instead of one.

Run:  python backtest_props.py [--players 60] [--markets all]
"""

from __future__ import annotations

import argparse
import base64
import io
import os
import re
import statistics
import zipfile
from datetime import date

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

# Books price AROUND a projection, not at it. Scoring only at the projection
# forces every prediction to ~50% and measures the model on the hardest
# possible question — the flaw that made the first strikeout backtest report
# 0.2472 with 705 of 711 predictions crammed into one band.
LINE_LADDER = (0.75, 0.85, 0.95, 1.05, 1.15)

# market -> (stat group, game-log keys to sum, minimum prior games)
MARKETS = {
    "pitcher_strikeouts":    ("pitching", ("strikeOuts",), 5),
    "pitcher_outs":          ("pitching", ("outs",), 5),
    "pitcher_hits_allowed":  ("pitching", ("hits",), 5),
    "pitcher_earned_runs":   ("pitching", ("earnedRuns",), 5),
    "pitcher_walks":         ("pitching", ("baseOnBalls",), 5),
    "batter_total_bases":    ("hitting", ("totalBases",), 20),
    "batter_hits":           ("hitting", ("hits",), 20),
    "batter_strikeouts":     ("hitting", ("strikeOuts",), 20),
    "batter_home_runs":      ("hitting", ("homeRuns",), 20),
    "batter_rbis":           ("hitting", ("rbi",), 20),
    "batter_runs_scored":    ("hitting", ("runs",), 20),
    "batter_walks":          ("hitting", ("baseOnBalls",), 20),
    "batter_doubles":        ("hitting", ("doubles",), 20),
    "batter_singles":        ("hitting", ("singles",), 20),
    "batter_hits_runs_rbis": ("hitting", ("hits", "runs", "rbi"), 20),
}

DISPERSION = {
    "pitcher_strikeouts": pr.K_DISPERSION,
    "pitcher_outs": getattr(pr, "OUTS_DISPERSION", 1.20),
    "pitcher_hits_allowed": getattr(pr, "HA_DISPERSION", 1.35),
    "pitcher_earned_runs": getattr(pr, "ER_DISPERSION", 1.90),
    "pitcher_walks": getattr(pr, "BB_DISPERSION", 1.30),
    "batter_total_bases": getattr(pr, "TB_DISPERSION", 1.55),
    "batter_rbis": pr.RBI_DISPERSION,
    "batter_hits_runs_rbis": pr.HRR_DISPERSION,
    "batter_runs_scored": pr.RBI_DISPERSION,
}


def brier(pairs):
    return sum((p - o) ** 2 for p, o in pairs) / len(pairs) if pairs else None


def separation(pairs):
    hi = [o for p, o in pairs if p >= 0.60]
    lo = [o for p, o in pairs if p <= 0.40]
    if not hi or not lo:
        return None
    return (sum(hi) / len(hi)) - (sum(lo) / len(lo))


def calibration_table(pairs):
    bands = ((0, .2), (.2, .35), (.35, .5), (.5, .65), (.65, .8), (.8, 1.01))
    out = []
    for lo, hi in bands:
        sel = [(p, o) for p, o in pairs if lo <= p < hi]
        if not sel:
            continue
        out.append({"band": f"{lo:.0%}-{hi:.0%}", "n": len(sel),
                    "pred": sum(p for p, _ in sel) / len(sel),
                    "actual": sum(o for _, o in sel) / len(sel)})
    return out


def sample_players(client, season, group, limit, sort_stat):
    try:
        resp = client.get_json("mlb/stats", {
            "stats": "season", "group": group, "sportId": 1, "season": season,
            "limit": limit, "sortStat": sort_stat, "order": "desc",
            "playerPool": "ALL"})
    except Exception:
        return []
    ids = []
    for blk in ((resp or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            pid = ((sp.get("player") or {}).get("id"))
            if pid:
                ids.append(pid)
    return ids


def game_values(client, pid, season, group, keys):
    """Per-game totals for the stat, oldest first. Starts only for pitchers."""
    try:
        log = client.get_json(f"mlb/people/{pid}/stats", {
            "stats": "gameLog", "group": group, "season": season})
    except Exception:
        return []
    rows = []
    for blk in ((log or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            st = sp.get("stat") or {}
            try:
                if group == "pitching":
                    if int(st.get("gamesStarted") or 0) < 1:
                        continue
                elif int(st.get("plateAppearances") or 0) < 1:
                    continue
            except (TypeError, ValueError):
                continue
            tot, ok = 0, False
            for k in keys:
                v = st.get(k)
                if v is None and k == "singles":
                    try:
                        v = (int(st.get("hits") or 0) - int(st.get("doubles") or 0)
                             - int(st.get("triples") or 0)
                             - int(st.get("homeRuns") or 0))
                    except (TypeError, ValueError):
                        v = None
                try:
                    tot += int(v)
                    ok = True
                except (TypeError, ValueError):
                    pass
            if ok:
                rows.append((sp.get("date") or "", tot))
    rows.sort(key=lambda r: r[0])
    return [v for _d, v in rows]


def backtest_market(client, season, mkey, players):
    """Replay one market. Projection = mean of that player's PRIOR games."""
    group, keys, min_prior = MARKETS[mkey]
    disp = DISPERSION.get(mkey)
    pairs, errs, blind_pairs = [], [], []
    per_player, all_vals = {}, []
    for pid in players:
        vals = game_values(client, pid, season, group, keys)
        if len(vals) > min_prior:
            per_player[pid] = vals
            all_vals.extend(vals)
    if not all_vals:
        return None
    league_mean = statistics.mean(all_vals)

    for vals in per_player.values():
        for i in range(min_prior, len(vals)):
            proj = statistics.mean(vals[:i])
            actual = vals[i]
            errs.append(actual - proj)
            for mult in LINE_LADDER:
                line = round(proj * mult * 2) / 2
                if abs(line - round(line)) < 0.1:
                    line += 0.5
                if line < 0.5:
                    continue
                need = int(line) + 1
                p = (pr.nb_at_least(proj, need, disp) if disp
                     else pr.poisson_at_least(proj, need))
                pb = (pr.nb_at_least(league_mean, need, disp) if disp
                      else pr.poisson_at_least(league_mean, need))
                o = 1.0 if actual > line else 0.0
                pairs.append((p, o))
                blind_pairs.append((pb, o))
    if not pairs:
        return None
    return {"market": mkey, "n": len(pairs),
            "games": sum(max(0, len(v) - min_prior) for v in per_player.values()),
            "brier": brier(pairs), "blind": brier(blind_pairs),
            "sep": separation(pairs), "bias": statistics.mean(errs),
            "bands": calibration_table(pairs), "league_mean": league_mean}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--players", type=int, default=60)
    ap.add_argument("--season", type=int, default=date.today().year)
    ap.add_argument("--markets", default="all")
    args = ap.parse_args()

    client = WorkerClient()
    want = (list(MARKETS) if args.markets == "all"
            else [m for m in args.markets.split(",") if m in MARKETS])

    pitchers = sample_players(client, args.season, "pitching",
                              args.players, "strikeOuts")
    batters = sample_players(client, args.season, "hitting",
                             args.players, "plateAppearances")
    print(f"[backtest] sampled {len(pitchers)} pitchers, {len(batters)} batters")

    results = []
    for mkey in want:
        pool = pitchers if MARKETS[mkey][0] == "pitching" else batters
        try:
            r = backtest_market(client, args.season, mkey, pool)
        except Exception as exc:
            print(f"[backtest] {mkey}: failed ({exc})")
            continue
        if r:
            results.append(r)
            print(f"[backtest] {mkey:24s} n={r['n']:6d} brier={r['brier']:.4f} "
                  f"blind={r['blind']:.4f} edge={r['blind']-r['brier']:+.4f} "
                  f"sep={(r['sep'] or 0):+.1%}")

    out = ["# Prop model backtest — every market", "",
           f"Replayed {date.today().isoformat()} for season {args.season}. Each "
           "projection uses ONLY that player's prior games (no lookahead) and is "
           "scored against a ladder of realistic book lines around it.", "",
           "**Read Brier against the BLIND column, never against 0.25.** Blind is "
           "what a model that ignores the player entirely and projects the league "
           "mean scores on the same lines. A market whose Brier matches its blind "
           "score carries no information about the individual, however sensible the "
           "formula looks.", "",
           "| Market | n | Brier | Blind | Edge | Separation | Bias | Verdict |",
           "|---|---|---|---|---|---|---|---|"]
    for r in sorted(results, key=lambda x: x["blind"] - x["brier"], reverse=True):
        edge = r["blind"] - r["brier"]
        sep = r["sep"] or 0
        if edge > 0.010 and sep > 0.15:
            v = "**carries information**"
        elif edge > 0.003:
            v = "marginal"
        else:
            v = "no better than blind"
        out.append(f"| {r['market']} | {r['n']:,} | {r['brier']:.4f} | {r['blind']:.4f} "
                   f"| {edge:+.4f} | {sep:+.1%} | {r['bias']:+.2f} | {v} |")
    out += ["",
            "**Edge** is blind minus model — positive means knowing the player helps. "
            "**Separation** is the hit rate when the model says 60%+ minus the rate "
            "when it says 40%-; near zero means the projection cannot tell games "
            "apart even when well calibrated. **Bias** is in the stat's own units, "
            "positive meaning the model under-projects.", "",
            "A market marked *no better than blind* should not be producing "
            "recommendations. The formula may be reasonable and the distribution "
            "correct, and it can still contain nothing the league average does not.",
            ""]

    for r in sorted(results, key=lambda x: x["blind"] - x["brier"], reverse=True):
        out.append(f"## {r['market']}")
        out.append("")
        out.append(f"- predictions scored: **{r['n']:,}** across {r['games']:,} "
                   f"player-games")
        out.append(f"- league mean for this stat: **{r['league_mean']:.2f}**")
        out.append(f"- Brier **{r['brier']:.4f}** vs blind **{r['blind']:.4f}** "
                   f"(edge {r['blind']-r['brier']:+.4f})")
        if r["sep"] is not None:
            out.append(f"- separation **{r['sep']:+.1%}**")
        out.append(f"- bias **{r['bias']:+.2f}** "
                   f"({'under' if r['bias'] > 0 else 'over'}-projects)")
        out.append("")
        out.append("| Model says | n | Predicted | Actual |")
        out.append("|---|---|---|---|")
        for b in r["bands"]:
            out.append(f"| {b['band']} | {b['n']:,} | {b['pred']:.0%} | "
                       f"{b['actual']:.0%} |")
        gaps = [abs(b["pred"] - b["actual"]) for b in r["bands"]]
        out.append("")
        if gaps:
            out.append(f"> Largest band gap **{max(gaps):.0%}**. Bands sitting "
                       f"consistently on one side of the diagonal mean the projection "
                       f"is biased, and every edge computed from it inherits that.")
        out.append("")

    os.makedirs("docs", exist_ok=True)
    with open("docs/BACKTEST.md", "w") as f:
        f.write("\n".join(out))
    print(f"Wrote docs/BACKTEST.md ({len(results)} markets)")


if __name__ == "__main__":
    main()
