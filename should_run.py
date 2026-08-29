#!/usr/bin/env python3
"""should_run.py — decide what work today still owes, and do it.

GitHub Actions cron is not a reliable scheduler. It silently drops
schedules when a workflow file changes, delays runs under load (we have
seen 2.5 hours), and disables schedules entirely in repos with no recent
human commits. Relying on four exact cron times means a missed slot is
simply lost — which is what happened on 2026-08-18, when both period runs
never fired and the boards went dark for a day.

The fix is to stop treating cron as an alarm clock and start treating it as
a heartbeat. The workflow wakes up frequently, this script asks "what has
today not done yet?", and the answer drives a single run. A missed slot is
picked up by the next heartbeat instead of being lost.

WORK ITEMS, in priority order (earliest owed runs first):
  core     midnight line on ML/Totals            — owed from 04:00 UTC
  early8   period markets + boards, pre-move     — owed from 12:00 UTC
  late11   period markets + boards, with lineups — owed from 15:00 UTC
  clv      closing prices on everything locked   — owed from 22:45 UTC

IDEMPOTENCE. Completion is read from the artefacts themselves — the locked
picks ledger and the board files — not from a run log. So the answer is
correct even if a run crashed halfway, and re-running can never double-lock
a pick (the dedupe in run.py is the second guard).

Writes MODE / PULL_TAG / PERIOD_ONLY to $GITHUB_ENV, and prints the
decision. Exits 0 always; "nothing owed" is a normal outcome.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

LOCK = "docs/locked_picks.jsonl"
BOARDS = ("docs/props_board.jsonl", "docs/nrfi_board.jsonl", "docs/hr_board.jsonl")

# (key, owed-from UTC hour, owed-from UTC minute)
WINDOWS = [
    ("core",   4,  5),
    ("early8", 12, 0),
    ("late11", 15, 0),
    ("clv",    22, 45),
]

# How long after the owed time we will still attempt the work. Past this the
# slot is abandoned rather than run at a useless hour — locking "midnight
# line" picks at 6pm would corrupt the CLV comparison the whole project
# rests on.
# Widened 2026-08-28 so a RETRY slot can still do the work. The old 2.5h
# window on early8 meant a retry at 13:37 UTC was fine but anything later
# was abandoned — and with GitHub dropping slots unpredictably, that threw
# away work that was still worth doing. These are the limits past which the
# run genuinely stops being what it claims: an "8am pre-move" pull taken
# after noon ET is no longer pre-move, and a midnight-line lock taken in the
# afternoon would corrupt the CLV baseline.
# Core widened to 13h on 2026-08-28. The tight window was costing whole
# days of moneyline and total picks: those markets ONLY lock on the core
# run, so when GitHub dropped that slot (8/27, 8/28) the day produced F5
# picks and nothing else. The original reason for the tight window was
# real — locking a "midnight line" pick at noon would corrupt the CLV
# baseline — so instead of abandoning the work, a late core run now runs
# and TAGS itself, letting the analysis exclude late locks rather than
# losing the picks entirely.
STALE_AFTER = {"core": 13.0, "early8": 4.0, "late11": 6.0, "clv": 4.0}

# Hours past the window opening after which a core lock is no longer taken
# at anything resembling the midnight line, and is marked as such.
CORE_LATE_AFTER = 3.0


def _rows(path):
    try:
        with open(path) as f:
            return [json.loads(l) for l in f if l.strip()]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def slate_date(now_utc: datetime) -> str:
    """The slate this run belongs to, in ET.

    Before ~4am ET the UTC date has already rolled over while the ET slate
    has not, so the core run at 04:05 UTC must claim the PREVIOUS ET day's
    date the same way run.py does."""
    return now_utc.astimezone(ET).strftime("%Y-%m-%d")


def core_done(date: str) -> bool:
    return any(r.get("slate_date") == date
               and (r.get("pull_tag") in (None, "core", "core_late"))
               and r.get("market") in ("Moneyline", "Total", "Run Line")
               for r in _rows(LOCK))


def period_done(date: str, tag: str) -> bool:
    """A period pull counts as done when ANY board wrote rows tagged with it.

    Checking the boards rather than the picks matters: a legitimate period
    run can produce zero locked picks (everything passes the gate) while
    still having done its work."""
    for path in BOARDS:
        for r in _rows(path):
            if r.get("slate_date") == date and r.get("pull_tag") == tag:
                return True
    # Legacy rows (written before pull tagging existed) count as an early
    # pull ONLY for dates before tagging shipped. Applying it to current
    # dates masked a missing pull: the HR writer did not set a tag, so any
    # HR rows made early8 look complete and the 8am slot was skipped.
    if tag == "early8" and date < "2026-08-20":
        for path in BOARDS:
            for r in _rows(path):
                if r.get("slate_date") == date and not r.get("pull_tag"):
                    return True
    return False


def clv_done(date: str) -> bool:
    if any(r.get("slate_date") == date and r.get("clv_final")
           for r in _rows(LOCK)):
        return True
    return any(r.get("slate_date") == date and r.get("clv_final")
               for r in _rows("docs/props_board.jsonl"))


def decide(now_utc: datetime | None = None) -> tuple[str, str]:
    now = now_utc or datetime.now(UTC)
    date = slate_date(now)
    checks = {"core": core_done(date),
              "early8": period_done(date, "early8"),
              "late11": period_done(date, "late11"),
              "clv": clv_done(date)}

    for key, hh, mm in WINDOWS:
        owed_at = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if now < owed_at:
            continue
        if checks[key]:
            continue
        age_h = (now - owed_at).total_seconds() / 3600.0
        if age_h > STALE_AFTER[key]:
            continue          # too late for this slot to be meaningful
        return key, (f"{key} owed since {hh:02d}:{mm:02d} UTC "
                     f"({age_h:.1f}h ago), not yet done for {date}")
    done = ", ".join(k for k, v in checks.items() if v) or "nothing"
    return "skip", f"nothing owed for {date} (done: {done})"


def main():
    job, why = decide()
    print(f"[should_run] {why}")
    print(f"[should_run] slate={slate_date(datetime.now(UTC))} "
          f"utc={datetime.now(UTC).strftime('%H:%M')}")
    env = os.environ.get("GITHUB_ENV")

    if job == "core":
        now = datetime.now(UTC)
        opened = now.replace(hour=4, minute=5, second=0, microsecond=0)
        late = (now - opened).total_seconds() / 3600.0 > CORE_LATE_AFTER
        out = {"MODE": "core",
               "PULL_TAG": "core_late" if late else "core",
               "PERIOD_ONLY": ""}
        label = "Late core pull (off midnight line)" if late else "Midnight pull"
    elif job in ("early8", "late11"):
        out = {"MODE": "period", "PULL_TAG": job, "PERIOD_ONLY": "1"}
        label = ("Early period pull (8am, pre-move)" if job == "early8"
                 else "Late period pull (11am, lineups)")
    elif job == "clv":
        out = {"MODE": "clv", "PULL_TAG": "clv", "PERIOD_ONLY": ""}
        label = "CLV close capture"
    else:
        out = {"MODE": "skip", "PULL_TAG": "", "PERIOD_ONLY": ""}
        label = "skip"

    print(f"[should_run] MODE={out['MODE']} PULL_TAG={out['PULL_TAG']}")
    if env:
        with open(env, "a") as f:
            for k, v in out.items():
                f.write(f"{k}={v}\n")
            f.write(f"RUN_LABEL={label}\n")


if __name__ == "__main__":
    main()
