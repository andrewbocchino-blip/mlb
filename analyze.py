#!/usr/bin/env python3
"""analyze.py — where should the gates actually be?

Every threshold in this project was set by judgement: PLAY at 7.0, LEAN at
5.0, the 6% no-vig prop gate, the tier gates. None of them were derived from
results. This sweeps each threshold across the real graded record and reports
what would have happened at every level, so the gates can be set by evidence
instead of by my guesses.

Method borrowed from gmalbert/baseball-predictions' `edge_filter_analysis`,
which does the same sweep for its own models. Adapted here to run over the
locked-picks ledger and the prop/NRFI/HR boards, and extended with
calibration and a bootstrap significance check — because a sweep over a small
sample WILL find a threshold that looks great by luck, and reporting the peak
without saying how likely it is to be noise would be the exact
selection-bias trap the sweep is supposed to protect against.

Writes docs/ANALYSIS.md. Read-only: touches no picks, no grades.

Run:  python analyze.py
"""

from __future__ import annotations

import json
import math
import os
import random

LOCK = "docs/locked_picks.jsonl"
PROPS = "docs/props_board.jsonl"
NRFI = "docs/nrfi_board.jsonl"
HR = "docs/hr_board.jsonl"


def load(path):
    try:
        with open(path) as f:
            return [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        return []


def american_payout(odds, win):
    if odds is None:
        return 0.91 if win else -1.0
    if win:
        return (odds / 100.0) if odds > 0 else (100.0 / abs(odds))
    return -1.0


def locked_odds(row):
    books = row.get("books") or {}
    bb = row.get("best_book")
    px = books.get(bb) if bb else None
    if px is None and books:
        px = max(books.values())
    return px


# --------------------------------------------------------------------------
# significance: is this threshold's edge distinguishable from luck?
# --------------------------------------------------------------------------

def bootstrap_roi_ci(pls, n=2000, seed=7):
    """Percentile CI for mean P/L. If it straddles zero, the 'edge' is noise."""
    if len(pls) < 5:
        return None
    rng = random.Random(seed)
    means = []
    for _ in range(n):
        s = [pls[rng.randrange(len(pls))] for _ in range(len(pls))]
        means.append(sum(s) / len(s))
    means.sort()
    return means[int(0.025 * n)], means[int(0.975 * n)]


def sweep(rows, key, thresholds, label, out, roi_from="pl"):
    """Performance at each minimum threshold of `key`."""
    graded = [r for r in rows if r.get("result") in ("WIN", "LOSS", "HIT", "MISS")]
    if not graded:
        out.append(f"_No graded rows for {label} yet._")
        out.append("")
        return
    out.append(f"### {label}")
    out.append("")
    out.append("| Min | n | W | L | Win% | Units | ROI | 95% CI on ROI | Verdict |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    best = None
    for t in thresholds:
        sel = [r for r in graded if (r.get(key) is not None and r[key] >= t)]
        if len(sel) < 5:
            continue
        w = sum(1 for r in sel if r["result"] in ("WIN", "HIT"))
        l = len(sel) - w
        if roi_from == "pl":
            pls = [r.get("pl") if r.get("pl") is not None
                   else american_payout(locked_odds(r), r["result"] in ("WIN", "HIT"))
                   for r in sel]
        else:
            pls = [american_payout(r.get("price"), r["result"] in ("WIN", "HIT"))
                   for r in sel]
        units = sum(pls)
        roi = units / len(sel)
        ci = bootstrap_roi_ci(pls)
        if ci:
            ci_s = f"{ci[0]:+.1%} to {ci[1]:+.1%}"
            verdict = "signal" if ci[0] > 0 else ("negative" if ci[1] < 0 else "indistinguishable from luck")
        else:
            ci_s, verdict = "—", "sample too small"
        out.append(f"| {t} | {len(sel)} | {w} | {l} | {w/len(sel):.1%} | "
                   f"{units:+.2f} | {roi:+.1%} | {ci_s} | {verdict} |")
        if best is None or roi > best[1]:
            best = (t, roi, len(sel), verdict)
    if best:
        out.append("")
        out.append(f"> Peak ROI at min {key} = **{best[0]}** ({best[1]:+.1%} over {best[2]} bets, "
                   f"{best[3]}). **Do not simply adopt the peak** — sweeping many thresholds over "
                   f"a small sample is guaranteed to surface one that looks good. A threshold is "
                   f"only worth adopting if its confidence interval clears zero AND the levels "
                   f"around it behave similarly.")
    out.append("")


def calibration(rows, prob_key, label, out):
    """Predicted vs actual by probability band — is the number honest?"""
    graded = [r for r in rows
              if r.get("result") in ("WIN", "LOSS", "HIT", "MISS")
              and r.get(prob_key) is not None]
    if len(graded) < 10:
        out.append(f"_Not enough graded rows to calibrate {label}._")
        out.append("")
        return
    bands = [(0, .4), (.4, .5), (.5, .6), (.6, .7), (.7, .8), (.8, 1.01)]
    out.append(f"### {label} calibration")
    out.append("")
    out.append("| Model says | n | Predicted | Actual | Gap |")
    out.append("|---|---|---|---|---|")
    brier = 0.0
    for lo, hi in bands:
        sel = [r for r in graded if lo <= r[prob_key] < hi]
        if not sel:
            continue
        pred = sum(r[prob_key] for r in sel) / len(sel)
        act = sum(1 for r in sel if r["result"] in ("WIN", "HIT")) / len(sel)
        out.append(f"| {lo:.0%}–{hi:.0%} | {len(sel)} | {pred:.0%} | {act:.0%} | {act-pred:+.0%} |")
    for r in graded:
        o = 1.0 if r["result"] in ("WIN", "HIT") else 0.0
        brier += (r[prob_key] - o) ** 2
    out.append("")
    out.append(f"Brier score: **{brier/len(graded):.4f}** over {len(graded)} calls "
               f"(0.25 = no skill).")
    out.append("")


def main():
    out = ["# Threshold and calibration analysis", "",
           "Every gate in this project was set by judgement, not evidence. This sweeps "
           "each one across the real graded record and reports what actually happened at "
           "every level, with a bootstrap confidence interval so a threshold that merely "
           "got lucky can be told apart from one that works.", "",
           "_Read-only: this script never alters picks, grades, or boards._", ""]

    picks = load(LOCK)
    latest = {}
    for r in picks:
        k = (r.get("model", "A"), r["slate_date"], r["game"], r["market"], r["pick"])
        if k not in latest or r.get("pulled_at", "") >= latest[k].get("pulled_at", ""):
            latest[k] = r
    picks = [r for r in latest.values() if r.get("model", "A") == "A"]

    out.append("## Locked picks — model score threshold")
    out.append("")
    sweep(picks, "score", [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5],
          "All markets by score", out)
    for mkt in sorted({r["market"] for r in picks}):
        sub = [r for r in picks if r["market"] == mkt]
        if len([r for r in sub if r.get("result") in ("WIN", "LOSS")]) >= 10:
            sweep(sub, "score", [5.0, 6.0, 7.0, 8.0, 9.0, 9.5], f"{mkt} by score", out)

    out.append("## Locked picks — CLV threshold")
    out.append("")
    sweep([r for r in picks if r.get("clv") is not None], "clv",
          [-5, -2, 0, 1, 2, 3, 5], "Picks by CLV at lock", out)

    props = load(PROPS)
    out.append("## Prop board")
    out.append("")
    sweep(props, "edge", [0.02, 0.04, 0.06, 0.08, 0.10, 0.15],
          "Props by no-vig edge", out, roi_from="price")
    sweep(props, "ev", [0.0, 0.03, 0.05, 0.07, 0.10, 0.15],
          "Props by expected value", out, roi_from="price")
    calibration(props, "model_p", "Prop model", out)
    for tier in ("A", "B", "C"):
        sub = [r for r in props if r.get("tier") == tier]
        if len([r for r in sub if r.get("result") in ("HIT", "MISS")]) >= 10:
            calibration(sub, "model_p", f"Prop tier {tier}", out)

    nrfi = load(NRFI)
    out.append("## NRFI/YRFI forced-call board")
    out.append("")
    calibration(nrfi, "model_p", "NRFI model", out)

    hrb = load(HR)
    out.append("## HR board")
    out.append("")
    calibration(hrb, "p_hr", "HR model", out)

    os.makedirs("docs", exist_ok=True)
    with open("docs/ANALYSIS.md", "w") as f:
        f.write("\n".join(out))
    print("Wrote docs/ANALYSIS.md")


if __name__ == "__main__":
    main()
