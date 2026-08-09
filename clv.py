#!/usr/bin/env python3
"""clv.py — capture closing lines for today's locked picks and compute CLV.

Runs near first pitch (22:45 UTC schedule). For every pick locked for
today's slate that has no closing price yet, this fetches current market
prices and records:

  close_odds  — current price for the SAME side at the SAME book (falls
                back to best available book on that side)
  close_line  — current line for point markets (totals / F5 / RL)
  clv         — percent value vs close, decimal-odds ratio:
                (dec_locked / dec_close - 1) * 100. Positive = the locked
                price beat the close (the sharp-side signal).

HONESTY RULES:
  * For point markets, price CLV is only computed when the closing line
    equals the locked line — comparing an Under 10.5 price to an Under 10.0
    price is apples to oranges. When the line moved, clv stays None and
    line_move records the direction (favorable/unfavorable for the side).
  * A pick with no matching close (game started early, market pulled) is
    left untouched — never guessed.
  * This script only ADDS close fields; it never alters picks or grades.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# unpack embedded package if needed (same bootstrap as grade.py)
try:
    from mlb_betting_model.worker_client import WorkerClient
except Exception:
    import base64, io, re, zipfile
    if os.path.exists("run.py"):
        m = re.search(r'_PKG_B64 = "([A-Za-z0-9+/=]+)"', open("run.py").read())
        if m:
            with zipfile.ZipFile(io.BytesIO(base64.b64decode(m.group(1)))) as zf:
                zf.extractall(".")
    from mlb_betting_model.worker_client import WorkerClient

from mlb_betting_model.parsers import parse_odds

LOCK = "docs/locked_picks.jsonl"
ET = ZoneInfo("America/New_York")
BOOKMAKERS = "draftkings,fanduel"
PERIOD_MARKETS = "h2h_1st_5_innings,totals_1st_5_innings,totals_1st_1_innings"


def to_decimal(american):
    return (american / 100.0 + 1.0) if american > 0 else (100.0 / abs(american) + 1.0)


def fetch_close_quotes(client, need_core=True, need_period=True):
    """Closing quotes — but ONLY for market groups with locked picks
    awaiting closes (credit economy, 2026-08-09). Skipping the per-event
    period loop on days with no period picks saves ~30 credits."""
    odds = []
    if need_core:
        try:
            core = client.odds(markets="h2h,totals", bookmakers=BOOKMAKERS)
            odds.extend(core or [])
        except Exception as exc:
            print(f"[clv] core odds unavailable ({exc})")
    if not need_period:
        return parse_odds(odds)
    try:
        for ev in (client.events() or []):
            ev_id = ev.get("id")
            if not ev_id:
                continue
            try:
                eo = client.event_odds(ev_id, markets=PERIOD_MARKETS,
                                       bookmakers=BOOKMAKERS)
                if eo and (eo.get("bookmakers") or []):
                    odds.append(eo)
            except Exception:
                continue
    except Exception as exc:
        print(f"[clv] period odds unavailable ({exc})")
    return parse_odds(odds)


def index_quotes(quotes):
    """(game, market_key, outcome, point) -> {book: price}; plus per-market
    median close line per game."""
    px = {}
    pts = {}
    for q in quotes:
        game = f"{q.away_team} @ {q.home_team}" if getattr(q, "away_team", None) else None
        if game is None:
            continue
        key = (game, q.market_key, q.outcome_name, q.point)
        px.setdefault(key, {})[q.book_title] = q.price
        if q.point is not None:
            pts.setdefault((game, q.market_key), []).append(q.point)
    lines = {k: sorted(v)[len(v) // 2] for k, v in pts.items()}
    return px, lines


def side_for(row):
    """Map a locked row to (market_key, outcome_name, needs_point)."""
    game = row["game"]
    away, home = game.split(" @ ", 1)
    mkt, pick = row["market"], row["pick"]
    if mkt == "Moneyline":
        team = home if pick.startswith(home) else away
        return "h2h", team, False
    if mkt == "Total":
        return "totals", ("Over" if pick.startswith("Over") else "Under"), True
    if mkt == "Run Line":
        team = home if pick.startswith(home) else away
        return "spreads", team, True
    if mkt == "F5 Total":
        return "totals_1st_5_innings", ("Over" if "Over" in pick else "Under"), True
    if mkt == "NRFI":
        return "totals_1st_1_innings", ("Under" if pick == "NRFI" else "Over"), True
    return None, None, False


def main():
    today = datetime.now(ET).strftime("%Y-%m-%d")
    if not os.path.exists(LOCK):
        print("No locked picks file.")
        return
    rows = [json.loads(l) for l in open(LOCK) if l.strip()]
    todo = [r for r in rows if r.get("slate_date") == today
            and r.get("close_odds") is None and not r.get("clv_final")]
    if not todo:
        print(f"CLV: nothing to capture for {today}.")
        return

    client = WorkerClient()
    need_core = any(r["market"] in ("Moneyline", "Total", "Run Line") for r in todo)
    need_period = any(r["market"] in ("F5 Total", "NRFI") for r in todo)
    quotes = fetch_close_quotes(client, need_core, need_period)
    if not quotes:
        print("CLV: no quotes returned — leaving picks untouched.")
        return
    px, lines = index_quotes(quotes)

    captured = skipped = 0
    for r in todo:
        mk, outcome, has_point = side_for(r)
        if mk is None:
            continue
        game = r["game"]
        locked_line = r.get("line_at_pull")
        want_point = locked_line if has_point else None
        if r["market"] == "Run Line":
            want_point = -1.5 if r["pick"].endswith("-1.5") or "-1.5" in r["pick"] else want_point
        books = px.get((game, mk, outcome, want_point)) or {}
        close_line = lines.get((game, mk))
        # same-book first, else best available on that side
        close = books.get(r.get("best_book"))
        if close is None and books:
            close = max(books.values())

        if has_point and locked_line is not None and close_line is not None \
                and close_line != locked_line:
            # line moved — record direction, no price CLV
            if outcome == "Under" or r["market"] == "NRFI" and r["pick"] == "NRFI":
                fav = close_line < locked_line
            elif outcome == "Over":
                fav = close_line > locked_line
            else:
                fav = None
            r["close_line"] = close_line
            r["close_odds"] = close
            r["clv"] = None
            r["clv_note"] = (f"line moved {locked_line} -> {close_line}"
                             + ("" if fav is None else (" (favorable)" if fav else " (unfavorable)")))
            r["clv_final"] = True
            captured += 1
            continue

        if close is None:
            skipped += 1
            continue

        locked = None
        bks = r.get("books") or {}
        locked = bks.get(r.get("best_book")) or (max(bks.values()) if bks else None)
        if locked is None:
            skipped += 1
            continue
        r["close_odds"] = close
        if close_line is not None:
            r["close_line"] = close_line
        r["clv"] = round((to_decimal(locked) / to_decimal(close) - 1.0) * 100.0, 2)
        r["clv_final"] = True
        captured += 1

    with open(LOCK, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"CLV: captured closes for {captured} picks "
          f"({skipped} unmatched — started early or market pulled).")


if __name__ == "__main__":
    main()
