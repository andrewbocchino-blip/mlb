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

# v15 validation: CLV, segmentation, artifact-checking (applies to both models)
try:
    from mlb_betting_model.v15.validation import summarize_segments, artifact_flags
except Exception:
    summarize_segments = None
    artifact_flags = None


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
                if ar is None or hr is None:
                    continue
                # v16: per-inning linescore for NRFI / F5 grading
                first = f5 = None
                innings = ((g.get("linescore") or {}).get("innings") or [])
                if innings:
                    def _runs(inn, side):
                        v = (inn.get(side) or {}).get("runs")
                        return v if isinstance(v, (int, float)) else 0
                    inns = sorted(innings, key=lambda i: i.get("num") or 0)
                    if inns and (inns[0].get("num") == 1):
                        first = (_runs(inns[0], "away"), _runs(inns[0], "home"))
                    if len(inns) >= 5:
                        a5 = sum(_runs(i, "away") for i in inns[:5])
                        h5 = sum(_runs(i, "home") for i in inns[:5])
                        f5 = (a5, h5)
                finals[(away, home)] = {"final": (ar, hr), "first": first, "f5": f5}
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
    fin = finals[key]
    ar, hr = fin["final"]
    total = ar + hr
    mkt = row["market"]
    pick = row["pick"]

    # PAYOUT BUGFIX (2026-07-18): grade P&L at the odds LOCKED at pull time
    # (best book), not a flat +0.91. Falls back to the conservative flat
    # payout only when no locked price exists.
    def _locked_odds():
        books = row.get("books") or {}
        bb = row.get("best_book")
        px = books.get(bb) if bb else None
        if px is None and books:
            px = max(books.values())
        return px

    if mkt == "Total":
        line = row.get("line_at_pull")
        if line is None:
            return None, None
        if total == line:
            return "PUSH", 0.0
        over = total > line
        win = (over and pick.startswith("Over")) or ((not over) and pick.startswith("Under"))
        return ("WIN" if win else "LOSS"), american_payout(_locked_odds(), win)

    if mkt == "F5 Total":
        line = row.get("line_at_pull")
        if line is None or fin.get("f5") is None:
            return None, None
        a5, h5 = fin["f5"]
        t5 = a5 + h5
        if t5 == line:
            return "PUSH", 0.0
        over = t5 > line
        win = (over and "Over" in pick) or ((not over) and "Under" in pick)
        return ("WIN" if win else "LOSS"), american_payout(_locked_odds(), win)

    if mkt == "NRFI":
        if fin.get("first") is None:
            return None, None
        a1, h1 = fin["first"]
        scored = (a1 + h1) > 0
        win = (pick == "YRFI" and scored) or (pick == "NRFI" and not scored)
        return ("WIN" if win else "LOSS"), american_payout(_locked_odds(), win)

    if mkt == "Moneyline":
        home_won = hr > ar
        picked_home = pick.startswith(home)
        win = (home_won and picked_home) or ((not home_won) and not picked_home)
        return ("WIN" if win else "LOSS"), american_payout(_locked_odds(), win)

    if mkt == "Run Line":
        picked_home = pick.startswith(home)
        margin = (hr - ar) if picked_home else (ar - hr)
        win = margin >= 2  # laying -1.5
        return ("WIN" if win else "LOSS"), american_payout(_locked_odds(), win)

    return None, None


BOARD = "docs/nrfi_board.jsonl"


def load_board():
    try:
        with open(BOARD) as f:
            return [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        return []


def grade_board(board, finals_by_date):
    """Grade forced NRFI/YRFI calls against the actual first inning."""
    changed = 0
    for r in board:
        if r.get("graded"):
            continue
        fin = (finals_by_date.get(r["slate_date"]) or {})
        for (away, home), f in fin.items():
            if f.get("first") is None:
                continue
            if f"{away} @ {home}" == r["game"]:
                a1, h1 = f["first"]
                actual = "YRFI" if (a1 + h1) > 0 else "NRFI"
                r["graded"] = True
                r["result"] = "HIT" if actual == r["call"] else "MISS"
                changed += 1
                break
    return changed


def main():
    client = WorkerClient()
    rows = load_locked()
    board = load_board()
    if not rows and not board:
        print("No locked picks yet.")
        return

    # group dates needing grading (locked picks + board dates)
    dates = sorted({r["slate_date"] for r in rows} | {b["slate_date"] for b in board})
    finals_by_date = {d: fetch_finals(client, d) for d in dates}

    b_changed = grade_board(board, finals_by_date)
    if board:
        with open(BOARD, "w") as f:
            for b in board:
                f.write(json.dumps(b) + "\n")
        if b_changed:
            print(f"Graded {b_changed} NRFI/YRFI board calls.")

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

    write_picks_md(rows, board)
    write_results_md(rows)
    print(f"Graded {changed} newly-final picks. Wrote docs/PICKS.md and docs/RESULTS.md")


def _books_cell(row):
    """Render both books' prices, bolding the better (higher American odds)."""
    books = row.get("books") or {}
    if not books:
        return "—"
    best = row.get("best_book")
    parts = []
    for bk, price in sorted(books.items(), key=lambda kv: -kv[1]):
        disp = f"{'+' if price > 0 else ''}{price}"
        if bk == best:
            parts.append(f"**{bk} {disp}**")   # bold the better line
        else:
            parts.append(f"{bk} {disp}")
    return " / ".join(parts)


def write_picks_md(rows, board=None):
    board = board or []
    # Dedupe to one row per unique bet per date (keep the latest pull), so
    # re-runs of the same slate don't show the pick twice. The raw
    # locked_picks.jsonl still preserves every timestamped pull.
    latest = {}
    for r in rows:
        key = (r.get("model", "A"), r["slate_date"], r["game"], r["market"], r["pick"])
        prev = latest.get(key)
        if prev is None or r.get("pulled_at", "") >= prev.get("pulled_at", ""):
            latest[key] = r
    deduped = list(latest.values())

    by_date = {}
    for r in deduped:
        by_date.setdefault(r["slate_date"], []).append(r)
    out = ["# Locked Picks — A/B", "", "Picks frozen at the line they were taken at. "
           "**Model A** = current (v14.3). **Model B** = variant. "
           "Both books shown; **bold = better price**. One row per bet. Paper only.", ""]
    for date in sorted(by_date, reverse=True):
        out.append(f"## {date}")
        out.append("")
        out.append("| Model | Verdict | Score | Game | Market | Pick | Line | Books (best in bold) |")
        out.append("|---|---|---|---|---|---|---|---|")
        for r in sorted(by_date[date], key=lambda x: (x.get("model", "A"), -x["score"])):
            line = r.get("line_at_pull")
            line = "—" if line is None else line
            out.append(f"| {r.get('model','A')} | {r['verdict']} | {r['score']} | {r['game']} | {r['market']} "
                       f"| {r['pick']} | {line} | {_books_cell(r)} |")
        out.append("")
        day_board = [b for b in board if b["slate_date"] == date]
        if day_board:
            out.append(f"#### NRFI/YRFI Board — forced calls (calibration record, NOT bets)")
            out.append("")
            out.append("| Game | Call | Confidence | Model P | Market P | Edge | Result |")
            out.append("|---|---|---|---|---|---|---|")
            conf_order = {"High": 0, "Medium": 1, "Low": 2, "Coin flip": 3}
            for b in sorted(day_board, key=lambda x: (conf_order.get(x["confidence"], 9),
                                                      -(x.get("model_p") or 0))):
                mp = f"{b['model_p']:.0%}" if b.get("model_p") is not None else "—"
                kp = f"{b['market_p']:.0%}" if b.get("market_p") is not None else "— (no market)"
                ed = f"{b['edge']:+.1%}" if b.get("edge") is not None else "—"
                res = {"HIT": "✅ HIT", "MISS": "❌ MISS"}.get(b.get("result"), "pending")
                out.append(f"| {b['game']} | **{b['call']}** | {b['confidence']} | {mp} | {kp} | {ed} | {res} |")
            out.append("")
            graded_b = [b for b in board if b.get("graded")]
            if graded_b:
                tiers = []
                for tier in ("High", "Medium", "Low", "Coin flip"):
                    tb = [b for b in graded_b if b["confidence"] == tier]
                    if tb:
                        h = sum(1 for b in tb if b["result"] == "HIT")
                        tiers.append(f"{tier} {h}-{len(tb)-h}")
                if tiers:
                    out.append(f"*Board calibration (all time): {' · '.join(tiers)}*")
                    out.append("")
    with open("docs/PICKS.md", "w") as f:
        f.write("\n".join(out))
    return


def _dedupe(graded):
    """Collapse to one row per unique bet (model+date+game+market+pick), so a
    pick logged multiple times (per book, or re-pulled) is counted ONCE. Model
    A and Model B are kept separate by including the model tag in the key."""
    best = {}
    for r in graded:
        key = (r.get("model", "A"), r["slate_date"], r["game"], r["market"], r["pick"])
        if key not in best or (r.get("books") and not best[key].get("books")):
            best[key] = r
    return list(best.values())


def _model_summary(graded, label):
    """One model's headline line: W-L, win rate, ROI, avg CLV, + artifact flags."""
    risk = [r for r in graded if r["result"] in ("WIN", "LOSS")]
    w = sum(1 for r in risk if r["result"] == "WIN")
    l = sum(1 for r in risk if r["result"] == "LOSS")
    pl = sum(r.get("pl", 0) for r in risk)
    n = len(risk)
    roi = (pl / n * 100) if n else 0.0
    wr = (w / n * 100) if n else 0.0
    clvs = [r["clv"] for r in risk if r.get("clv") is not None]
    avg_clv = (sum(clvs) / len(clvs)) if clvs else None
    clv_str = f"{avg_clv:+.2f}%" if avg_clv is not None else "n/a (no closing lines yet)"
    line = (f"**Model {label}: {w}-{l}  ·  {wr:.0f}% win  ·  {pl:+.2f}u  ·  "
            f"{roi:+.1f}% ROI  ·  avg CLV {clv_str}**")
    flags = artifact_flags(risk) if artifact_flags else []
    return line, flags


def write_results_md(rows):
    graded_all = [r for r in rows if r.get("graded")]
    graded = _dedupe(graded_all)
    A = [r for r in graded if r.get("model", "A") == "A"]
    B = [r for r in graded if r.get("model") == "B"]

    out = ["# Results — A/B Test", "",
           "**Model A** = current model (v14.3, control). **Model B** = variant "
           "(stricter regression + literature weights). CLV measured from the real "
           "price vs close. Each unique bet counted once. Paper only — no real money.", ""]

    # headline comparison
    for label, g in (("A", A), ("B", B)):
        line, flags = _model_summary(g, label)
        out.append(line)
        for f in flags:
            out.append(f"  - ⚠️ _{f}_")
    out.append("")
    out.append("> CLV is the signal that matters here, not W-L — per the sharp-bettor "
               "method, beating the closing line is what indicates a real edge. A small "
               "sample of wins with negative CLV is luck, not edge.")
    out.append("")

    # segmentation: where does each model win? (find the ONE slice, if any)
    if summarize_segments:
        for label, g in (("A", A), ("B", B)):
            risk = [r for r in g if r["result"] in ("WIN", "LOSS")]
            if not risk:
                continue
            seg = summarize_segments(risk)
            out.append(f"### Model {label} — segments (finding the winning slice)")
            out.append("")
            for dim in ("market", "side", "fav_band"):
                buckets = seg.get(dim, {})
                if not buckets:
                    continue
                parts = []
                for name, b in sorted(buckets.items(), key=lambda kv: -kv[1]["roi"]):
                    clv = f", CLV {b['avg_clv']:+.1f}%" if b.get("avg_clv") is not None else ""
                    parts.append(f"{name} {b['w']}-{b['l']} ({b['roi']:+.0f}%{clv})")
                out.append(f"- **by {dim}:** " + "  ·  ".join(parts))
            out.append("")

    # per-model, per-day detail tables
    for label, g in (("A", A), ("B", B)):
        if not g:
            continue
        out.append(f"## Model {label} — picks by date")
        out.append("")
        by_date = {}
        for r in g:
            by_date.setdefault(r["slate_date"], []).append(r)
        for date in sorted(by_date, reverse=True):
            day = by_date[date]
            dw = sum(1 for r in day if r["result"] == "WIN")
            dl = sum(1 for r in day if r["result"] == "LOSS")
            dpl = sum(r.get("pl", 0) for r in day)
            out.append(f"### {date} — {dw}-{dl}  ({dpl:+.2f}u)")
            out.append("")
            out.append("| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |")
            out.append("|---|---|---|---|---|---|---|---|---|")
            for r in sorted(day, key=lambda x: (x["result"] != "WIN", -x["score"])):
                line = r.get("line_at_pull")
                line = "—" if line is None else line
                emoji = {"WIN": "✅ WIN", "LOSS": "❌ LOSS", "PUSH": "➖ PUSH"}.get(r["result"], r["result"])
                clv = f"{r['clv']:+.1f}%" if r.get("clv") is not None else "—"
                out.append(f"| {emoji} | {r['verdict']} | {r['game']} | {r['market']} "
                           f"| {r['pick']} | {line} | {_books_cell(r)} | {clv} | {r.get('pl',0):+.2f} |")
            out.append("")
    with open("docs/RESULTS.md", "w") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
