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


def locked_odds(row):
    """Best locked price for a row, or None."""
    books = row.get("books") or {}
    bb = row.get("best_book")
    px = books.get(bb) if bb else None
    if px is None and books:
        px = max(books.values())
    return px


def reprice_historical(rows):
    """REPRICE PASS (2026-08-06): rows graded before the payout fix carry a
    flat +0.91 on every win. Recompute P&L at the locked best-book odds.
    Idempotent: corrected rows are flagged 'repriced' and never touched
    again. LOSS/PUSH amounts are unchanged (-1.0 / 0.0 were always right)."""
    fixed = 0
    delta = 0.0
    for r in rows:
        if not r.get("graded") or r.get("repriced"):
            continue
        if r.get("result") != "WIN":
            r["repriced"] = True
            continue
        odds = locked_odds(r)
        correct = round(american_payout(odds, True), 2)
        if abs(correct - (r.get("pl") or 0)) >= 0.005:
            delta += correct - (r.get("pl") or 0)
            r["pl"] = correct
            fixed += 1
        r["repriced"] = True
    if fixed:
        print(f"Repriced {fixed} historical wins at locked odds (net P&L change {delta:+.2f}u).")
    return fixed


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
        return locked_odds(row)

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


PROPS = "docs/props_board.jsonl"


def load_props():
    try:
        with open(PROPS) as f:
            return [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        return []


def grade_props(client, board):
    """Grade prop calls off each player's game log for the slate date.
    HR props: did he homer. K props: strikeouts vs the locked line."""
    changed = 0
    cache = {}
    for r in board:
        if r.get("graded"):
            continue
        season = int(r["slate_date"][:4])
        group = "pitching" if r["market"] == "pitcher_strikeouts" else "hitting"
        STAT_KEYS = {
            "batter_home_runs": ("homeRuns",),
            "pitcher_strikeouts": ("strikeOuts",),
            "batter_strikeouts": ("strikeOuts",),
            "batter_hits": ("hits",),
            "batter_rbis": ("rbi",),
            "batter_hits_runs_rbis": ("hits", "runs", "rbi"),   # composite
        }
        pid = r.get("player_id")
        if pid is None:
            continue
        key = (pid, group)
        if key not in cache:
            try:
                cache[key] = client.get_json(
                    f"mlb/people/{pid}/stats",
                    {"stats": "gameLog", "group": group, "season": season})
            except Exception:
                cache[key] = None
        resp = cache[key]
        if not resp:
            continue
        day = []
        for blk in (resp.get("stats") or []):
            for sp in (blk.get("splits") or []):
                if sp.get("date") == r["slate_date"]:
                    day.append(sp.get("stat") or {})
        if not day:
            continue          # didn't play / not final yet — stays pending
        if len(day) > 1:
            # Props settle on a SINGLE game. Summing both halves of a
            # doubleheader (1 hit + 1 hit graded against Over 1.5 as a
            # win) is simply wrong, and we don't store the gamePk needed
            # to pick the right half. Void rather than grade it falsely.
            r["graded"] = True
            r["result"] = "VOID"
            r["actual"] = None
            r["void_reason"] = "doubleheader — per-game settlement not determinable"
            changed += 1
            continue
        keys = STAT_KEYS.get(r["market"])
        if not keys:
            continue
        total = 0
        for st in day:
            for kkey in keys:
                try:
                    total += int(st.get(kkey) or 0)
                except (TypeError, ValueError):
                    pass
        line = float(r["line"])
        if total == line:
            r["graded"], r["result"], r["actual"] = True, "PUSH", total
        else:
            went_over = total > line
            hit = (went_over and r["side"] == "Over") or ((not went_over) and r["side"] == "Under")
            r["graded"] = True
            r["result"] = "HIT" if hit else "MISS"
            r["actual"] = total
        changed += 1
    return changed


BOARD = "docs/nrfi_board.jsonl"
HRBOARD = "docs/hr_board.jsonl"


def load_hr_board():
    try:
        with open(HRBOARD) as f:
            return [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        return []


def grade_hr_board(client, board):
    """Did each listed player homer on the slate date? (Doubleheaders: any
    game that day counts.) One gameLog call per ungraded player."""
    changed = 0
    log_cache = {}
    for r in board:
        if r.get("graded"):
            continue
        pid = r.get("player_id")
        season = int(r["slate_date"][:4])
        if pid not in log_cache:
            try:
                log_cache[pid] = client.get_json(
                    f"mlb/people/{pid}/stats",
                    {"stats": "gameLog", "group": "hitting", "season": season})
            except Exception:
                log_cache[pid] = None
        resp = log_cache[pid]
        if not resp:
            continue
        day_games = []
        for blk in (resp.get("stats") or []):
            for sp in (blk.get("splits") or []):
                if sp.get("date") == r["slate_date"]:
                    day_games.append(sp.get("stat") or {})
        if not day_games:
            continue  # hasn't played yet / off day — stays pending
        hrs = 0
        for st in day_games:
            try:
                hrs += int(st.get("homeRuns") or 0)
            except (TypeError, ValueError):
                pass
        r["graded"] = True
        r["result"] = "HIT" if hrs > 0 else "MISS"
        changed += 1
    return changed


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

    props_board = load_props()
    p_changed = grade_props(client, props_board)
    if props_board:
        with open(PROPS, "w") as f:
            for b in props_board:
                f.write(json.dumps(b) + "\n")
        if p_changed:
            print(f"Graded {p_changed} prop calls.")

    hr_board = load_hr_board()
    hr_changed = grade_hr_board(client, hr_board)
    if hr_board:
        with open(HRBOARD, "w") as f:
            for b in hr_board:
                f.write(json.dumps(b) + "\n")
        if hr_changed:
            print(f"Graded {hr_changed} HR board calls.")

    b_changed = grade_board(board, finals_by_date)
    if board:
        with open(BOARD, "w") as f:
            for b in board:
                f.write(json.dumps(b) + "\n")
        if b_changed:
            print(f"Graded {b_changed} NRFI/YRFI board calls.")

    reprice_historical(rows)

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

    write_picks_md(rows, board, hr_board, props_board)
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


def write_picks_md(rows, board=None, hr_board=None, props_board=None):
    board = board or []
    hr_board = hr_board or []
    props_board = props_board or []
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
    # BOARD VISIBILITY FIX (2026-08-11): the boards render inside the per-date
    # loop, so a slate with zero locked picks used to drop its NRFI/HR/prop
    # tables entirely even though they were written to disk. Iterate over the
    # UNION of pick dates and board dates.
    for _b in list(board) + list(hr_board) + list(props_board):
        by_date.setdefault(_b["slate_date"], [])
    out = ["# Locked Picks — A/B", "", "Picks frozen at the line they were taken at. "
           "**Model A** = current (v14.3). **Model B** = variant. "
           "Both books shown; **bold = better price**. One row per bet. Paper only.", ""]
    for date in sorted(by_date, reverse=True):
        out.append(f"## {date}")
        out.append("")
        if not by_date[date]:
            out.append("*No locked picks — model passed the slate. Boards below are "
                       "calibration records, not bets.*")
            out.append("")
        else:
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
        day_hr = [b for b in hr_board if b["slate_date"] == date]
        if day_hr:
            out.append("#### HR Board — Top 10 P(HR) (calibration record, NOT bets — lineups unconfirmed)")
            out.append("")
            out.append("| # | Player | Team | Game | P(HR) | Park | Wx | vs SP | Result |")
            out.append("|---|---|---|---|---|---|---|---|---|")
            for b in sorted(day_hr, key=lambda x: x.get("rank") or 99):
                res = {"HIT": "✅ HR", "MISS": "❌ no HR"}.get(b.get("result"), "pending")
                out.append(f"| {b.get('rank','')} | {b.get('player','?')} | {b.get('team','—')} | {b.get('game','—')} "
                           f"| {b.get('p_hr',0):.0%} | {b.get('park_f',1):.2f} "
                           f"| {b.get('wx_f',1):.2f} | {b.get('sp_f',1):.2f} | {res} |")
            out.append("")
            graded_hr = [b for b in hr_board if b.get("graded")]
            if graded_hr:
                exp = sum(b["p_hr"] for b in graded_hr)
                hits = sum(1 for b in graded_hr if b["result"] == "HIT")
                out.append(f"*HR board calibration (all time): {hits} homered of "
                           f"{len(graded_hr)} listed · model expected {exp:.1f}*")
                out.append("")
        day_props = [b for b in props_board if b["slate_date"] == date]
        if day_props:
            MKT = {"batter_home_runs": "HR", "pitcher_strikeouts": "Ks (P)",
                   "batter_strikeouts": "Ks (B)", "batter_hits": "Hits",
                   "batter_rbis": "RBI", "batter_hits_runs_rbis": "H+R+RBI"}
            out.append("#### Prop Divergence — model vs **no-vig** market "
                       "(calibration record, NOT bets)")
            out.append("")
            out.append("*Divergence means our number disagrees with the market — it does "
                       "NOT mean the market is wrong. The market price already contains "
                       "every sharp model working on this game; when we disagree, the "
                       "more likely explanation is that our number is worse. Until this "
                       "board beats its baseline, read a large divergence as a warning "
                       "about our projection, not an opportunity.*")
            out.append("")
            out.append("| Player | Mkt | Tier | Call | Line | Price | Book | Model | No-vig | Diverg. | EV | Result |")
            out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
            in_band = [b for b in day_props if b.get("in_band", True)]
            parlay = [b for b in day_props if b.get("parlay_only")]
            for b in sorted(in_band, key=lambda x: (-(x.get("rank_score") or 0),
                                                    -(x.get("ev") or 0)))[:15]:
                res = {"HIT": "✅ HIT", "MISS": "❌ MISS", "PUSH": "➖ PUSH",
                       "VOID": "⊘ VOID"}.get(b.get("result"), "pending")
                if b.get("actual") is not None:
                    res += f" ({b['actual']})"
                star = "**" if b.get("qualified") else ""
                px = b.get("price")
                pxs = f"{'+' if px and px > 0 else ''}{int(px)}" if px is not None else "—"
                out.append(f"| {star}{b['player']}{star} | {MKT.get(b['market'], b['market'])} "
                           f"| {b.get('tier','?')} | {b['side']} | {b['line']} | {pxs} | {b.get('book','—')} "
                           f"| {b['model_p']:.0%} | {b['novig_p']:.0%} | {b['edge']:+.1%} "
                           f"| {b.get('ev', 0):+.1%} | {res} |")
            out.append("")
            nq = sum(1 for b in day_props if b.get("qualified"))
            out.append(f"*Scanned {len(day_props)} priced props today; {nq} cleared their "
                       f"market's EV gate. With this many comparisons some divergence is "
                       f"guaranteed by noise alone — the top of the board is exactly where "
                       f"model error concentrates, so treat rank as a research queue, not a "
                       f"confidence order.*")
            out.append("")
            gp = [b for b in props_board if b.get("graded") and b.get("result") in ("HIT", "MISS")]
            n_void = sum(1 for b in props_board if b.get("result") == "VOID")
            if gp:
                q = [b for b in gp if b.get("qualified")]
                def _rec(rows_):
                    h = sum(1 for b in rows_ if b["result"] == "HIT")
                    exp = sum(b["model_p"] for b in rows_)
                    return f"{h}-{len(rows_)-h} (model expected {exp:.1f} hits)"
                line = f"*Prop calibration (all time): all calls {_rec(gp)}*"
                if n_void:
                    line += f" · {n_void} void"
                if q:
                    line += f" · *gate-clearing calls {_rec(q)}*"
                for t in ("A", "B", "C"):
                    tb = [b for b in gp if b.get("tier") == t]
                    if tb:
                        line += f" · *tier {t} {_rec(tb)}*"
                out.append(line)
                out.append("")
            if parlay:
                out.append("")
                out.append("**Parlay-leg candidates** (heavier juice than the "
                           "-250 straight-bet floor; only worth considering inside a "
                           "multi-leg ticket where the combined price justifies it)")
                out.append("")
                out.append("| Player | Mkt | Call | Line | Price | Model | No-vig | Result |")
                out.append("|---|---|---|---|---|---|---|---|")
                for b in sorted(parlay, key=lambda x: -(x.get("ev") or 0))[:6]:
                    px = b.get("price")
                    pxs = f"{'+' if px and px > 0 else ''}{int(px)}" if px is not None else "—"
                    res = {"HIT": "✅", "MISS": "❌", "PUSH": "➖", "VOID": "⊘"}.get(b.get("result"), "pending")
                    out.append(f"| {b['player']} | {MKT.get(b['market'], b['market'])} "
                               f"| {b['side']} | {b['line']} | {pxs} "
                               f"| {b['model_p']:.0%} | {b['novig_p']:.0%} | {res} |")
                out.append("")
                out.append("> A parlay multiplies the vig on every leg. Two legs at -300 "
                           "each is a -900 ticket needing ~90% to break even — only "
                           "sensible if BOTH legs are genuinely mispriced, which we have "
                           "not demonstrated.")
                out.append("")

            # PROP CLV — known at close, long before results are. This is
            # the fastest honest verdict available on the board: beating the
            # closing prop price does not require outsmarting the market,
            # only being early to a move it later makes.
            clvs = [b["clv"] for b in props_board if b.get("clv") is not None]
            if clvs:
                _avg = sum(clvs) / len(clvs)
                _pos = sum(1 for c in clvs if c > 0)
                out.append(f"**Prop CLV: {_avg:+.2f}%** across {len(clvs)} closed rows "
                           f"({_pos}/{len(clvs)} beat the close).")
                out.append("")
                if _avg <= 0:
                    out.append("> Negative or flat CLV means the market moved AGAINST our "
                               "calls after we made them — the clearest available evidence "
                               "that the divergences are our error, not the market's.")
                else:
                    out.append("> Positive CLV is the first real evidence this board carries "
                               "information. It needs to persist over a few hundred rows "
                               "before it means anything.")
                out.append("")
            out.append("*Ranked by EV discounted for how much evidence each market has: "
                       "pitcher Ks (backtest Brier 0.2307 vs 0.2466 blind) rank at full "
                       "weight, HR and RBI at half or less because neither has "
                       "demonstrated skill. Price band: -250 to +250 for most markets "
                       "(worse than -250 needs 71%+ to break even); HR props run to "
                       "+955 since the market is priced as longshots by nature. Rows at "
                       "+400 or longer carry a caution — our probability estimate is "
                       "least reliable at that scale, and so is the devig.*")
            out.append("")
            out.append("*Bold = cleared its market's no-vig edge gate with no data-quality flags. "
                       "Edge is measured against the vig-free price, never the raw line.* "
                       "**Tier A** = skill-rate model with matchup (HR, pitcher Ks). "
                       "**Tier B** = rate model, no platoon splits (hits, batter Ks). "
                       "**Tier C** = experimental (RBI, H+R+RBI): depends on teammates reaching "
                       "base, and H+R+RBI sums correlated components as independent, which "
                       "understates variance — research only.")
            out.append("")
            shown = [b for b in sorted(day_props, key=lambda x: -x.get("ev", 0))[:15]
                     if b.get("basis") or b.get("flags")]
            if shown:
                out.append("<details><summary>Inputs behind each call</summary>")
                out.append("")
                for b in shown:
                    bits = list(b.get("basis") or [])
                    for fl in (b.get("flags") or []):
                        bits.append(f"⚠️ {fl}")
                    out.append(f"- **{b['player']}** ({b['side']} {b['line']}): " + " · ".join(bits))
                out.append("")
                out.append("</details>")
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


def _standings_block(out):
    """Calibration standings for every board — the scoreboard that decides
    whether any of these models has earned trust. Lives in RESULTS.md
    because it IS the result: not units won, but whether the stated
    probabilities match what actually happened."""
    board = load_board()
    hrb = load_hr_board()
    props = load_props()

    out.append("## Board calibration standings")
    out.append("")
    out.append("These boards are calibration records, not bets. The question is not "
               "whether they won — it is whether a call at a stated confidence lands "
               "at that rate. A tier that hits BELOW its stated probability is a model "
               "telling you it does not know what it claims to know.")
    out.append("")

    # ---- NRFI forced-call board ----
    gb = [b for b in board if b.get("result") in ("HIT", "MISS")]
    if gb:
        out.append("### NRFI/YRFI forced calls")
        out.append("")
        out.append("| Confidence | n | Hit | Miss | Hit% | Model said | Gap |")
        out.append("|---|---|---|---|---|---|---|")
        for tier in ("High", "Medium", "Low", "Coin flip"):
            tb = [b for b in gb if b.get("confidence") == tier]
            if not tb:
                continue
            h = sum(1 for b in tb if b["result"] == "HIT")
            act = h / len(tb)
            pred = sum(b.get("model_p") or 0 for b in tb) / len(tb)
            out.append(f"| {tier} | {len(tb)} | {h} | {len(tb)-h} | {act:.0%} "
                       f"| {pred:.0%} | {act-pred:+.0%} |")
        h_all = sum(1 for b in gb if b["result"] == "HIT")
        pred_all = sum(b.get("model_p") or 0 for b in gb) / len(gb)
        out.append(f"| **All** | **{len(gb)}** | **{h_all}** | **{len(gb)-h_all}** "
                   f"| **{h_all/len(gb):.0%}** | **{pred_all:.0%}** "
                   f"| **{h_all/len(gb)-pred_all:+.0%}** |")
        out.append("")
        yr = [b for b in gb if b.get("call") == "YRFI"]
        if yr:
            out.append(f"YRFI share of calls: **{len(yr)}/{len(gb)} ({len(yr)/len(gb):.0%})** "
                       f"— hitting {sum(1 for b in yr if b['result']=='HIT')/len(yr):.0%}.")
            out.append("")
        # NAIVE BASELINE. A forced-call board must beat "always call the
        # majority class" or it has no discriminating power at all. This is
        # the comparison that matters and the one the board kept failing:
        # through 8/15 it was 34-53 (39%) while always-NRFI would have gone
        # 51-36 (59%).
        n_nrfi_actual = sum(1 for b in gb
                            if (b.get("call") == "NRFI") == (b["result"] == "HIT"))
        base_rate = n_nrfi_actual / len(gb)
        naive = max(base_rate, 1 - base_rate)
        naive_side = "NRFI" if base_rate >= 0.5 else "YRFI"
        model_rate = h_all / len(gb)
        out.append(f"**Naive baseline check.** First innings were scoreless in "
                   f"**{base_rate:.1%}** of these games, so always calling {naive_side} "
                   f"scores **{naive:.1%}**. The model scores **{model_rate:.1%}**.")
        if model_rate < naive:
            out.append("")
            out.append("> ⚠️ **The model is losing to a coin that always says the same thing.** "
                       "Until it beats this line, its calls carry no information and should "
                       "not be treated as analysis — a forced call is only worth making if it "
                       "beats the majority class.")
        out.append("")

        hi = [b for b in gb if b.get("confidence") == "High"]
        if len(hi) >= 15:
            hi_rate = sum(1 for b in hi if b["result"] == "HIT") / len(hi)
            cf = [b for b in gb if b.get("confidence") == "Coin flip"]
            if cf and hi_rate < (sum(1 for b in cf if b["result"] == "HIT") / len(cf)):
                out.append("> ⚠️ **Confidence is inverted**: the High tier is hitting BELOW "
                           "the Coin flip tier. Whatever the confidence metric is measuring, "
                           "it is not the probability of being right. Calls at this tier "
                           "should carry no weight until this reverses.")
                out.append("")

    # ---- HR board ----
    ghr = [b for b in hrb if b.get("result") in ("HIT", "MISS")]
    if ghr:
        hits = sum(1 for b in ghr if b["result"] == "HIT")
        exp = sum(b.get("p_hr") or 0 for b in ghr)
        out.append("### HR board (top-10 daily)")
        out.append("")
        out.append(f"- listed and graded: **{len(ghr)}**")
        out.append(f"- homered: **{hits}** · model expected **{exp:.1f}**")
        out.append(f"- actual rate **{hits/len(ghr):.1%}** vs predicted **{exp/len(ghr):.1%}** "
                   f"(**{hits/len(ghr)-exp/len(ghr):+.1%}**)")
        out.append("")

    # ---- prop board ----
    gp = [b for b in props if b.get("result") in ("HIT", "MISS")]
    if gp:
        out.append("### Prop divergence board")
        out.append("")
        out.append("| Tier | Market | n | Hit | Miss | Hit% | Model said | Gap |")
        out.append("|---|---|---|---|---|---|---|---|")
        LABEL = {"batter_home_runs": "HR", "pitcher_strikeouts": "Ks (P)",
                 "batter_strikeouts": "Ks (B)", "batter_hits": "Hits",
                 "batter_rbis": "RBI", "batter_hits_runs_rbis": "H+R+RBI"}
        for tier in ("A", "B", "C"):
            tb = [b for b in gp if b.get("tier") == tier]
            for mkt in sorted({b["market"] for b in tb}):
                mb = [b for b in tb if b["market"] == mkt]
                h = sum(1 for b in mb if b["result"] == "HIT")
                act = h / len(mb)
                pred = sum(b.get("model_p") or 0 for b in mb) / len(mb)
                out.append(f"| {tier} | {LABEL.get(mkt, mkt)} | {len(mb)} | {h} "
                           f"| {len(mb)-h} | {act:.0%} | {pred:.0%} | {act-pred:+.0%} |")
        h_all = sum(1 for b in gp if b["result"] == "HIT")
        pred_all = sum(b.get("model_p") or 0 for b in gp) / len(gp)
        out.append(f"| **All** | | **{len(gp)}** | **{h_all}** | **{len(gp)-h_all}** "
                   f"| **{h_all/len(gp):.0%}** | **{pred_all:.0%}** "
                   f"| **{h_all/len(gp)-pred_all:+.0%}** |")
        out.append("")
        q = [b for b in gp if b.get("qualified")]
        if q:
            hq = sum(1 for b in q if b["result"] == "HIT")
            pq = sum(b.get("model_p") or 0 for b in q) / len(q)
            out.append(f"Gate-clearing calls only: **{hq}-{len(q)-hq}** "
                       f"({hq/len(q):.0%} vs {pq:.0%} predicted).")
            out.append("")
        nvoid = sum(1 for b in props if b.get("result") == "VOID")
        if nvoid:
            out.append(f"_{nvoid} void (doubleheaders — per-game settlement not determinable)._")
            out.append("")

    out.append("> **Sample-size reality check.** Distinguishing a real edge from noise "
               "needs hundreds of graded calls per tier. Gaps below are indicative, not "
               "verdicts — except where a tier is inverted against a lower tier, which is "
               "a structural signal rather than variance.")
    out.append("")




def _timing_block(out):
    """Does taking the slate early actually beat taking it late?

    The 8am pull takes prices before the day's money moves them; the 11am
    pull re-prices with confirmed lineups. Dedupe means the 8am lock is
    never overwritten, so any row the 11am run adds is one the 8am run
    passed on — and CLV on each tells us directly whether being early beat
    being better informed."""
    props = load_props()
    rows = [b for b in props if b.get("clv") is not None and b.get("pull_tag")]
    if len(rows) < 10:
        return
    out.append("## Early vs late pull")
    out.append("")
    out.append("| Pull | Rows | Avg CLV | Beat close |")
    out.append("|---|---|---|---|")
    for tag, name in (("early8", "8am (pre-move)"), ("late11", "11am (lineups)")):
        sel = [b for b in rows if b.get("pull_tag") == tag]
        if not sel:
            continue
        avg = sum(b["clv"] for b in sel) / len(sel)
        pos = sum(1 for b in sel if b["clv"] > 0)
        out.append(f"| {name} | {len(sel)} | **{avg:+.2f}%** | {pos}/{len(sel)} |")
    out.append("")
    e = [b["clv"] for b in rows if b.get("pull_tag") == "early8"]
    l = [b["clv"] for b in rows if b.get("pull_tag") == "late11"]
    if e and l:
        diff = (sum(e) / len(e)) - (sum(l) / len(l))
        if diff > 0.5:
            out.append(f"> The early pull is beating the late pull by **{diff:+.2f}%** CLV — "
                       f"taking the number before the day's money arrives is worth more "
                       f"than the extra information the later pull has.")
        elif diff < -0.5:
            out.append(f"> The late pull is ahead by **{-diff:.2f}%** CLV. Confirmed lineups "
                       f"are worth more here than being early.")
        else:
            out.append("> No meaningful difference yet. Needs a few hundred rows per pull.")
        out.append("")


def _recent_results_block(out, rows=None, days_back: int = 4):
    """Every call and its result, day by day — the full ledger.

    The previous version summarised ("HR 2 of 10") and showed only the top
    eight props, which meant answering "what did it pick yesterday and what
    happened" still required scrolling PICKS.md. Results belong on the
    results page in full: same tables as the picks, with the outcome
    attached to each row."""
    board = load_board()
    hrb = load_hr_board()
    props = load_props()
    rows = rows or []

    graded_dates = sorted(
        {b["slate_date"] for b in (board + hrb + props)
         if b.get("result") in ("HIT", "MISS", "PUSH", "VOID")}
        | {r["slate_date"] for r in rows
           if r.get("result") in ("WIN", "LOSS", "PUSH")},
        reverse=True)[:days_back]
    if not graded_dates:
        return

    ICON = {"HIT": "✅", "MISS": "❌", "WIN": "✅", "LOSS": "❌",
            "PUSH": "➖", "VOID": "⊘"}
    MKT = {"batter_home_runs": "HR", "pitcher_strikeouts": "Ks (P)",
           "batter_strikeouts": "Ks (B)", "batter_hits": "Hits",
           "batter_rbis": "RBI", "batter_hits_runs_rbis": "H+R+RBI"}

    out.append("## Daily ledger — every call, every result")
    out.append("")
    out.append(f"Last {len(graded_dates)} graded slates in full. Most recent first.")
    out.append("")

    for di, d in enumerate(graded_dates):
        dg = [r for r in rows if r.get("slate_date") == d
              and r.get("result") in ("WIN", "LOSS", "PUSH")
              and r.get("model", "A") == "A"]
        db = [b for b in board if b["slate_date"] == d
              and b.get("result") in ("HIT", "MISS")]
        dh = [b for b in hrb if b["slate_date"] == d
              and b.get("result") in ("HIT", "MISS")]
        dp = [b for b in props if b["slate_date"] == d
              and b.get("result") in ("HIT", "MISS", "PUSH", "VOID")]
        if not (dg or db or dh or dp):
            continue

        head = []
        if dg:
            w = sum(1 for r in dg if r["result"] == "WIN")
            pl = sum(r.get("pl") or 0 for r in dg)
            head.append(f"bets {w}-{len(dg)-w} ({pl:+.2f}u)")
        if dp:
            h = sum(1 for b in dp if b["result"] == "HIT")
            n = sum(1 for b in dp if b["result"] in ("HIT", "MISS"))
            head.append(f"props {h}-{n-h}")
        if db:
            h = sum(1 for b in db if b["result"] == "HIT")
            head.append(f"NRFI {h}-{len(db)-h}")
        if dh:
            h = sum(1 for b in dh if b["result"] == "HIT")
            head.append(f"HR {h}-{len(dh)-h}")
        out.append(f"### {d} — {' · '.join(head)}")
        out.append("")

        if dg:
            out.append("**Locked bets**")
            out.append("")
            out.append("| Market | Pick | Line | Price | Score | CLV | Result |")
            out.append("|---|---|---|---|---|---|---|")
            for r in sorted(dg, key=lambda x: -(x.get("score") or 0)):
                px = locked_odds(r)
                pxs = f"{'+' if px and px > 0 else ''}{int(px)}" if px is not None else "—"
                ln = r.get("line_at_pull")
                clv = f"{r['clv']:+.1f}%" if r.get("clv") is not None else "—"
                out.append(f"| {r['market']} | {r['pick']} | {ln if ln is not None else '—'} "
                           f"| {pxs} | {r.get('score','')} | {clv} "
                           f"| {ICON.get(r['result'],'')} {r.get('pl',0):+.2f}u |")
            out.append("")

        if dp:
            out.append("**Player props**")
            out.append("")
            out.append("| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |")
            out.append("|---|---|---|---|---|---|---|---|---|")
            for b in sorted(dp, key=lambda x: -(x.get("rank_score") or x.get("ev") or 0)):
                px = b.get("price")
                pxs = f"{'+' if px and px > 0 else ''}{int(px)}" if px is not None else "—"
                star = "**" if b.get("qualified") else ""
                clv = f"{b['clv']:+.1f}%" if b.get("clv") is not None else "—"
                out.append(f"| {star}{b['player']}{star} | {MKT.get(b['market'], b['market'])} "
                           f"| {b['side']} | {b['line']} | {pxs} | {b.get('model_p',0):.0%} "
                           f"| {b.get('actual','—')} | {clv} | {ICON.get(b.get('result'),'')} |")
            out.append("")
            out.append("*Bold = cleared its edge and EV gate.*")
            out.append("")

        if db:
            out.append("**NRFI / YRFI forced calls**")
            out.append("")
            out.append("| Game | Call | Confidence | Model | Market | Result |")
            out.append("|---|---|---|---|---|---|")
            order = {"High": 0, "Medium": 1, "Low": 2, "Coin flip": 3}
            for b in sorted(db, key=lambda x: order.get(x.get("confidence"), 9)):
                mk = f"{b['market_p']:.0%}" if b.get("market_p") is not None else "—"
                out.append(f"| {b['game']} | **{b['call']}** | {b.get('confidence','')} "
                           f"| {b.get('model_p',0):.0%} | {mk} | {ICON.get(b['result'],'')} |")
            out.append("")

        if dh:
            out.append("**HR board — top 10**")
            out.append("")
            out.append("| # | Player | Game | P(HR) | Result |")
            out.append("|---|---|---|---|---|")
            for b in sorted(dh, key=lambda x: x.get("rank") or 99):
                out.append(f"| {b.get('rank','')} | {b['player']} | {b.get('game','')} "
                           f"| {b.get('p_hr',0):.0%} | {ICON.get(b['result'],'')} |")
            exp = sum(b.get("p_hr") or 0 for b in dh)
            hits = sum(1 for b in dh if b["result"] == "HIT")
            out.append("")
            out.append(f"*{hits} homered · model expected {exp:.1f}*")
            out.append("")

        if di == 0 and len(graded_dates) > 1:
            out.append("---")
            out.append("")


def write_results_md(rows):
    graded_all = [r for r in rows if r.get("graded")]
    graded = _dedupe(graded_all)
    A = [r for r in graded if r.get("model", "A") == "A"]
    B = [r for r in graded if r.get("model") == "B"]

    out = ["# Results", ""]

    # ---- SCOREBOARD: every board's standing, at a glance, first thing ----
    board = load_board()
    hrb = load_hr_board()
    props = load_props()

    def _line(name, hits, n, pred, extra=""):
        if not n:
            return f"| {name} | — | no graded calls yet | | |"
        act = hits / n
        gap = act - pred if pred is not None else None
        verdict = ("🟢 ahead of its own number" if gap is not None and gap > 0.03
                   else "🔴 behind its own number" if gap is not None and gap < -0.03
                   else "🟡 tracking its number")
        return (f"| {name} | {hits}-{n-hits} | **{act:.1%}** | "
                f"{pred:.1%} | {verdict}{extra} |" if pred is not None
                else f"| {name} | {hits}-{n-hits} | **{act:.1%}** | — | {verdict}{extra} |")

    out.append("## Scoreboard")
    out.append("")
    out.append("| Board | Record | Hit rate | Model predicted | Standing |")
    out.append("|---|---|---|---|---|")

    gA = [r for r in _dedupe([x for x in rows if x.get("graded")])
          if r.get("model", "A") == "A" and r.get("result") in ("WIN", "LOSS")]
    if gA:
        w = sum(1 for r in gA if r["result"] == "WIN")
        pl = sum(r.get("pl") or 0 for r in gA)
        clvs = [r["clv"] for r in gA if r.get("clv") is not None]
        extra = f" · CLV {sum(clvs)/len(clvs):+.2f}%" if clvs else " · CLV pending"
        out.append(f"| **Locked bets** (ML/Total) | {w}-{len(gA)-w} | "
                   f"**{w/len(gA):.1%}** | — | {pl:+.2f}u{extra} |")

    gb = [b for b in board if b.get("result") in ("HIT", "MISS")]
    if gb:
        h = sum(1 for b in gb if b["result"] == "HIT")
        pred = sum(b.get("model_p") or 0 for b in gb) / len(gb)
        base = sum(1 for b in gb
                   if (b.get("call") == "NRFI") == (b["result"] == "HIT")) / len(gb)
        naive = max(base, 1 - base)
        flag = "" if h / len(gb) > naive else f" · ⚠️ below {naive:.0%} naive baseline"
        out.append(_line("NRFI/YRFI forced calls", h, len(gb), pred, flag))

    ghr = [b for b in hrb if b.get("result") in ("HIT", "MISS")]
    if ghr:
        h = sum(1 for b in ghr if b["result"] == "HIT")
        pred = sum(b.get("p_hr") or 0 for b in ghr) / len(ghr)
        out.append(_line("HR board (top 10 daily)", h, len(ghr), pred))

    gp = [b for b in props if b.get("result") in ("HIT", "MISS")]
    if gp:
        h = sum(1 for b in gp if b["result"] == "HIT")
        pred = sum(b.get("model_p") or 0 for b in gp) / len(gp)
        pclv = [b["clv"] for b in props if b.get("clv") is not None]
        extra = f" · CLV {sum(pclv)/len(pclv):+.2f}%" if pclv else " · CLV pending"
        out.append(_line("Player props (all tiers)", h, len(gp), pred, extra))
        for tier, name in (("A", "props · tier A (HR, pitcher K)"),
                           ("B", "props · tier B (hits, batter K)"),
                           ("C", "props · tier C (RBI, H+R+RBI)")):
            tb = [b for b in gp if b.get("tier") == tier]
            if len(tb) >= 5:
                th = sum(1 for b in tb if b["result"] == "HIT")
                tp = sum(b.get("model_p") or 0 for b in tb) / len(tb)
                out.append(_line(f"&nbsp;&nbsp;↳ {name}", th, len(tb), tp))

    out.append("")
    out.append("**Hit rate vs predicted is the whole test.** A board that hits at the rate "
               "it claims is trustworthy even when it loses; a board that hits below its "
               "own number is telling you it does not know what it claims to know.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("**Model A** = current model (control). **Model B** = retired variant, "
               "history preserved. CLV measured from the real price vs close. Each unique "
               "bet counted once. Paper only — no real money.")
    out.append("")

    # headline comparison
    for label, g in (("A", A), ("B", B)):
        line, flags = _model_summary(g, label)
        out.append(line)
        for f in flags:
            out.append(f"  - ⚠️ _{f}_")
    out.append("")
    _standings_block(out)

    _timing_block(out)
    _recent_results_block(out, rows)

    out.append("> **CLV caveat.** Beating the close is evidence of skill only when the "
               "move came from the market re-evaluating information we also had. If a "
               "scratch or injury broke after we locked, we collect the CLV without "
               "having known anything — that is luck wearing the costume of skill. Read "
               "CLV in aggregate, never on a single bet.")
    out.append("")
    out.append("> CLV is the signal that matters here, not W-L — per the sharp-bettor "
               "method, beating the closing line is what indicates a real edge. A small "
               "sample of wins with negative CLV is luck, not edge.")
    out.append("")

    # probability calibration: does the ML win model's number mean anything?
    ml_rows = [r for r in A if r["market"] == "Moneyline"
               and r.get("home_win_prob") is not None
               and r["result"] in ("WIN", "LOSS")]
    if ml_rows:
        pts = []
        for r in ml_rows:
            away, home = r["game"].split(" @ ", 1)
            picked_home = r["pick"].startswith(home)
            home_won = (r["result"] == "WIN") == picked_home
            pts.append((float(r["home_win_prob"]), 1.0 if home_won else 0.0))
        brier = sum((p - o) ** 2 for p, o in pts) / len(pts)
        out.append(f"### Moneyline probability calibration (Model A, n={len(pts)})")
        out.append("")
        out.append(f"Brier score: **{brier:.4f}** (0.25 = coin flip knowledge; lower is better)")
        out.append("")
        out.append("| Model home-win band | n | Predicted avg | Actual home-win % |")
        out.append("|---|---|---|---|")
        bands = [(0.0, 0.40), (0.40, 0.45), (0.45, 0.50), (0.50, 0.55),
                 (0.55, 0.60), (0.60, 0.65), (0.65, 1.01)]
        for lo, hi in bands:
            bp = [(p, o) for p, o in pts if lo <= p < hi]
            if not bp:
                continue
            pred = sum(p for p, _ in bp) / len(bp)
            act = sum(o for _, o in bp) / len(bp)
            label = f"{lo:.0%}–{hi:.0%}" if hi <= 1 else f"{lo:.0%}+"
            out.append(f"| {label} | {len(bp)} | {pred:.0%} | {act:.0%} |")
        out.append("")
        out.append("> Calibrated = predicted ≈ actual per band. Systematic gaps mean the "
                   "win probabilities themselves need retuning before any ML edge claim.")
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
