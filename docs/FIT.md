# Fitted model parameters

Fitted 2026-08-17 against real distributions from MLB StatsAPI. Every value below was previously chosen by judgement. The NRFI dispersion showed why that matters: the guess was 1.45, the fitted value 3.36, and the error made the board call YRFI on 79% of games and go 34-53.

| Parameter | Guessed | Fitted | Sample | Verdict |
|---|---|---|---|---|
| `FI_DISPERSION` | 3.36 | **2.169** | 764 games | 0.65x — **materially wrong** (mean 0.99, P(0)=51.8%) |
| `K_DISPERSION` | 1.3 | **1.112** | 2435 starts | 0.86x — close (mean 5.34) |
| `RBI_DISPERSION` | 1.5 | **1.585** | 13615 games | 1.06x — close (mean 0.55) |
| `HRR_DISPERSION` | 1.35 | **2.044** | 13861 games | 1.51x — **materially wrong** (mean 2.04) |
| `SHRINK_avg` | 200.0 | **800.000** | 200 players | 4.00x — **materially wrong** (split-half) |
| `SHRINK_k_pa` | 150.0 | **30.000** | 200 players | 0.20x — **materially wrong** (split-half) |

## What to do with this

Values marked **materially wrong** are off by more than 1.5x and are distorting every probability derived from them — in the direction of manufactured edge if the fitted dispersion is HIGHER than the guess (the model is overstating its confidence in outer outcomes), or of missed opportunity if LOWER.

The model reads `docs/fitted_params.json` at runtime and uses these values in place of the hard-coded constants. Re-run this script periodically — these are seasonal quantities, not universal ones.
