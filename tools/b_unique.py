#!/usr/bin/env python3
"""
b_unique.py — emit Model B picks that diverge from Model A.

Reads the "Locked Picks — A/B" markdown and prints, per date:
  NEW      — B made the pick, A did not
  UPGRADE  — both made the pick, but B graded it PLAY where A graded LEAN
  (optionally DROPPED — A made it, B didn't, with --show-drops)

"Bet worthy" filter: --min-score (default 5.0, the LEAN floor).
Use --plays-only to restrict to B PLAY grades.

Usage:
    python3 tools/b_unique.py locked_picks.md
    python3 tools/b_unique.py locked_picks.md --date 2026-07-08 --plays-only
    python3 tools/b_unique.py locked_picks.md --markdown >> site/b_divergence.md

Run it in Actions right after pick generation to publish a standing
"B divergence" section — the isolated record of the xERA/xwOBA signal.
"""

import argparse
import re
import sys
from collections import defaultdict

DATE_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})")
ROW_RE = re.compile(r"^\|\s*([AB])\s*\|")


def parse(path):
    """-> {date: {"A": {key: pick}, "B": {key: pick}}}"""
    days = defaultdict(lambda: {"A": {}, "B": {}})
    date = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = DATE_RE.match(line)
            if m:
                date = m.group(1)
                continue
            if not date or not ROW_RE.match(line):
                continue
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            # Model | Verdict | Score | Game | Market | Pick | Line | Books
            if len(cols) < 8:
                continue
            model, verdict, score, game, market, pick, ln, books = cols[:8]
            key = (game, market, pick, ln)
            days[date][model][key] = {
                "verdict": verdict,
                "score": float(score) if score else 0.0,
                "game": game, "market": market, "pick": pick,
                "line": ln, "books": books,
            }
    return days


def diverging(days, min_score, plays_only, show_drops):
    out = defaultdict(list)
    for date in sorted(days):
        a, b = days[date]["A"], days[date]["B"]
        for key, bp in b.items():
            if bp["score"] < min_score:
                continue
            if plays_only and bp["verdict"] != "PLAY":
                continue
            if key not in a:
                out[date].append(("NEW", bp, None))
            elif bp["verdict"] == "PLAY" and a[key]["verdict"] == "LEAN":
                out[date].append(("UPGRADE", bp, a[key]))
        if show_drops:
            for key, ap in a.items():
                if key not in b:
                    out[date].append(("DROPPED", ap, None))
    return out


def fmt_row(tag, p, ap):
    note = f" (A: {ap['verdict']} {ap['score']})" if ap else ""
    books = p["books"] if p["books"] and p["books"] != "—" else "no line captured"
    return (f"  [{tag:7s}] {p['verdict']} {p['score']:>4} | {p['market']:9s} | "
            f"{p['pick']} — {p['game']} | {books}{note}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="locked picks markdown file")
    ap.add_argument("--min-score", type=float, default=5.0)
    ap.add_argument("--plays-only", action="store_true")
    ap.add_argument("--show-drops", action="store_true",
                    help="also list A picks that B dropped")
    ap.add_argument("--date", help="only this date (YYYY-MM-DD)")
    ap.add_argument("--markdown", action="store_true",
                    help="emit a markdown section instead of plain text")
    args = ap.parse_args()

    days = parse(args.path)
    if args.date:
        days = {d: v for d, v in days.items() if d == args.date}

    div = diverging(days, args.min_score, args.plays_only, args.show_drops)

    if not div:
        print("No B divergence found for the selected range/filters.")
        return

    total = 0
    for date in sorted(div, reverse=True):
        rows = div[date]
        if not rows:
            continue
        total += sum(1 for t, *_ in rows if t != "DROPPED")
        if args.markdown:
            print(f"\n### {date} — B divergence")
            print("| Type | Verdict | Score | Market | Pick | Game | Books |")
            print("|---|---|---|---|---|---|---|")
            for tag, p, ap in rows:
                note = f" (A: {ap['verdict']} {ap['score']})" if ap else ""
                print(f"| {tag} | {p['verdict']}{note} | {p['score']} | "
                      f"{p['market']} | {p['pick']} | {p['game']} | {p['books']} |")
        else:
            print(f"\n{date}")
            for tag, p, ap in rows:
                print(fmt_row(tag, p, ap))

    print(f"\n{total} diverging B pick(s) at score >= {args.min_score}"
          + (" (PLAYs only)" if args.plays_only else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
