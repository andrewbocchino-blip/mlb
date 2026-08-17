# Prop model backtest

Replayed on 2026-08-17 for season 2026. Each projection uses ONLY that pitcher's prior starts — no lookahead. This measures whether the model is ACCURATE; it does not measure whether it beats a market, because historical prop prices are not available here.

## Pitcher strikeouts

- starts scored: **3735**
- Brier score: **0.2307**  (0.25 = no skill; lower is better)
- mean projection bias: **+0.08 K** (positive = model UNDER-projects)

> **How to read the Brier score.** 0.25 is a coin flip, but the number that matters is the comparison to a model that ignores the pitcher entirely. In simulation, a constant-guess model scores about **0.247** against these same lines, a weak model about **0.234**, and a model with real knowledge about **0.221**. A score at or above ~0.245 means the projection is carrying essentially no information about this particular start.

| Model P(over) | n | Predicted | Actual |
|---|---|---|---|
| 20%–35% | 770 | 31% | 30% |
| 35%–50% | 1362 | 42% | 45% |
| 50%–65% | 1264 | 57% | 63% |
| 65%–80% | 339 | 69% | 71% |

> Largest band gap: **6%**. Bands that sit consistently above or below the diagonal mean the projection is biased, and every edge computed from it inherits that bias.

### Discrimination

- when the model says **60%+**: hit **70.3%** (737 calls)
- when the model says **40%-**: hit **34.1%** (1217 calls)
- separation: **+36.2%**

> Separation is the number that matters for betting. A model can be perfectly calibrated and still useless if it never leaves 50%. Wide, correctly-ordered separation is what an edge looks like; near-zero separation means the projection carries no usable information.

### Skill by line position

| Line vs projection | n | Brier | Actual over-rate |
|---|---|---|---|
| 0.75x | 747 | 0.2125 | 70.5% |
| 0.85x | 747 | 0.2383 | 60.8% |
| 0.95x | 747 | 0.2496 | 49.7% |
| 1.05x | 747 | 0.2410 | 40.7% |
| 1.15x | 747 | 0.2121 | 31.2% |

> A model with real skill should beat 0.25 at every rung, and most clearly at the outer ones where the answer is least obvious.
