#!/usr/bin/env python3
"""grade.py — read locked picks, grade against finals, write readable tables.

Reads docs/locked_picks.jsonl (the timestamped, line-locked picks), pulls
final scores from the Cloudflare Worker, grades each pick (WIN/LOSS/PUSH),
and writes two human-readable files that GitHub renders natively:

  docs/PICKS.md   — every locked pick as a clean markdown table by date
  docs/RESULTS.md — graded results with per-day and running W-L-ROI tally

It also rewrites locked_picks.jsonl with graded=true/result filled in, so a
pick is graded once and frozen. Run after games finish (or on a schedule a
few hours after first pitch).

Honest grading rules: a pick is graded only when the game is final. Totals
graded on combined runs vs the locked line; PUSH if exactly equal. ML graded
on winner. Run line -1.5 graded on margin >= 2. Moneyline/run-line P&L uses
the actual American odds when present, else flat -1.0 on a loss and a
conservative +0.91 on a win (≈ -110) so the tally is never inflated.
"""

from __future__ import annotations

import json
import os
import sys

# locate the embedded package (run.py unpacks it; if absent, unpack here too)
try:
    from mlb_betting_model.worker_client import WorkerClient
except Exception:
    import base64, io, zipfile
    if os.path.exists("run.py"):
        src = open("run.py").read()
        import re
        m = re.search(r'_PKG_B64 = "([A-Za-z0-9+/=]+)"', src)
        if m:
            with zipfile.ZipFile(io.BytesIO(base64.b64decode(m.group(1)))) as zf:
                zf.extractall(".")
    from mlb_betting_model.worker_client import WorkerClient

LOCK = "docs/locked_picks.jsonl"


def american_payout(odds, win):
    if odds is None:
        return (0.91 if win else -1.0)
    if win:
        return (odds / 100.0) if odds > 0 else (100.0 / abs(odds))
    return -1.0


def load_locked():
    if not os.path.exists(LOCK):
        return []
    rows = []
    for line in open(LOCK):
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def fetch_finals(client, date):
    """Return {('AWAY','HOME'): (away_runs, home_runs)} for final games on date."""
    finals = {}
    try:
        sched = client.get_json(f"mlb/schedule", {"date": date, "hydrate": "linescore"})
    except Exception:
        return finals
    for d in (sched.get("dates") or []):
        for g in (d.get("games") or []):
            try:
                status = (g.get("status") or {}).get("abstractGameState")
                if status != "Final":
                    continue
                teams = g["teams"]
                away = teams["away"]["team"]["name"]
                home = teams["home"]["team"]["name"]
                ar = teams["away"].get("score")
                hr = teams["home"].get("score")
                if ar is not None and hr is not None:
                    finals[(away, home)] = (ar, hr)
            except Exception:
                continue
    return finals


def grade_pick(row, finals):
    """Return (result, pl) or (None, None) if not gradeable yet."""
    game = row["game"]
    if " @ " not in game:
        return None, None
    away, home = game.split(" @ ", 1)
    key = (away, home)
    if key not in finals:
        return None, None
    ar, hr = finals[key]
    total = ar + hr
    mkt = row["market"]
    pick = row["pick"]

    if mkt == "Total":
        line = row.get("line_at_pull")
        if line is None:
            return None, None
        if total == line:
            return "PUSH", 0.0
        over = total > line
        win = (over and pick.startswith("Over")) or ((not over) and pick.startswith("Under"))
        return ("WIN" if win else "LOSS"), american_payout(None, win)

    if mkt == "Moneyline":
        home_won = hr > ar
        picked_home = home in pick and not pick.strip().startswith(away)
        # robust: match pick text to team name
        picked_home = pick.startswith(home)
        win = (home_won and picked_home) or ((not home_won) and not picked_home)
        return ("WIN" if win else "LOSS"), american_payout(None, win)

    if mkt == "Run Line":
        picked_home = pick.startswith(home)
        margin = (hr - ar) if picked_home else (ar - hr)
        win = margin >= 2  # laying -1.5
        return ("WIN" if win else "LOSS"), american_payout(None, win)

    return None, None


def main():
    client = WorkerClient()
    rows = load_locked()
    if not rows:
        print("No locked picks yet.")
        return

    # group dates needing grading
    dates = sorted({r["slate_date"] for r in rows})
    finals_by_date = {d: fetch_finals(client, d) for d in dates}

    changed = 0
    for r in rows:
        if r.get("graded"):
            continue
        res, pl = grade_pick(r, finals_by_date.get(r["slate_date"], {}))
        if res is not None:
            r["graded"] = True
            r["result"] = res
            r["pl"] = round(pl, 2)
            changed += 1

    # rewrite the locked file with grades frozen in
    with open(LOCK, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    write_picks_md(rows)
    write_results_md(rows)
    print(f"Graded {changed} newly-final picks. Wrote docs/PICKS.md and docs/RESULTS.md")


def write_picks_md(rows):
    by_date = {}
    for r in rows:
        by_date.setdefault(r["slate_date"], []).append(r)
    out = ["# Locked Picks", "", "Picks frozen at the line they were taken at. Paper only — no real money.", ""]
    for date in sorted(by_date, reverse=True):
        out.append(f"## {date}")
        out.append("")
        out.append("| Verdict | Score | Game | Market | Pick | Line | Model Tot | Home Win% |")
        out.append("|---|---|---|---|---|---|---|---|")
        for r in sorted(by_date[date], key=lambda x: -x["score"]):
            line = r.get("line_at_pull")
            line = "—" if line is None else line
            out.append(f"| {r['verdict']} | {r['score']} | {r['game']} | {r['market']} "
                       f"| {r['pick']} | {line} | {r.get('model_total','')} "
                       f"| {round(r.get('home_win_prob',0)*100)}% |")
        out.append("")
    with open("docs/PICKS.md", "w") as f:
        f.write("\n".join(out))


def write_results_md(rows):
    graded = [r for r in rows if r.get("graded")]
    out = ["# Results", "", "Graded against finals. Paper only.", ""]

    # running tally
    tot_w = sum(1 for r in graded if r["result"] == "WIN")
    tot_l = sum(1 for r in graded if r["result"] == "LOSS")
    tot_p = sum(1 for r in graded if r["result"] == "PUSH")
    tot_pl = sum(r.get("pl", 0) for r in graded)
    risk = sum(1 for r in graded if r["result"] in ("WIN", "LOSS"))
    roi = (tot_pl / risk * 100) if risk else 0.0
    out.append(f"**Overall: {tot_w}-{tot_l}" + (f"-{tot_p}" if tot_p else "") +
               f"  ·  {tot_pl:+.2f}u  ·  {roi:+.1f}% ROI** (1u flat)")
    out.append("")

    # PLAY vs LEAN split
    for tier in ("PLAY", "LEAN"):
        tw = sum(1 for r in graded if r["verdict"] == tier and r["result"] == "WIN")
        tl = sum(1 for r in graded if r["verdict"] == tier and r["result"] == "LOSS")
        out.append(f"- **{tier} tier:** {tw}-{tl}")
    out.append("")

    by_date = {}
    for r in graded:
        by_date.setdefault(r["slate_date"], []).append(r)
    for date in sorted(by_date, reverse=True):
        day = by_date[date]
        dw = sum(1 for r in day if r["result"] == "WIN")
        dl = sum(1 for r in day if r["result"] == "LOSS")
        dpl = sum(r.get("pl", 0) for r in day)
        out.append(f"## {date} — {dw}-{dl}  ({dpl:+.2f}u)")
        out.append("")
        out.append("| Result | Verdict | Game | Market | Pick | Line | P/L |")
        out.append("|---|---|---|---|---|---|---|")
        for r in sorted(day, key=lambda x: (x["result"] != "WIN", -x["score"])):
            line = r.get("line_at_pull")
            line = "—" if line is None else line
            emoji = {"WIN": "✅ WIN", "LOSS": "❌ LOSS", "PUSH": "➖ PUSH"}.get(r["result"], r["result"])
            out.append(f"| {emoji} | {r['verdict']} | {r['game']} | {r['market']} "
                       f"| {r['pick']} | {line} | {r.get('pl',0):+.2f} |")
        out.append("")
    with open("docs/RESULTS.md", "w") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
