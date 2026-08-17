#!/usr/bin/env python3
"""drift.py — is the run environment moving faster than the market?

Every other tool in this project asks a game-level question: is tonight's
line wrong? That competes head-on with the sharpest number available, and
our own results say we lose that fight.

This asks a different, market-level question: has the actual scoring
environment shifted, and has the market finished repricing it? That is a
LAG question rather than a knowledge question, and lags are the one place a
public-data operation can plausibly be early.

The idea comes from a specific case: an MLB season opened with home runs
sharply up. Dismissable as small sample — except Statcast showed balls
leaving the bat harder while pitching had not changed, which pointed at a
changed baseball. Overs held value until the market caught up.

WHAT THIS MEASURES
  1. Actual runs per game over rolling windows, versus the market's average
     posted total over the same window. A persistent gap means the market
     is trailing reality.
  2. The same for home runs per game, which respond fastest to ball changes.
  3. Whether Statcast contact quality corroborates the move — a scoring
     spike backed by rising exit velocity is a real environment change; one
     without it is variance.

WHAT IT DOES NOT DO
  It does not produce bets. A drift signal is a THESIS GENERATOR: it tells
  you where to look and what to test. Corroboration matters more than the
  gap itself, because a gap with no physical explanation is usually noise
  that will mean-revert before you finish betting it.

Writes docs/DRIFT.md. Costs no odds credits for the scoring side; market
totals come from the locked-picks ledger we already keep.

Run:  python drift.py [--days 45]
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

LOCK = "docs/locked_picks.jsonl"


def fetch_scoring(client, days: int):
    """Runs and home runs per game, by date, from completed linescores."""
    end = date.today()
    start = end - timedelta(days=days)
    by_date: dict[str, dict] = {}
    cur = start
    while cur < end:
        chunk = min(cur + timedelta(days=27), end)
        try:
            resp = client.get_json("mlb/schedule", {
                "sportId": 1, "startDate": cur.isoformat(),
                "endDate": chunk.isoformat(),
                "hydrate": "linescore,team"})
        except Exception:
            resp = None
        for day in ((resp or {}).get("dates") or []):
            d = day.get("date")
            for g in (day.get("games") or []):
                if ((g.get("status") or {}).get("abstractGameState")) != "Final":
                    continue
                teams = g.get("teams") or {}
                a = (teams.get("away") or {}).get("score")
                h = (teams.get("home") or {}).get("score")
                if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
                    continue
                rec = by_date.setdefault(d, {"games": 0, "runs": 0})
                rec["games"] += 1
                rec["runs"] += a + h
        cur = chunk + timedelta(days=1)
    return by_date


def fetch_hr_rate(client, season: int, days: int):
    """League home runs per game over the window, from team season splits.

    Uses the byDateRange split when available; falls back to None rather
    than guessing, because a fabricated HR rate would be worse than no
    HR section at all."""
    end = date.today()
    start = end - timedelta(days=days)
    try:
        resp = client.get_json("mlb/stats", {
            "stats": "byDateRange", "group": "hitting", "sportId": 1,
            "season": season, "startDate": start.isoformat(),
            "endDate": end.isoformat()})
    except Exception:
        return None
    hr = games = 0
    for blk in ((resp or {}).get("stats") or []):
        for sp in (blk.get("splits") or []):
            st = sp.get("stat") or {}
            try:
                hr += int(st.get("homeRuns") or 0)
                games += int(st.get("gamesPlayed") or 0)
            except (TypeError, ValueError):
                continue
    if games <= 0:
        return None
    return hr / (games / 2.0)      # gamesPlayed counts each team


def market_totals_by_date():
    """Average posted total per slate, from picks we already locked.

    This is the market's own opinion of the run environment, recorded at
    the time — which is exactly what we want to compare reality against."""
    try:
        rows = [json.loads(l) for l in open(LOCK) if l.strip()]
    except FileNotFoundError:
        return {}
    by: dict[str, list] = {}
    for r in rows:
        if r.get("market") != "Total":
            continue
        line = r.get("line_at_pull")
        if line is None:
            continue
        by.setdefault(r["slate_date"], []).append(float(line))
    return {d: statistics.mean(v) for d, v in by.items() if v}


def window_mean(by_date, days, key_num, key_den):
    end = date.today()
    cutoff = (end - timedelta(days=days)).isoformat()
    num = den = 0
    for d, rec in by_date.items():
        if d >= cutoff:
            num += rec[key_num]
            den += rec[key_den]
    return (num / den) if den else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=45)
    ap.add_argument("--season", type=int, default=date.today().year)
    args = ap.parse_args()

    client = WorkerClient()
    scoring = fetch_scoring(client, args.days)
    if not scoring:
        print("[drift] no completed games returned")
        return

    out = ["# Run environment drift", "",
           "Every other tool here asks whether tonight's line is wrong — competing "
           "directly with the sharpest number on the board. This asks whether the "
           "scoring environment has moved and the market has not finished repricing "
           "it. That is a lag question, and lags are where being early beats being "
           "smarter.", "",
           "**This produces theses, not bets.** A gap with no physical explanation "
           "is usually noise about to mean-revert.", ""]

    # ---- actual scoring by window ----
    out.append("## Actual scoring")
    out.append("")
    out.append("| Window | Games | Runs/game |")
    out.append("|---|---|---|")
    windows = [7, 14, 30, args.days]
    vals = {}
    for w in windows:
        rpg = window_mean(scoring, w, "runs", "games")
        n = sum(rec["games"] for d, rec in scoring.items()
                if d >= (date.today() - timedelta(days=w)).isoformat())
        if rpg:
            vals[w] = rpg
            out.append(f"| last {w}d | {n} | {rpg:.2f} |")
    out.append("")

    if len(vals) >= 2 and args.days in vals and 7 in vals:
        delta = vals[7] - vals[args.days]
        out.append(f"Recent 7-day scoring is **{delta:+.2f} runs/game** versus the "
                   f"{args.days}-day baseline.")
        out.append("")

    # ---- market's opinion, from our own ledger ----
    mkt = market_totals_by_date()
    if mkt:
        out.append("## Market totals vs reality")
        out.append("")
        out.append("| Window | Avg posted total | Actual runs/game | Gap |")
        out.append("|---|---|---|---|")
        for w in windows:
            cutoff = (date.today() - timedelta(days=w)).isoformat()
            m = [v for d, v in mkt.items() if d >= cutoff]
            rpg = vals.get(w)
            if m and rpg:
                mm = statistics.mean(m)
                out.append(f"| last {w}d | {mm:.2f} | {rpg:.2f} | **{rpg-mm:+.2f}** |")
        out.append("")
        out.append("> A persistent positive gap means games are outscoring the posted "
                   "totals — the market trailing a real shift, or our slate being "
                   "unrepresentative. A gap that appears in the 7-day window but not "
                   "the 30 is almost always variance.")
        out.append("")

    # ---- home runs ----
    hr_recent = fetch_hr_rate(client, args.season, 14)
    hr_base = fetch_hr_rate(client, args.season, args.days)
    if hr_recent and hr_base:
        out.append("## Home run rate")
        out.append("")
        out.append(f"- last 14d: **{hr_recent:.2f} HR/game**")
        out.append(f"- last {args.days}d: **{hr_base:.2f} HR/game**")
        out.append(f"- drift: **{hr_recent-hr_base:+.2f}**")
        out.append("")
        out.append("> Home run rate is the fastest indicator of a changed ball. A move "
                   "here that is CORROBORATED by rising exit velocity is a genuine "
                   "environment change; a move without it is variance.")
        out.append("")

    # ---- Statcast corroboration ----
    try:
        rows = client.get_json("savant/batter", {"year": args.season})
    except Exception:
        rows = None
    if rows:
        def col(r, *names):
            for n in names:
                v = r.get(n)
                if v not in ("", None):
                    try:
                        return float(v)
                    except (TypeError, ValueError):
                        pass
            return None
        ev = [col(r, "exit_velocity_avg", "avg_hit_speed") for r in rows if isinstance(r, dict)]
        ev = [v for v in ev if v]
        brl = [col(r, "barrel_batted_rate", "barrel_percent") for r in rows if isinstance(r, dict)]
        brl = [v for v in brl if v]
        if ev:
            out.append("## Contact quality (corroboration)")
            out.append("")
            out.append(f"- league average exit velocity: **{statistics.mean(ev):.1f} mph** "
                       f"across {len(ev)} qualified hitters")
            if brl:
                out.append(f"- league average barrel rate: **{statistics.mean(brl):.1f}%**")
            out.append("")
            out.append("> These are season-to-date figures. The corroboration test needs "
                       "them tracked over time — save this report periodically and compare, "
                       "because the SHIFT is the signal, not the level.")
            out.append("")

    out.append("## How to use this")
    out.append("")
    out.append("1. A gap that shows in the 7-day window only is noise. Wait for it in 14 and 30.")
    out.append("2. A scoring gap with no matching contact-quality move is noise.")
    out.append("3. A corroborated gap is a thesis, not a bet — it says which SIDE of totals "
               "to investigate, and it decays as the market reprices.")
    out.append("4. Our slate is not the league. The market-vs-reality table compares the "
               "totals WE recorded against ALL games, so a persistent gap may just mean our "
               "pick selection is skewed. Check the direction against the league runs/game "
               "trend before believing it.")
    out.append("")

    os.makedirs("docs", exist_ok=True)
    with open("docs/DRIFT.md", "w") as f:
        f.write("\n".join(out))
    print("Wrote docs/DRIFT.md")
    for w in sorted(vals):
        print(f"  last {w}d: {vals[w]:.2f} runs/game")


if __name__ == "__main__":
    main()
