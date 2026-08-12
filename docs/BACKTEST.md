# Prop model backtest

Replayed on 2026-08-12 for season 2026. Each projection uses ONLY that pitcher's prior starts — no lookahead. This measures whether the model is ACCURATE; it does not measure whether it beats a market, because historical prop prices are not available here.

## Pitcher strikeouts

- starts scored: **711**
- Brier score: **0.2472**  (0.25 = no skill; lower is better)
- mean projection bias: **+0.08 K** (positive = model UNDER-projects)

| Model P(over) | n | Predicted | Actual |
|---|---|---|---|
| 20%–35% | 6 | 35% | 33% |
| 35%–50% | 705 | 43% | 46% |

> Largest band gap: **3%**. Bands that sit consistently above or below the diagonal mean the projection is biased, and every edge computed from it inherits that bias.
