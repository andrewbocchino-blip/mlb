# Results

## Model standing — read this first

Fitting the optimal blend between this model's projections and the no-vig market price, over the real graded record, returns a weight on the **market** of:

| Board | n | Model Brier | Market Brier | Optimal weight on market |
|---|---|---|---|---|
| NRFI forced calls | 200 | 0.2686 | **0.2459** | **1.00** |
| Props — tier A | 279 | 0.2568 | **0.2489** | 0.80 |
| Props — tier B | 2,224 | 0.2507 | **0.2436** | **1.00** |
| Props — tier C | 4,450 | 0.2281 | **0.2231** | **1.00** |

**Predictions are most accurate when this model's number is discarded and the market price is used instead.** The projections are not merely uninformative — including them makes forecasts measurably worse. Tier A props retain a 0.20 weight, and even there the blended Brier (0.2485) beats the pure market (0.2489) by an amount inside the noise.

Consequences now built into the model: qualification gates run on the market-shrunk probability, so a row must show edge AFTER its projection is pulled toward the price; NRFI confidence tiers were retired as a signal after measuring as anti-predictive (High tier 45.0% actual vs 63.7% claimed, Coin flip 58.8% vs 53.0%); and the HR board carries a fitted calibration scale after projecting 24.5% and delivering 14.7% over 150 graded rows.

**Gate mode: MODEL.** Recommendations are generated from the model's own edge and EV, not the market-shrunk figures above. Every row records both, so this period can be graded either way after the fact — if the model-gated picks win, the Brier result above was the wrong read and the record will say so plainly.

Track two numbers as this accumulates: whether gate-clearing picks beat their own stated probability, and whether they beat the closing price. The first says the model is calibrated; the second says it has edge. Neither has been shown yet.

---

## Scoreboard

| Board | Record | Hit rate | Model predicted | Standing |
|---|---|---|---|---|
| **Locked bets** (ML/Total) | 375-321 | **53.9%** | — | -7.86u · CLV -3.07% |
| NRFI/YRFI forced calls | 146-143 | **50.5%** | 59.4% | 🔴 behind its own number · ⚠️ below 53% naive baseline |
| HR board (top 10 daily) | 34-169 | **16.7%** | 23.7% | 🔴 behind its own number |
| Player props (all tiers) | 4964-5505 | **47.4%** | 52.9% | 🔴 behind its own number · CLV +0.35% |
| &nbsp;&nbsp;↳ props · tier A (HR, pitcher K) | 223-197 | **53.1%** | 57.6% | 🔴 behind its own number |
| &nbsp;&nbsp;↳ props · tier B (hits, batter K) | 1706-1633 | **51.1%** | 57.6% | 🔴 behind its own number |
| &nbsp;&nbsp;↳ props · tier C (RBI, H+R+RBI) | 3022-3658 | **45.2%** | 50.2% | 🔴 behind its own number |

**Hit rate vs predicted is the whole test.** A board that hits at the rate it claims is trustworthy even when it loses; a board that hits below its own number is telling you it does not know what it claims to know.

---

**Model A** = current model (control). **Model B** = retired variant, history preserved. CLV measured from the real price vs close. Each unique bet counted once. Paper only — no real money.

**Model A: 375-321  ·  54% win  ·  -7.86u  ·  -1.1% ROI  ·  avg CLV -3.07%**
**Model B: 237-191  ·  55% win  ·  +14.16u  ·  +3.3% ROI  ·  avg CLV n/a (no closing lines yet)**

## Board calibration standings

These boards are calibration records, not bets. The question is not whether they won — it is whether a call at a stated confidence lands at that rate. A tier that hits BELOW its stated probability is a model telling you it does not know what it claims to know.

### NRFI/YRFI forced calls

| Confidence | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|
| High | 153 | 73 | 80 | 48% | 64% | -16% |
| Medium | 53 | 28 | 25 | 53% | 56% | -3% |
| Low | 29 | 14 | 15 | 48% | 54% | -5% |
| Coin flip | 54 | 31 | 23 | 57% | 53% | +4% |
| **All** | **289** | **146** | **143** | **51%** | **59%** | **-9%** |

YRFI share of calls: **190/289 (66%)** — hitting 48%.

**Naive baseline check.** First innings were scoreless in **53.3%** of these games, so always calling NRFI scores **53.3%**. The model scores **50.5%**.

> ⚠️ **The model is losing to a coin that always says the same thing.** Until it beats this line, its calls carry no information and should not be treated as analysis — a forced call is only worth making if it beats the majority class.

> ⚠️ **Confidence is inverted**: the High tier is hitting BELOW the Coin flip tier. Whatever the confidence metric is measuring, it is not the probability of being right. Calls at this tier should carry no weight until this reverses.

### HR board (top-10 daily)

- listed and graded: **203**
- homered: **34** · model expected **48.0**
- actual rate **16.7%** vs predicted **23.7%** (**-6.9%**)

### Prop divergence board

| Tier | Market | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|---|
| A | Ks (P) | 420 | 223 | 197 | 53% | 58% | -4% |
| B | Hits | 3339 | 1706 | 1633 | 51% | 58% | -7% |
| C | H+R+RBI | 3340 | 1686 | 1654 | 50% | 56% | -6% |
| C | RBI | 3340 | 1336 | 2004 | 40% | 44% | -4% |
| **All** | | **10469** | **4964** | **5505** | **47%** | **53%** | **-6%** |

Gate-clearing calls only: **40-32** (56% vs 60% predicted).

> **Sample-size reality check.** Distinguishing a real edge from noise needs hundreds of graded calls per tier. Gaps below are indicative, not verdicts — except where a tier is inverted against a lower tier, which is a structural signal rather than variance.

## Gate comparison — model vs market-shrunk

| Gate | Rows cleared | Record |
|---|---|---|
| **Model edge** (live) | 72 | 40-32 (55.6%) vs 60% predicted |
| Market-shrunk | 0 | — |

> **135 totals excluded** from every table below: they were locked against a probable ALTERNATE line before the main-line fix of 2026-08-25, so both the pick and its grade were made against a number the book never offered. They are kept in the ledger and flagged, not deleted.

## Weak-link analysis

Every slice of the graded record with a bootstrap confidence interval. A segment only counts as a demonstrated loser when its whole interval sits below zero — otherwise it is a segment having a bad run, and cutting it would be fitting to noise.

### By grade

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| LEAN | 123-132 | -23.93u | -9.4% | -21.7% to +2.4% | ⚪ inconclusive |
| PLAY | 215-162 | +8.87u | +2.4% | -6.5% to +11.1% | ⚪ inconclusive |

### By market

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| F5 Total | 18-23 | -9.47u | -23.1% | -49.7% to +7.0% | ⚪ inconclusive |
| Total | 51-62 | -12.75u | -11.3% | -29.8% to +7.4% | ⚪ inconclusive |
| Run Line | 42-48 | -2.11u | -2.3% | -24.3% to +20.2% | ⚪ inconclusive |
| Moneyline | 221-156 | +9.13u | +2.4% | -6.1% to +11.2% | ⚪ inconclusive |

### By price band

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| dog +120 or longer | 19-34 | -5.19u | -9.8% | -40.8% to +21.8% | ⚪ inconclusive |
| fav -121 to -160 | 86-76 | -14.29u | -8.8% | -21.7% to +4.0% | ⚪ inconclusive |
| heavy fav past -160 | 74-42 | -3.32u | -2.9% | -15.9% to +10.5% | ⚪ inconclusive |
| pickem -120 to -100 | 103-97 | -4.01u | -2.0% | -14.7% to +11.3% | ⚪ inconclusive |
| dog +100 to +119 | 37-33 | +6.46u | +9.2% | -14.6% to +33.0% | ⚪ inconclusive |

### By model score — does the score rank bets correctly?

| Score band | n | Record | Units | ROI |
|---|---|---|---|---|
| 5.0–5.9 | 147 | 71-76 | -14.59u | -9.9% |
| 6.0–6.9 | 108 | 52-56 | -9.34u | -8.6% |
| 7.0–7.9 | 107 | 57-50 | +1.42u | +1.3% |
| 8.0–8.9 | 80 | 49-31 | +8.09u | +10.1% |
| 9.0–10.9 | 190 | 109-81 | -0.64u | -0.3% |

> Rank correlation between score band and ROI: **+0.70** (+1.00 = ROI rises perfectly with score).

> Below score 7.0: **-23.93u over 255 bets (-9.4%)**. At 7.0 and above: **+8.87u over 377 bets (+2.4%)**. The sign flips at exactly the PLAY threshold.

> ⚠️ ROI does not trend with score. The score is not reliably ranking bets, and any threshold drawn from this table would be fitted to noise.

> 4 picks were locked on a LATE core run (the midnight slot was dropped and the work was done hours later). They count in the W-L record but are excluded from CLV below, because a pick taken at noon cannot be compared to a closing line the same way one taken at midnight can.

### Closing line value — the deeper test

Across **64** picks with a captured close, average CLV is **-3.21%** and **17/64 (27%)** beat the closing price.

> ⚠️ **Negative CLV outweighs a winning record.** The market is moving against these picks after they lock, which is what luck looks like from the inside — a model with real edge gets better prices than the close, not worse. Until this turns positive, treat any winning stretch as variance.

> One measurement caveat before over-reading it: picks lock at the BEST price across two books, and the close is captured from that same book. Some of the gap is simply the best-of-two price regressing, not the market disagreeing. The honest read is directional, not exact.

## Early vs late pull

| Pull | Rows | Avg CLV | Beat close |
|---|---|---|---|
| 8am (pre-move) | 2187 | **+0.47%** | 1106/2187 |

## Daily ledger — every call, every result

Last 4 graded slates in full. Most recent first.

### 2026-08-30 — bets 2-3 (-1.49u) · props 290-320 · NRFI 10-3 · HR 3-6

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Milwaukee Brewers ML | — | -154 | 9.5 | — | ❌ -1.00u |
| Moneyline | Chicago Cubs ML | — | -142 | 8.7 | — | ❌ -1.00u |
| Moneyline | Pittsburgh Pirates ML | — | -113 | 8.1 | — | ✅ +0.88u |
| Moneyline | Tampa Bay Rays ML | — | -158 | 7.2 | — | ✅ +0.63u |
| F5 Total | F5 Over 3.5 | 3.5 | -148 | 7.2 | — | ❌ -1.00u |

**Recommended props** (0 of 610 priced cleared the gate)

*None cleared the gate — the model found no prop worth recommending on this slate.*

**Parlay-leg candidates** (30 priced beyond the -250 straight-bet floor)

| Player | Mkt | Call | Line | Price | Model | Actual | Result |
|---|---|---|---|---|---|---|---|
| Carlos Narvaez | RBI | Under | 0.5 | -277 | 82% | 0 | ✅ |
| Christian Encarnacion-Strand | Hits | Under | 1.5 | -266 | 79% | 0 | ✅ |
| Dane Myers | RBI | Under | 0.5 | -331 | 83% | 1 | ❌ |
| Gunnar Henderson | Hits | Under | 1.5 | -255 | 75% | 4 | ❌ |
| Michael Conforto | RBI | Under | 0.5 | -310 | 78% | 1 | ❌ |
| Jackson Chourio | Hits | Over | 0.5 | -251 | 74% | 1 | ✅ |
| Chase DeLauter | Hits | Over | 0.5 | -269 | 74% | 4 | ✅ |
| Jackson Holliday | RBI | Under | 0.5 | -256 | 73% | 0 | ✅ |

*Legs: **23-7**. A 30-leg parlay of these would NOT have cashed — every leg must land.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Boston Red Sox @ New York Yankees | **NRFI** | High | 60% | 50% | ✅ |
| Seattle Mariners @ Toronto Blue Jays | **YRFI** | High | 69% | 50% | ✅ |
| Los Angeles Dodgers @ Detroit Tigers | **YRFI** | High | 54% | 43% | ❌ |
| Chicago White Sox @ Minnesota Twins | **YRFI** | High | 73% | 50% | ✅ |
| Texas Rangers @ Milwaukee Brewers | **YRFI** | High | 71% | 50% | ✅ |
| Pittsburgh Pirates @ St. Louis Cardinals | **YRFI** | High | 62% | 44% | ❌ |
| Philadelphia Phillies @ Los Angeles Angels | **YRFI** | High | 66% | 50% | ✅ |
| Colorado Rockies @ Atlanta Braves | **NRFI** | Medium | 54% | 50% | ✅ |
| Kansas City Royals @ Cleveland Guardians | **YRFI** | Medium | 53% | 48% | ✅ |
| San Diego Padres @ Tampa Bay Rays | **NRFI** | Medium | 60% | 53% | ✅ |
| Houston Astros @ New York Mets | **NRFI** | Medium | 53% | 47% | ❌ |
| Cincinnati Reds @ Chicago Cubs | **YRFI** | Medium | 60% | 54% | ✅ |
| Baltimore Orioles @ Athletics | **YRFI** | Coin flip | 55% | 54% | ✅ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Matt Olson | Colorado Rockies @ Atlanta Braves | 24% | ❌ |
| 2 | Hunter Goodman | Colorado Rockies @ Atlanta Braves | 23% | ❌ |
| 3 | Munetaka Murakami | Chicago White Sox @ Minnesota Twins | 22% | ❌ |
| 4 | Pete Alonso | Baltimore Orioles @ Athletics | 22% | ❌ |
| 5 | Kyle Schwarber | Philadelphia Phillies @ Los Angeles Angels | 21% | ❌ |
| 6 | Willson Contreras | Boston Red Sox @ New York Yankees | 21% | ❌ |
| 7 | Juan Soto | Houston Astros @ New York Mets | 20% | ✅ |
| 8 | Coby Mayo | Baltimore Orioles @ Athletics | 20% | ✅ |
| 10 | Sal Stewart | Cincinnati Reds @ Chicago Cubs | 19% | ✅ |

*3 homered · model expected 1.9*

---

### 2026-08-29 — bets 5-0 (+3.36u) · props 283-325 · NRFI 7-10 · HR 0-9

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Chicago Cubs ML | — | -196 | 9.5 | — | ✅ +0.51u |
| Moneyline | Milwaukee Brewers ML | — | -164 | 9.5 | — | ✅ +0.61u |
| Total | Over 5.5 | 5.5 | -104 | 9.5 | — | ✅ +0.96u |
| Moneyline | Toronto Blue Jays ML | — | -126 | 8.8 | — | ✅ +0.79u |
| Moneyline | Atlanta Braves ML | — | -205 | 8.4 | — | ✅ +0.49u |

**Recommended props** (0 of 608 priced cleared the gate)

*None cleared the gate — the model found no prop worth recommending on this slate.*

**Parlay-leg candidates** (40 priced beyond the -250 straight-bet floor)

| Player | Mkt | Call | Line | Price | Model | Actual | Result |
|---|---|---|---|---|---|---|---|
| Christian Encarnacion-Strand | Hits | Under | 1.5 | -267 | 82% | 1 | ✅ |
| Nick Gonzales | Hits | Over | 0.5 | -264 | 80% | 2 | ✅ |
| Mauricio Dubon | Hits | Over | 0.5 | -266 | 79% | 1 | ✅ |
| Daulton Varsho | RBI | Under | 0.5 | -282 | 78% | 0 | ✅ |
| Yandy Diaz | Hits | Over | 0.5 | -269 | 77% | 2 | ✅ |
| Otto Lopez | Hits | Over | 0.5 | -252 | 75% | 1 | ✅ |
| Yordan Alvarez | Hits | Over | 0.5 | -258 | 75% | 2 | ✅ |
| Mike Yastrzemski | RBI | Under | 0.5 | -282 | 77% | 0 | ✅ |

*Legs: **29-11**. A 40-leg parlay of these would NOT have cashed — every leg must land.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Chicago White Sox @ Minnesota Twins | **YRFI** | High | 74% | 53% | ✅ |
| Seattle Mariners @ Toronto Blue Jays | **YRFI** | High | 59% | 43% | ❌ |
| Arizona Diamondbacks @ San Francisco Giants | **YRFI** | High | 57% | 48% | ✅ |
| Miami Marlins @ Washington Nationals | **NRFI** | High | 66% | 58% | ✅ |
| Kansas City Royals @ Cleveland Guardians | **YRFI** | High | 60% | 46% | ❌ |
| Philadelphia Phillies @ Los Angeles Angels | **YRFI** | High | 63% | 50% | ❌ |
| Boston Red Sox @ New York Yankees | **NRFI** | Medium | 62% | 56% | ✅ |
| Cincinnati Reds @ Chicago Cubs | **NRFI** | Medium | 54% | 47% | ❌ |
| Houston Astros @ New York Mets | **YRFI** | Medium | 57% | 50% | ✅ |
| San Diego Padres @ Tampa Bay Rays | **NRFI** | Medium | 55% | 50% | ❌ |
| Colorado Rockies @ Atlanta Braves | **YRFI** | Medium | 60% | 53% | ❌ |
| Baltimore Orioles @ Athletics | **YRFI** | Medium | 57% | 52% | ❌ |
| Pittsburgh Pirates @ St. Louis Cardinals | **NRFI** | Low | 54% | 51% | ❌ |
| Boston Red Sox @ New York Yankees | **NRFI** | Coin flip | 51% | 56% | ✅ |
| Los Angeles Dodgers @ Detroit Tigers | **NRFI** | Coin flip | 54% | 53% | ✅ |
| Arizona Diamondbacks @ San Francisco Giants | **NRFI** | Coin flip | 51% | 52% | ❌ |
| Texas Rangers @ Milwaukee Brewers | **NRFI** | Coin flip | 51% | 50% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Kyle Schwarber | Philadelphia Phillies @ Los Angeles Angels | 24% | ❌ |
| 2 | Matt Olson | Colorado Rockies @ Atlanta Braves | 24% | ❌ |
| 3 | Ben Rice | Boston Red Sox @ New York Yankees | 22% | ❌ |
| 4 | Pete Alonso | Baltimore Orioles @ Athletics | 22% | ❌ |
| 5 | Munetaka Murakami | Chicago White Sox @ Minnesota Twins | 21% | ❌ |
| 6 | Luis García Jr. | Boston Red Sox @ New York Yankees | 21% | ❌ |
| 8 | Kazuma Okamoto | Seattle Mariners @ Toronto Blue Jays | 20% | ❌ |
| 9 | Hunter Goodman | Colorado Rockies @ Atlanta Braves | 20% | ❌ |
| 10 | Coby Mayo | Baltimore Orioles @ Athletics | 20% | ❌ |

*0 homered · model expected 1.9*

### 2026-08-28 — bets 2-1 (+0.49u) · props 315-353 · NRFI 9-6 · HR 1-7

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| F5 Total | F5 Over 4.5 | 4.5 | -128 | 9.5 | — | ✅ +0.78u |
| F5 Total | F5 Over 4.5 | 4.5 | -140 | 9.5 | — | ✅ +0.71u |
| F5 Total | F5 Over 4.5 | 4.5 | +100 | 7.7 | — | ❌ -1.00u |

**Recommended props** (0 of 668 priced cleared the gate)

*None cleared the gate — the model found no prop worth recommending on this slate.*

**Parlay-leg candidates** (41 priced beyond the -250 straight-bet floor)

| Player | Mkt | Call | Line | Price | Model | Actual | Result |
|---|---|---|---|---|---|---|---|
| Esteury Ruiz | RBI | Under | 0.5 | -341 | 86% | 0 | ✅ |
| Carlos Narvaez | RBI | Under | 0.5 | -327 | 83% | 0 | ✅ |
| Mike Yastrzemski | RBI | Under | 0.5 | -281 | 77% | 0 | ✅ |
| Joc Pederson | RBI | Under | 0.5 | -286 | 77% | 0 | ✅ |
| Jesus Sanchez | RBI | Under | 0.5 | -271 | 76% | 0 | ✅ |
| Jose Siri | RBI | Under | 0.5 | -349 | 81% | 0 | ✅ |
| Daulton Varsho | RBI | Under | 0.5 | -300 | 78% | 2 | ❌ |
| Trea Turner | RBI | Under | 0.5 | -267 | 75% | 0 | ✅ |

*Legs: **31-10**. A 41-leg parlay of these would NOT have cashed — every leg must land.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| San Diego Padres @ Tampa Bay Rays | **NRFI** | High | 61% | 50% | ✅ |
| Seattle Mariners @ Toronto Blue Jays | **YRFI** | High | 55% | 40% | ✅ |
| Chicago White Sox @ Minnesota Twins | **YRFI** | High | 68% | 53% | ✅ |
| Pittsburgh Pirates @ St. Louis Cardinals | **YRFI** | High | 60% | 46% | ❌ |
| Philadelphia Phillies @ Los Angeles Angels | **YRFI** | High | 61% | 49% | ✅ |
| Cincinnati Reds @ Chicago Cubs | **NRFI** | Medium | 54% | 48% | ❌ |
| Miami Marlins @ Washington Nationals | **NRFI** | Medium | 57% | 52% | ✅ |
| Arizona Diamondbacks @ San Francisco Giants | **YRFI** | Medium | 58% | 50% | ✅ |
| Baltimore Orioles @ Athletics | **YRFI** | Low | 52% | 48% | ❌ |
| Los Angeles Dodgers @ Detroit Tigers | **NRFI** | Coin flip | 53% | 57% | ✅ |
| Kansas City Royals @ Cleveland Guardians | **YRFI** | Coin flip | 52% | 50% | ❌ |
| Houston Astros @ New York Mets | **NRFI** | Coin flip | 54% | 53% | ✅ |
| Colorado Rockies @ Atlanta Braves | **YRFI** | Coin flip | 53% | 55% | ❌ |
| Boston Red Sox @ New York Yankees | **NRFI** | Coin flip | 57% | 57% | ✅ |
| Texas Rangers @ Milwaukee Brewers | **NRFI** | Coin flip | 51% | 51% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Hunter Goodman | Colorado Rockies @ Atlanta Braves | 24% | ❌ |
| 2 | Matt Olson | Colorado Rockies @ Atlanta Braves | 24% | ❌ |
| 3 | Munetaka Murakami | Chicago White Sox @ Minnesota Twins | 22% | ❌ |
| 4 | Ben Rice | Boston Red Sox @ New York Yankees | 22% | ❌ |
| 7 | Mickey Moniak | Colorado Rockies @ Atlanta Braves | 19% | ❌ |
| 8 | Kyle Schwarber | Philadelphia Phillies @ Los Angeles Angels | 19% | ❌ |
| 9 | Joc Pederson | Texas Rangers @ Milwaukee Brewers | 19% | ❌ |
| 10 | Colson Montgomery | Chicago White Sox @ Minnesota Twins | 18% | ✅ |

*1 homered · model expected 1.7*

### 2026-08-27 — bets 0-1 (-1.00u) · props 124-173 · NRFI 2-5 · HR 3-5

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| F5 Total | F5 Over 5.5 | 5.5 | -114 | 9.5 | — | ❌ -1.00u |

**Recommended props** (0 of 297 priced cleared the gate)

*None cleared the gate — the model found no prop worth recommending on this slate.*

**Parlay-leg candidates** (21 priced beyond the -250 straight-bet floor)

| Player | Mkt | Call | Line | Price | Model | Actual | Result |
|---|---|---|---|---|---|---|---|
| Tyler Tolbert | RBI | Under | 0.5 | -398 | 88% | 0 | ✅ |
| Austin Wells | RBI | Under | 0.5 | -324 | 81% | 0 | ✅ |
| Jung Hoo Lee | Hits | Over | 0.5 | -273 | 78% | 0 | ❌ |
| Daulton Varsho | RBI | Under | 0.5 | -297 | 78% | 0 | ✅ |
| William Contreras | Hits | Over | 0.5 | -266 | 75% | 0 | ❌ |
| Pete Alonso | Hits | Over | 0.5 | -258 | 74% | 0 | ❌ |
| Geraldo Perdomo | RBI | Under | 0.5 | -268 | 74% | 0 | ✅ |
| Bobby Witt Jr. | Hits | Under | 1.5 | -253 | 72% | 2 | ❌ |

*Legs: **12-9**. A 21-leg parlay of these would NOT have cashed — every leg must land.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Colorado Rockies @ Washington Nationals | **NRFI** | High | 62% | 45% | ❌ |
| Milwaukee Brewers @ New York Mets | **YRFI** | High | 50% | 41% | ✅ |
| Baltimore Orioles @ St. Louis Cardinals | **YRFI** | Medium | 53% | 47% | ❌ |
| Houston Astros @ New York Yankees | **NRFI** | Medium | 55% | 50% | ✅ |
| Arizona Diamondbacks @ San Francisco Giants | **NRFI** | Low | 54% | 51% | ❌ |
| Kansas City Royals @ Toronto Blue Jays | **NRFI** | Coin flip | 54% | 52% | ❌ |
| Los Angeles Dodgers @ Atlanta Braves | **NRFI** | Coin flip | 59% | 60% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Hunter Goodman | Colorado Rockies @ Washington Nationals | 26% | ❌ |
| 2 | Yordan Alvarez | Houston Astros @ New York Yankees | 22% | ❌ |
| 4 | Ben Rice | Houston Astros @ New York Yankees | 18% | ❌ |
| 5 | Luis García Jr. | Houston Astros @ New York Yankees | 18% | ❌ |
| 6 | Matt Olson | Los Angeles Dodgers @ Atlanta Braves | 17% | ❌ |
| 8 | Christian Walker | Houston Astros @ New York Yankees | 16% | ✅ |
| 9 | Jac Caglianone | Kansas City Royals @ Toronto Blue Jays | 16% | ✅ |
| 10 | Jeremy Peña | Houston Astros @ New York Yankees | 16% | ✅ |

*3 homered · model expected 1.5*

> **CLV caveat.** Beating the close is evidence of skill only when the move came from the market re-evaluating information we also had. If a scratch or injury broke after we locked, we collect the CLV without having known anything — that is luck wearing the costume of skill. Read CLV in aggregate, never on a single bet.

> CLV is the signal that matters here, not W-L — per the sharp-bettor method, beating the closing line is what indicates a real edge. A small sample of wins with negative CLV is luck, not edge.

### Moneyline probability calibration (Model A, n=377)

Brier score: **0.2433** (0.25 = coin flip knowledge; lower is better)

| Model home-win band | n | Predicted avg | Actual home-win % |
|---|---|---|---|
| 0%–40% | 51 | 36% | 35% |
| 40%–45% | 60 | 43% | 47% |
| 45%–50% | 62 | 47% | 39% |
| 50%–55% | 51 | 52% | 45% |
| 55%–60% | 66 | 57% | 64% |
| 60%–65% | 46 | 62% | 57% |
| 65%+ | 41 | 69% | 66% |

> Calibrated = predicted ≈ actual per band. Systematic gaps mean the win probabilities themselves need retuning before any ML edge claim.

### Model A — segments (finding the winning slice)

- **by market:** Moneyline 221-156 (+2%, CLV -3.6%)  ·  NRFI 6-5 (+1%, CLV -4.0%)  ·  Run Line 42-48 (-2%)  ·  Total 88-89 (-3%, CLV +0.8%)  ·  F5 Total 18-23 (-23%, CLV -2.5%)
- **by side:** Under 62-55 (+2%, CLV +1.5%)  ·  team 287-232 (-0%, CLV -3.4%)  ·  Over 26-34 (-14%, CLV +0.4%)
- **by fav_band:** unknown 20-14 (+12%)  ·  pickem 189-167 (+2%, CLV +0.2%)  ·  fav 114-82 (-5%, CLV -7.1%)  ·  heavy fav 23-12 (-7%, CLV -1.7%)  ·  dog 29-46 (-7%, CLV -1.9%)

### Model B — segments (finding the winning slice)

- **by market:** Total 64-49 (+9%)  ·  Moneyline 142-101 (+4%)  ·  Run Line 31-41 (-7%)
- **by side:** Over 13-7 (+24%)  ·  Under 51-42 (+6%)  ·  team 173-142 (+1%)
- **by fav_band:** pickem 129-98 (+9%)  ·  fav 68-40 (+4%)  ·  dog 27-40 (-5%)  ·  unknown 2-3 (-24%)  ·  heavy fav 11-10 (-26%)

## Model A — picks by date

### 2026-08-30 — 2-3  (-1.49u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Pittsburgh Pirates @ St. Louis Cardinals | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -113** / FanDuel -114 | — | +0.88 |
| ✅ WIN | PLAY | San Diego Padres @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -158** / DraftKings -165 | — | +0.63 |
| ❌ LOSS | PLAY | Texas Rangers @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -162 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -142** / DraftKings -142 | — | -1.00 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Los Angeles Angels | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -148** | — | -1.00 |

### 2026-08-29 — 5-0  (+3.36u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -196** / DraftKings -197 | — | +0.51 |
| ✅ WIN | PLAY | Texas Rangers @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -164** / DraftKings -171 | — | +0.61 |
| ✅ WIN | PLAY | Baltimore Orioles @ Athletics | Total | Over 5.5 | 5.5 | **DraftKings -104** / FanDuel -120 | — | +0.96 |
| ✅ WIN | PLAY | Seattle Mariners @ Toronto Blue Jays | Moneyline | Toronto Blue Jays ML | — | **FanDuel -126** / DraftKings -126 | — | +0.79 |
| ✅ WIN | PLAY | Colorado Rockies @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -205** / DraftKings -230 | — | +0.49 |

### 2026-08-28 — 2-1  (+0.49u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Chicago Cubs | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -128** | — | +0.78 |
| ✅ WIN | PLAY | Chicago White Sox @ Minnesota Twins | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -140** | — | +0.71 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ St. Louis Cardinals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel +100** | — | -1.00 |

### 2026-08-27 — 0-1  (-1.00u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ❌ LOSS | PLAY | Colorado Rockies @ Washington Nationals | F5 Total | F5 Over 5.5 | 5.5 | **FanDuel -114** | — | -1.00 |

### 2026-08-26 — 4-1  (+1.84u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Colorado Rockies @ Washington Nationals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -135** | — | +0.74 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Seattle Mariners | Moneyline | Philadelphia Phillies ML | — | **FanDuel -126** / DraftKings -130 | — | +0.79 |
| ✅ WIN | PLAY | Milwaukee Brewers @ New York Mets | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -163 | — | +0.65 |
| ✅ WIN | PLAY | Cincinnati Reds @ San Francisco Giants | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -152** | — | +0.66 |
| ❌ LOSS | PLAY | Colorado Rockies @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -120** / DraftKings -131 | — | -1.00 |

### 2026-08-25 — 1-3  (-2.04u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Philadelphia Phillies @ Seattle Mariners | Total | Under 11.5 | 11.5 | **FanDuel -104** / DraftKings -118 | — | +0.96 |
| ❌ LOSS | PLAY | Baltimore Orioles @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **DraftKings -131** / FanDuel -132 | -2.4% | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ New York Mets | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -167 | -1.9% | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Arizona Diamondbacks | Moneyline | Chicago Cubs ML | — | **FanDuel -108** / DraftKings -114 | +0.0% | -1.00 |

### 2026-08-24 — 4-2  (+1.06u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Chicago Cubs @ Arizona Diamondbacks | Moneyline | Chicago Cubs ML | — | **FanDuel -142** / DraftKings -150 | -11.5% | +0.70 |
| ✅ WIN | LEAN | Minnesota Twins @ Athletics | Moneyline | Minnesota Twins ML | — | **FanDuel -154** / DraftKings -156 | -1.6% | +0.65 |
| ✅ WIN | LEAN | Colorado Rockies @ Washington Nationals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -108** | +8.9% | +0.93 |
| ✅ WIN | LEAN | Colorado Rockies @ Washington Nationals | NRFI | NRFI | 0.5 | **FanDuel -128** | -3.6% | +0.78 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Seattle Mariners | Moneyline | Philadelphia Phillies ML | — | **FanDuel -116** / DraftKings -123 | -6.9% | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Arizona Diamondbacks | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -146** | -3.2% | -1.00 |

### 2026-08-23 — 10-5  (+2.60u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Baltimore Orioles | Moneyline | Tampa Bay Rays ML | — | **FanDuel -108** / DraftKings -113 | — | +0.93 |
| ✅ WIN | PLAY | Cleveland Guardians @ Colorado Rockies | Moneyline | Cleveland Guardians ML | — | **FanDuel -164** / DraftKings -175 | — | +0.61 |
| ✅ WIN | PLAY | Cleveland Guardians @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings +100** / FanDuel -128 | — | +1.00 |
| ✅ WIN | PLAY | San Francisco Giants @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -220** / DraftKings -231 | — | +0.45 |
| ✅ WIN | PLAY | Chicago Cubs @ Seattle Mariners | Moneyline | Chicago Cubs ML | — | **FanDuel -108** / DraftKings -111 | — | +0.93 |
| ✅ WIN | PLAY | Cincinnati Reds @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **FanDuel -126** / DraftKings -131 | +73.6% | +0.79 |
| ✅ WIN | PLAY | St. Louis Cardinals @ Philadelphia Phillies | Moneyline | Philadelphia Phillies ML | — | **FanDuel -220** / DraftKings -224 | — | +0.45 |
| ✅ WIN | LEAN | Toronto Blue Jays @ New York Yankees | NRFI | NRFI | 0.5 | **FanDuel -128** | — | +0.78 |
| ✅ WIN | LEAN | Athletics @ Houston Astros | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -146** | — | +0.68 |
| ✅ WIN | LEAN | Los Angeles Angels @ Texas Rangers | NRFI | NRFI | 0.5 | **FanDuel -102** | — | +0.98 |
| ❌ LOSS | PLAY | Atlanta Braves @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings +100** / FanDuel -102 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Miami Marlins | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -110** | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **DraftKings -132** / FanDuel -134 | -8.3% | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Miami Marlins | NRFI | NRFI | 0.5 | **FanDuel -125** | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ San Diego Padres | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -146** | — | -1.00 |

### 2026-08-22 — 9-11  (-5.11u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Pittsburgh Pirates @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -255** / DraftKings -267 | +3.5% | +0.39 |
| ✅ WIN | PLAY | San Francisco Giants @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **DraftKings -217** / FanDuel -220 | -2.0% | +0.46 |
| ✅ WIN | PLAY | Cleveland Guardians @ Colorado Rockies | Total | Under 11.0 | 11.0 | **FanDuel -105** / DraftKings -106 | +4.0% | +0.95 |
| ✅ WIN | PLAY | Washington Nationals @ Miami Marlins | Moneyline | Miami Marlins ML | — | **DraftKings -186** / FanDuel -188 | -4.7% | +0.54 |
| ✅ WIN | PLAY | Washington Nationals @ Miami Marlins | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -152** | — | +0.66 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Los Angeles Dodgers | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -154** | +0.0% | +0.65 |
| ✅ WIN | LEAN | Minnesota Twins @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -164** / DraftKings -164 | -7.8% | +0.61 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Philadelphia Phillies | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -138** | — | +0.72 |
| ✅ WIN | LEAN | Detroit Tigers @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **DraftKings -110** / FanDuel -116 | -2.7% | +0.91 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Baltimore Orioles | Moneyline | Tampa Bay Rays ML | — | **FanDuel -130** / DraftKings -136 | -8.1% | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Seattle Mariners | Moneyline | Chicago Cubs ML | — | **FanDuel +102** / DraftKings -101 | +6.7% | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **DraftKings -163** / FanDuel -174 | -7.0% | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Miami Marlins | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Los Angeles Dodgers | Total | Over 7.5 | 7.5 | **DraftKings -112** / FanDuel -115 | +0.0% | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Houston Astros | Moneyline | Houston Astros ML | — | **DraftKings -246** / FanDuel -255 | -1.3% | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Texas Rangers | NRFI | NRFI | 0.5 | **FanDuel -104** | -0.9% | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Seattle Mariners | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -104** | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Miami Marlins | NRFI | NRFI | 0.5 | **FanDuel -128** | — | -1.00 |
| ❌ LOSS | LEAN | Cincinnati Reds @ Arizona Diamondbacks | Total | Under 9.5 | 9.5 | **DraftKings -112** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ New York Yankees | NRFI | NRFI | 0.5 | **FanDuel -192** | -13.5% | -1.00 |

### 2026-08-21 — 6-3  (+1.34u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -178** / DraftKings -186 | +6.6% | +0.56 |
| ✅ WIN | PLAY | Cleveland Guardians @ Colorado Rockies | Total | Under 11.0 | 11.0 | **FanDuel +100** / DraftKings -117 | -1.0% | +1.00 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -230** / DraftKings -245 | +3.1% | +0.43 |
| ✅ WIN | LEAN | Cleveland Guardians @ Colorado Rockies | Moneyline | Cleveland Guardians ML | — | **DraftKings -157** / FanDuel -158 | -4.0% | +0.64 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Baltimore Orioles | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -113** | -9.4% | +0.88 |
| ✅ WIN | LEAN | Minnesota Twins @ San Diego Padres | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -120** | -1.9% | +0.83 |
| ❌ LOSS | PLAY | Chicago Cubs @ Seattle Mariners | Moneyline | Chicago Cubs ML | — | **FanDuel -108** / DraftKings -108 | -3.7% | -1.00 |
| ❌ LOSS | PLAY | Atlanta Braves @ Milwaukee Brewers | F5 Total | F5 Over 2.5 | 2.5 | **FanDuel -160** | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ Milwaukee Brewers | Total | Over 6.5 | 6.5 | **FanDuel -102** / DraftKings -112 | — | -1.00 |

### 2026-08-20 — 3-3  (-0.56u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -126** / DraftKings -131 | — | +0.79 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Cincinnati Reds | Moneyline | St. Louis Cardinals ML | — | **FanDuel -110** / DraftKings -118 | — | +0.91 |
| ✅ WIN | LEAN | Athletics @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel -136** / DraftKings -142 | — | +0.74 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **DraftKings -166** / FanDuel -172 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Tampa Bay Rays | Total | Over 7.5 | 7.5 | **FanDuel -118** / DraftKings -118 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Texas Rangers | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -146** | +1.6% | -1.00 |

### 2026-08-19 — 2-6  (-4.81u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Dodgers @ Colorado Rockies | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -197** / FanDuel -198 | -0.7% | +0.51 |
| ✅ WIN | LEAN | Toronto Blue Jays @ Tampa Bay Rays | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -148** | -17.9% | +0.68 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **DraftKings -149** / FanDuel -154 | +12.7% | -1.00 |
| ❌ LOSS | PLAY | Seattle Mariners @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -120** / DraftKings -125 | +2.2% | -1.00 |
| ❌ LOSS | LEAN | Chicago White Sox @ Chicago Cubs | Total | Over 7.5 | 7.5 | **FanDuel +110** / DraftKings +104 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Texas Rangers | Total | Over 7.5 | 7.5 | **DraftKings -110** / FanDuel -114 | +5.3% | -1.00 |
| ❌ LOSS | LEAN | Detroit Tigers @ Pittsburgh Pirates | Total | Over 8.0 | 8.0 | **FanDuel -112** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago White Sox @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -195** / DraftKings -205 | — | -1.00 |

### 2026-08-18 — 4-3  (-0.42u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Dodgers @ Colorado Rockies | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -180** / DraftKings -193 | +3.4% | +0.56 |
| ✅ WIN | PLAY | St. Louis Cardinals @ Cincinnati Reds | Moneyline | St. Louis Cardinals ML | — | **FanDuel -120** / DraftKings -123 | -18.1% | +0.83 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **DraftKings -171** / FanDuel -174 | -6.5% | +0.58 |
| ✅ WIN | LEAN | Chicago White Sox @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -164** / DraftKings -175 | +0.9% | +0.61 |
| ❌ LOSS | PLAY | Atlanta Braves @ Minnesota Twins | Moneyline | Atlanta Braves ML | — | **FanDuel -126** / DraftKings -131 | -9.4% | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -146** / DraftKings -150 | +14.1% | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ Minnesota Twins | Total | Over 8.5 | 8.5 | **FanDuel -115** / DraftKings -122 | — | -1.00 |

### 2026-08-17 — 3-2  (-0.09u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Baltimore Orioles @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -156** / DraftKings -167 | -30.2% | +0.64 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Colorado Rockies | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -255** / DraftKings -258 | -11.6% | +0.39 |
| ✅ WIN | LEAN | Chicago White Sox @ Chicago Cubs | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -113** | -2.1% | +0.88 |
| ❌ LOSS | PLAY | Atlanta Braves @ Minnesota Twins | Moneyline | Atlanta Braves ML | — | **FanDuel -122** / DraftKings -132 | +0.7% | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Colorado Rockies | Total | Under 11.0 | 11.0 | **FanDuel -115** / DraftKings -118 | — | -1.00 |

### 2026-08-16 — 8-2  (+4.46u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Miami Marlins @ Cincinnati Reds | Moneyline | Miami Marlins ML | — | **FanDuel -122** / DraftKings -126 | — | +0.82 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Minnesota Twins | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -144** | — | +0.69 |
| ✅ WIN | PLAY | Texas Rangers @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -112** / FanDuel -120 | — | +0.89 |
| ✅ WIN | LEAN | Miami Marlins @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings -103** / FanDuel -120 | — | +0.97 |
| ✅ WIN | LEAN | New York Yankees @ Toronto Blue Jays | NRFI | NRFI | 0.5 | **FanDuel -184** | — | +0.54 |
| ✅ WIN | LEAN | Baltimore Orioles @ Tampa Bay Rays | Total | Over 8.0 | 8.0 | **DraftKings -102** / FanDuel -115 | — | +0.98 |
| ✅ WIN | LEAN | Washington Nationals @ New York Mets | Moneyline | New York Mets ML | — | **DraftKings -175** / FanDuel -178 | — | +0.57 |
| ✅ WIN | LEAN | Kansas City Royals @ Los Angeles Angels | NRFI | NRFI | 0.5 | **FanDuel +100** | — | +1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -134** / DraftKings -135 | -95.8% | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Tampa Bay Rays | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel +116** | — | -1.00 |

### 2026-08-15 — 3-7  (-4.46u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Texas Rangers @ Athletics | Total | Under 11.5 | 11.5 | **FanDuel -118** / DraftKings -120 | — | +0.85 |
| ✅ WIN | PLAY | Boston Red Sox @ Pittsburgh Pirates | Moneyline | Boston Red Sox ML | — | **FanDuel -126** / DraftKings -126 | -11.2% | +0.79 |
| ✅ WIN | LEAN | Colorado Rockies @ San Francisco Giants | Total | Over 7.5 | 7.5 | **DraftKings -111** / FanDuel -115 | — | +0.90 |
| ❌ LOSS | PLAY | St. Louis Cardinals @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -166** / DraftKings -181 | -0.9% | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Cleveland Guardians | Moneyline | San Diego Padres ML | — | **FanDuel +102** | +6.7% | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Atlanta Braves | Total | Under 9.5 | 9.5 | **DraftKings -107** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Atlanta Braves | F5 Total | F5 Under 5.5 | 5.5 | **FanDuel -132** | +0.0% | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Pittsburgh Pirates | Total | Over 7.5 | 7.5 | **FanDuel -115** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Chicago Cubs | Total | Under 9.5 | 9.5 | **DraftKings -118** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Tampa Bay Rays | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -144** | — | -1.00 |

### 2026-08-14 — 1-7  (-6.44u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | St. Louis Cardinals @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -180** / DraftKings -191 | -1.2% | +0.56 |
| ❌ LOSS | PLAY | Colorado Rockies @ San Francisco Giants | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -122 | -4.1% | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Pittsburgh Pirates | Moneyline | Boston Red Sox ML | — | **FanDuel -144** / DraftKings -144 | -7.6% | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ New York Mets | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -120** | +0.0% | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Tampa Bay Rays | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -120** | -1.9% | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel +112** | -1.9% | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Chicago Cubs | Total | Over 8.0 | 8.0 | **FanDuel -108** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ New York Mets | Moneyline | Washington Nationals ML | — | **FanDuel +102** / DraftKings +100 | -1.9% | -1.00 |

### 2026-08-13 — 1-1  (-0.17u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Philadelphia Phillies @ Minnesota Twins | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -120** | +0.8% | +0.83 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel -112** / DraftKings -114 | -3.5% | -1.00 |

### 2026-08-12 — 5-3  (+0.91u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Athletics | Moneyline | Tampa Bay Rays ML | — | **FanDuel -200** | — | +0.50 |
| ✅ WIN | PLAY | Chicago Cubs @ Washington Nationals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -144** | -11.2% | +0.69 |
| ✅ WIN | PLAY | Texas Rangers @ Los Angeles Angels | Total | Under 9.5 | 9.5 | **FanDuel -106** / DraftKings -122 | — | +0.94 |
| ✅ WIN | LEAN | Cleveland Guardians @ Detroit Tigers | NRFI | YRFI | 0.5 | **FanDuel +106** | +2.0% | +1.06 |
| ✅ WIN | LEAN | Houston Astros @ San Francisco Giants | Moneyline | Houston Astros ML | — | **FanDuel -138** | — | +0.72 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -130** / DraftKings -131 | -14.1% | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Chicago White Sox | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -130** | +0.0% | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **FanDuel -172** / DraftKings -180 | — | -1.00 |

### 2026-08-11 — 6-6  (-1.84u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Athletics | Moneyline | Tampa Bay Rays ML | — | **FanDuel -172** / DraftKings -174 | — | +0.58 |
| ✅ WIN | PLAY | Kansas City Royals @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -260** / DraftKings -264 | — | +0.38 |
| ✅ WIN | PLAY | Cleveland Guardians @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -120** / DraftKings -124 | — | +0.83 |
| ✅ WIN | PLAY | New York Mets @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -124** / DraftKings -130 | — | +0.81 |
| ✅ WIN | LEAN | Chicago Cubs @ Washington Nationals | Moneyline | Chicago Cubs ML | — | **DraftKings -159** / FanDuel -160 | — | +0.63 |
| ✅ WIN | LEAN | Milwaukee Brewers @ San Diego Padres | Total | Over 7.5 | 7.5 | **FanDuel -108** / DraftKings -108 | — | +0.93 |
| ❌ LOSS | PLAY | Houston Astros @ San Francisco Giants | Moneyline | Houston Astros ML | — | **DraftKings -177** / FanDuel -184 | — | -1.00 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel -105** / DraftKings -115 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Miami Marlins | Total | Over 7.0 | 7.0 | **FanDuel -102** / DraftKings -104 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ St. Louis Cardinals | Moneyline | Philadelphia Phillies ML | — | **FanDuel -160** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Miami Marlins | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -114** | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **FanDuel -168** / DraftKings -170 | — | -1.00 |

### 2026-08-09 — 5-4  (-0.65u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Boston Red Sox | Total | Under 10.5 | 10.5 | **FanDuel -115** / DraftKings -118 | — | +0.87 |
| ✅ WIN | PLAY | Minnesota Twins @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -245** / DraftKings -258 | — | +0.41 |
| ✅ WIN | PLAY | Detroit Tigers @ San Francisco Giants | Moneyline | Detroit Tigers ML | — | **FanDuel -118** / DraftKings -119 | — | +0.85 |
| ✅ WIN | PLAY | Chicago Cubs @ Kansas City Royals | Moneyline | Chicago Cubs ML | — | **FanDuel -162** / DraftKings -171 | — | +0.62 |
| ✅ WIN | LEAN | Colorado Rockies @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -166** / DraftKings -168 | — | +0.60 |
| ❌ LOSS | PLAY | New York Mets @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -142** / FanDuel -142 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Kansas City Royals | Total | Under 10.0 | 10.0 | **FanDuel -105** / DraftKings -108 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Arizona Diamondbacks | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -146** / DraftKings -149 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -103** / FanDuel -104 | — | -1.00 |

### 2026-08-08 — 4-4  (-0.70u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Detroit Tigers @ San Francisco Giants | Moneyline | Detroit Tigers ML | — | **DraftKings -110** / FanDuel -112 | — | +0.91 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Seattle Mariners | Moneyline | Tampa Bay Rays ML | — | **FanDuel +104** / DraftKings -101 | — | +1.04 |
| ✅ WIN | PLAY | Colorado Rockies @ St. Louis Cardinals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -128** | — | +0.78 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Arizona Diamondbacks | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -176** / DraftKings -180 | — | +0.57 |
| ❌ LOSS | PLAY | Athletics @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **DraftKings -243** / FanDuel -245 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Kansas City Royals | Moneyline | Chicago Cubs ML | — | **FanDuel -164** / DraftKings -175 | — | -1.00 |
| ❌ LOSS | PLAY | Houston Astros @ San Diego Padres | Moneyline | Houston Astros ML | — | **DraftKings +104** / FanDuel +100 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Boston Red Sox | Total | Under 9.5 | 9.5 | **DraftKings +101** / FanDuel -124 | — | -1.00 |

### 2026-08-07 — 4-7  (-4.14u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -255** / DraftKings -269 | — | +0.39 |
| ✅ WIN | PLAY | Chicago Cubs @ Kansas City Royals | Moneyline | Chicago Cubs ML | — | **FanDuel -164** | — | +0.61 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Seattle Mariners | Moneyline | Tampa Bay Rays ML | — | **DraftKings +101** / FanDuel +100 | — | +1.01 |
| ✅ WIN | PLAY | Minnesota Twins @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -120 | — | +0.85 |
| ❌ LOSS | PLAY | Detroit Tigers @ San Francisco Giants | Moneyline | Detroit Tigers ML | — | **FanDuel -124** | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Arizona Diamondbacks | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -140** | — | -1.00 |
| ➖ PUSH | PLAY | Chicago Cubs @ Kansas City Royals | Total | Under 10.0 | 10.0 | **FanDuel -122** | — | +0.00 |
| ❌ LOSS | PLAY | Minnesota Twins @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -171 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Arizona Diamondbacks | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -166** / DraftKings -181 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Boston Red Sox | NRFI | YRFI | 0.5 | **FanDuel +100** | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Philadelphia Phillies | Total | Under 8.5 | 8.5 | **DraftKings -112** / FanDuel -128 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Texas Rangers | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -144** | — | -1.00 |

### 2026-08-06 — 4-6  (-3.55u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Cincinnati Reds | Moneyline | Cincinnati Reds ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Washington Nationals @ Philadelphia Phillies | Moneyline | Philadelphia Phillies ML | — | **FanDuel -335** / DraftKings -354 | — | +0.30 |
| ✅ WIN | PLAY | Chicago White Sox @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -184** / DraftKings -192 | — | +0.54 |
| ✅ WIN | LEAN | Los Angeles Angels @ Baltimore Orioles | Total | Under 10.0 | 10.0 | **DraftKings -104** / FanDuel -114 | — | +0.96 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Chicago Cubs | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -144** | — | -1.00 |
| ❌ LOSS | LEAN | Chicago White Sox @ Boston Red Sox | Run Line | Boston Red Sox -1.5 | — | **FanDuel +116** / DraftKings +109 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **FanDuel -106** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Chicago Cubs | Total | Over 7.5 | 7.5 | **DraftKings -105** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **DraftKings -114** / FanDuel -116 | — | -1.00 |

### 2026-08-05 — 5-10  (-6.00u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -108** / FanDuel -110 | — | +0.93 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -130** / DraftKings -136 | — | +0.77 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -110 | — | +0.91 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Moneyline | Tampa Bay Rays ML | — | **FanDuel -154** / DraftKings -167 | — | +0.65 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Colorado Rockies | F5 Total | F5 Under 6.5 | 6.5 | **FanDuel -135** | — | +0.74 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -158** / DraftKings -169 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Arizona Diamondbacks | Moneyline | San Diego Padres ML | — | **FanDuel -112** / DraftKings -121 | — | -1.00 |
| ❌ LOSS | PLAY | Detroit Tigers @ Seattle Mariners | Moneyline | Detroit Tigers ML | — | **DraftKings +128** / FanDuel +124 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Philadelphia Phillies | F5 Total | F5 Over 5.5 | 5.5 | **FanDuel -110** | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.0 | 7.0 | **DraftKings -117** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Run Line | Houston Astros -1.5 | — | **FanDuel +130** / DraftKings +118 | — | -1.00 |
| ❌ LOSS | PLAY | Minnesota Twins @ Kansas City Royals | F5 Total | F5 Over 4.5 | 4.5 | **FanDuel -138** | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Arizona Diamondbacks | Total | Under 9.5 | 9.5 | **DraftKings +101** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Milwaukee Brewers | F5 Total | F5 Over 3.5 | 3.5 | **FanDuel -132** | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings +102** / FanDuel -120 | — | -1.00 |

### 2026-08-04 — 4-5  (-2.22u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -167 | — | +0.65 |
| ✅ WIN | PLAY | Washington Nationals @ Philadelphia Phillies | Moneyline | Philadelphia Phillies ML | — | **FanDuel -250** / DraftKings -263 | — | +0.40 |
| ✅ WIN | PLAY | Athletics @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings -106** / FanDuel -122 | — | +0.94 |
| ✅ WIN | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -126** / DraftKings -131 | — | +0.79 |
| ❌ LOSS | PLAY | Minnesota Twins @ Kansas City Royals | Total | Under 9.5 | 9.5 | **DraftKings -105** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Texas Rangers | Moneyline | San Francisco Giants ML | — | **DraftKings +167** / FanDuel +166 | — | -1.00 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -108** / FanDuel -114 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Chicago Cubs | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -208** / FanDuel -210 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -114** / FanDuel -115 | — | -1.00 |

### 2026-08-03 — 3-3  (-0.45u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Texas Rangers | Moneyline | San Francisco Giants ML | — | **FanDuel +100** / DraftKings -110 | — | +1.00 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Moneyline | Tampa Bay Rays ML | — | **FanDuel -156** / DraftKings -166 | — | +0.64 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ Chicago Cubs | Total | Over 8.0 | 8.0 | **FanDuel -110** / DraftKings -113 | — | +0.91 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -126** / DraftKings -136 | — | -1.00 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -115** / DraftKings -115 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 8.5 | 8.5 | **FanDuel -104** / DraftKings -106 | — | -1.00 |

### 2026-08-02 — 7-2  (+4.75u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Texas Rangers @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -122** / DraftKings -126 | — | +0.82 |
| ✅ WIN | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 12.5 | 12.5 | **DraftKings -103** / FanDuel -110 | — | +0.97 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -106** / DraftKings -115 | — | +0.94 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Total | Under 11.5 | 11.5 | **DraftKings -112** / FanDuel -122 | — | +0.89 |
| ✅ WIN | PLAY | Texas Rangers @ Houston Astros | Run Line | Houston Astros -1.5 | — | **DraftKings +163** / FanDuel +160 | — | +1.63 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Baltimore Orioles | Moneyline | Philadelphia Phillies ML | — | **FanDuel -128** / DraftKings -137 | — | +0.78 |
| ✅ WIN | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -138** / DraftKings -150 | — | +0.72 |
| ❌ LOSS | PLAY | New York Yankees @ Chicago Cubs | Total | Over 6.5 | 6.5 | **DraftKings -111** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Houston Astros | Total | Under 9.0 | 9.0 | **DraftKings +101** / FanDuel -120 | — | -1.00 |

### 2026-08-01 — 7-3  (+2.52u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | New York Yankees @ Chicago Cubs | Total | Over 6.5 | 6.5 | **DraftKings +100** / FanDuel -104 | — | +1.00 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -132** / DraftKings -137 | — | +0.76 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -114** / DraftKings -123 | — | +0.88 |
| ✅ WIN | PLAY | Miami Marlins @ New York Mets | Total | Under 9.0 | 9.0 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | Washington Nationals @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -184** / DraftKings -197 | — | +0.54 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Baltimore Orioles | Moneyline | Philadelphia Phillies ML | — | **FanDuel -138** / DraftKings -148 | — | +0.72 |
| ✅ WIN | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -134** / DraftKings -136 | — | +0.75 |
| ❌ LOSS | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 12.0 | 12.0 | **DraftKings -115** / FanDuel -118 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -161 | — | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +138** / DraftKings +131 | — | -1.00 |

### 2026-07-31 — 6-6  (-0.99u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -107** / FanDuel -120 | — | +0.93 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -154** / DraftKings -163 | — | +0.65 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -120 | — | +0.85 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Los Angeles Angels | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -171 | — | +0.62 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Run Line | Detroit Tigers -1.5 | — | **FanDuel +100** / DraftKings -105 | — | +1.00 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Los Angeles Angels | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -126** / DraftKings -135 | — | -1.00 |
| ❌ LOSS | PLAY | Detroit Tigers @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel +100** / DraftKings +100 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | — | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +136** / DraftKings +128 | — | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | — | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Colorado Rockies | Moneyline | Kansas City Royals ML | — | **FanDuel -108** / DraftKings -111 | — | -1.00 |

### 2026-07-30 — 5-4  (+0.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel +102** / DraftKings +100 | — | +1.02 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -108** / FanDuel -110 | — | +0.93 |
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -156** / FanDuel -162 | — | +0.64 |
| ✅ WIN | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -144** / DraftKings -150 | — | +0.69 |
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings +135** / FanDuel +134 | — | +1.35 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -112** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Run Line | Pittsburgh Pirates -1.5 | — | **DraftKings +135** / FanDuel +134 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +160** / DraftKings +153 | — | -1.00 |
| ❌ LOSS | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -124** / DraftKings -131 | — | -1.00 |

### 2026-07-29 — 4-8  (-4.96u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -144** / DraftKings -150 | — | +0.69 |
| ✅ WIN | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -138** / DraftKings -143 | — | +0.72 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -154** / DraftKings -156 | — | +0.65 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel -102** / DraftKings -106 | — | +0.98 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -174** / DraftKings -180 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel -116** / DraftKings -127 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +140** / DraftKings +138 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ St. Louis Cardinals | Run Line | Chicago Cubs -1.5 | — | **FanDuel +146** / DraftKings +131 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -129** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel +106** / DraftKings +102 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Tampa Bay Rays | Total | Over 7.5 | 7.5 | **DraftKings -107** / FanDuel -108 | — | -1.00 |

### 2026-07-28 — 8-7  (-0.25u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel -112** / DraftKings -115 | — | +0.89 |
| ✅ WIN | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -143 | — | +0.75 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 9.5 | 9.5 | **FanDuel -102** / DraftKings -108 | — | +0.98 |
| ✅ WIN | PLAY | Milwaukee Brewers @ San Francisco Giants | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +130** / DraftKings +124 | — | +1.30 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -110** / DraftKings -117 | — | +0.91 |
| ✅ WIN | LEAN | Colorado Rockies @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -180** / DraftKings -191 | — | +0.56 |
| ✅ WIN | LEAN | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -136** / DraftKings -144 | — | +0.74 |
| ✅ WIN | LEAN | Kansas City Royals @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ❌ LOSS | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **DraftKings -175** / FanDuel -178 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -144** / DraftKings -155 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -184** / DraftKings -192 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Detroit Tigers | Total | Under 9.5 | 9.5 | **DraftKings -103** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -110** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Miami Marlins | Run Line | Miami Marlins -1.5 | — | **DraftKings -194** / FanDuel -196 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Diego Padres | Run Line | San Diego Padres -1.5 | — | **FanDuel +118** / DraftKings +113 | — | -1.00 |

### 2026-07-27 — 3-5  (-2.59u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -168** / DraftKings -182 | — | +0.60 |
| ✅ WIN | LEAN | Boston Red Sox @ Athletics | Run Line | Boston Red Sox -1.5 | — | **FanDuel -105** / DraftKings -111 | — | +0.95 |
| ✅ WIN | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -116** / DraftKings -123 | — | +0.86 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -137 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -130** / DraftKings -131 | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ New York Mets | Moneyline | Atlanta Braves ML | — | **DraftKings -115** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Milwaukee Brewers @ San Francisco Giants | Total | Over 8.5 | 8.5 | **DraftKings -105** / FanDuel -105 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Washington Nationals | Run Line | Washington Nationals -1.5 | — | **FanDuel +155** / DraftKings +143 | — | -1.00 |

### 2026-07-26 — 6-2  (+2.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -142** / DraftKings -143 | — | +0.70 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -320** / DraftKings -340 | — | +0.31 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **FanDuel -114** / DraftKings -118 | — | +0.88 |
| ✅ WIN | PLAY | Atlanta Braves @ Baltimore Orioles | Moneyline | Atlanta Braves ML | — | **FanDuel -104** / DraftKings -106 | — | +0.96 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -144** / DraftKings -149 | — | +0.69 |
| ✅ WIN | LEAN | Cincinnati Reds @ St. Louis Cardinals | Total | Under 9.0 | 9.0 | **DraftKings -101** / FanDuel -122 | — | +0.99 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ New York Mets | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -172 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Texas Rangers | Moneyline | Texas Rangers ML | — | **FanDuel -110** / DraftKings -111 | — | -1.00 |

### 2026-07-25 — 6-2  (+3.30u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -134** / DraftKings -134 | — | +0.75 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -215** / DraftKings -228 | — | +0.47 |
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +168** / DraftKings +159 | — | +1.68 |
| ✅ WIN | LEAN | Athletics @ Minnesota Twins | Total | Under 10.5 | 10.5 | **FanDuel -110** / DraftKings -114 | — | +0.91 |
| ✅ WIN | LEAN | Colorado Rockies @ Milwaukee Brewers | Total | Over 8.5 | 8.5 | **DraftKings -114** / FanDuel -115 | — | +0.88 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ New York Mets | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -163** / FanDuel -164 | — | +0.61 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -112** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -132** / DraftKings -136 | — | -1.00 |

### 2026-07-24 — 3-3  (+0.43u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Atlanta Braves @ Baltimore Orioles | Moneyline | Atlanta Braves ML | — | **FanDuel +100** / DraftKings -101 | — | +1.00 |
| ✅ WIN | LEAN | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -134** / DraftKings -142 | — | +0.75 |
| ✅ WIN | LEAN | Cleveland Guardians @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +168** / DraftKings +153 | — | +1.68 |
| ❌ LOSS | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -240** / DraftKings -258 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -108** / DraftKings -115 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |

### 2026-07-23 — 1-2  (-1.57u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -235** / DraftKings -249 | — | +0.43 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **DraftKings -107** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -110** / DraftKings -123 | — | -1.00 |

### 2026-07-22 — 5-1  (+3.95u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Washington Nationals @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -104** / DraftKings -110 | — | +0.96 |
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -118** / DraftKings -120 | — | +0.85 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Philadelphia Phillies | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -112** / DraftKings -120 | — | +0.89 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ Philadelphia Phillies | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +138** / DraftKings +129 | — | +1.38 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -144** / DraftKings -147 | — | -1.00 |

### 2026-07-21 — 2-5  (-2.59u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -112** / DraftKings -115 | — | +0.89 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Toronto Blue Jays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +152** / DraftKings +149 | — | +1.52 |
| ❌ LOSS | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -144** / DraftKings -149 | — | -1.00 |
| ❌ LOSS | PLAY | New York Mets @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -142** / DraftKings -149 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +140** / DraftKings +138 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Colorado Rockies | Total | Under 13.0 | 13.0 | **FanDuel +100** / DraftKings -113 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Colorado Rockies | Moneyline | Washington Nationals ML | — | **FanDuel -102** / DraftKings -106 | — | -1.00 |

### 2026-07-20 — 8-3  (+4.35u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -144** / DraftKings -144 | — | +0.69 |
| ✅ WIN | PLAY | Chicago White Sox @ Texas Rangers | Moneyline | Chicago White Sox ML | — | **DraftKings +144** / FanDuel +142 | — | +1.44 |
| ✅ WIN | PLAY | New York Mets @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -198** / DraftKings -199 | — | +0.51 |
| ✅ WIN | LEAN | Washington Nationals @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -102** / DraftKings -114 | — | +0.98 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **DraftKings -120** / FanDuel -124 | — | +0.83 |
| ✅ WIN | LEAN | New York Mets @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +106** / DraftKings +100 | — | +1.06 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ New York Yankees | Total | Over 8.0 | 8.0 | **DraftKings -103** / FanDuel -110 | — | +0.97 |
| ❌ LOSS | PLAY | Detroit Tigers @ Chicago Cubs | Total | Under 12.0 | 12.0 | **DraftKings -111** / FanDuel -112 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **FanDuel -162** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +142** / DraftKings +131 | — | -1.00 |

### 2026-07-19 — 7-6  (+0.32u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel +104** / DraftKings +100 | — | +1.04 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cleveland Guardians | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -124** / DraftKings -131 | — | +0.81 |
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -156** / DraftKings -163 | — | +0.64 |
| ✅ WIN | PLAY | Minnesota Twins @ Chicago Cubs | Total | Over 8.0 | 8.0 | **FanDuel -102** / DraftKings -110 | — | +0.98 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Cleveland Guardians | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +146** / DraftKings +139 | — | +1.46 |
| ✅ WIN | LEAN | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel -130** / DraftKings -143 | — | +0.77 |
| ✅ WIN | LEAN | Minnesota Twins @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -162** / DraftKings -169 | — | +0.62 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ New York Yankees | Total | Over 7.5 | 7.5 | **FanDuel -110** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -108** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **DraftKings -131** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -105** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Cincinnati Reds @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Arizona Diamondbacks | Total | Under 9.0 | 9.0 | **FanDuel -112** / DraftKings -112 | — | -1.00 |

### 2026-07-18 — 5-6  (-1.58u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel +100** / DraftKings -102 | — | +1.00 |
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings +100** / FanDuel -104 | — | +1.00 |
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Run Line | Kansas City Royals -1.5 | — | **FanDuel -156** / DraftKings -163 | — | +0.64 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -120** / DraftKings -120 | — | +0.83 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Cleveland Guardians | Total | Over 7.5 | 7.5 | **FanDuel -105** / DraftKings -118 | — | +0.95 |
| ➖ PUSH | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 13.0 | 13.0 | **FanDuel -106** / DraftKings -115 | — | +0.00 |
| ❌ LOSS | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -112** / DraftKings -117 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel +110** / DraftKings +108 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Seattle Mariners | Moneyline | San Francisco Giants ML | — | **FanDuel +116** / DraftKings +112 | — | -1.00 |
| ❌ LOSS | PLAY | Texas Rangers @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -192** / DraftKings -192 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Chicago Cubs | Moneyline | Minnesota Twins ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Cleveland Guardians | Moneyline | Pittsburgh Pirates ML | — | **FanDuel +108** / DraftKings -112 | — | -1.00 |

### 2026-07-17 — 4-2  (+1.01u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 12.0 | 12.0 | **DraftKings -111** / FanDuel -114 | — | +0.90 |
| ✅ WIN | PLAY | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel -104** / DraftKings -108 | — | +0.96 |
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -215** / DraftKings -217 | — | +0.47 |
| ✅ WIN | LEAN | Miami Marlins @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -146** / DraftKings -149 | — | +0.68 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.0 | 10.0 | **DraftKings -103** / FanDuel -104 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Athletics | Total | Under 10.0 | 10.0 | **DraftKings -108** / FanDuel -110 | — | -1.00 |

### 2026-07-16 — 1-0  (+0.96u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | New York Mets @ Philadelphia Phillies | Total | Under 9.5 | 9.5 | **FanDuel -104** / DraftKings -109 | — | +0.96 |

### 2026-07-12 — 4-4  (-0.49u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ Pittsburgh Pirates | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -122 | — | +0.87 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel -120** / DraftKings -126 | — | +0.83 |
| ✅ WIN | LEAN | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **DraftKings +113** / FanDuel +110 | — | +1.13 |
| ✅ WIN | LEAN | Kansas City Royals @ Baltimore Orioles | Moneyline | Baltimore Orioles ML | — | **FanDuel -148** / DraftKings -155 | — | +0.68 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -219** / FanDuel -225 | — | -1.00 |
| ❌ LOSS | PLAY | Seattle Mariners @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -130** / DraftKings -136 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -112** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Total | Over 8.5 | 8.5 | **DraftKings -117** / FanDuel -122 | — | -1.00 |

### 2026-07-11 — 4-8  (-4.30u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ✅ WIN | LEAN | Seattle Mariners @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -108** / DraftKings -114 | — | +0.93 |
| ✅ WIN | LEAN | New York Yankees @ Washington Nationals | Moneyline | New York Yankees ML | — | **FanDuel -190** / DraftKings -199 | — | +0.53 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel +128** | — | +1.28 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **FanDuel -116** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -260** / DraftKings -287 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Pittsburgh Pirates | Moneyline | Milwaukee Brewers ML | — | **DraftKings -125** / FanDuel -130 | — | -1.00 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Run Line | Atlanta Braves -1.5 | — | **FanDuel +142** / DraftKings +139 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Total | Over 8.5 | 8.5 | **FanDuel -105** / DraftKings -113 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | Colorado Rockies ML | — | **DraftKings +130** / FanDuel +124 | — | -1.00 |

### 2026-07-10 — 3-7  (-4.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel +104** / DraftKings +104 | — | +1.04 |
| ✅ WIN | LEAN | Athletics @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -166** / DraftKings -175 | — | +0.60 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **FanDuel -164** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -255** / DraftKings -272 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Cincinnati Reds | Moneyline | Chicago Cubs ML | — | **FanDuel -110** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -114** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -118** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Cincinnati Reds | Run Line | Chicago Cubs -1.5 | — | **DraftKings +142** / FanDuel +140 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **DraftKings -163** / FanDuel -166 | — | -1.00 |

### 2026-07-09 — 2-2  (-0.50u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **DraftKings -137** / FanDuel -138 | — | +0.73 |
| ✅ WIN | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -130** / DraftKings -136 | — | +0.77 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel +114** / DraftKings +108 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | Colorado Rockies ML | — | — | — | -1.00 |

### 2026-07-08 — 4-1  (+2.57u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -158** / DraftKings -163 | — | +0.63 |
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Run Line | Detroit Tigers -1.5 | — | **FanDuel +128** / DraftKings +128 | — | +1.28 |
| ✅ WIN | LEAN | Kansas City Royals @ New York Mets | Moneyline | New York Mets ML | — | — | — | +0.91 |
| ✅ WIN | LEAN | Houston Astros @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -134** / DraftKings -136 | — | +0.75 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -143 | — | -1.00 |

### 2026-07-07 — 2-2  (-0.18u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Milwaukee Brewers @ St. Louis Cardinals | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -122 | — | +0.87 |
| ✅ WIN | LEAN | Atlanta Braves @ Pittsburgh Pirates | Total | Over 8.0 | 8.0 | **DraftKings -105** / FanDuel -106 | — | +0.95 |
| ❌ LOSS | PLAY | Colorado Rockies @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -250** / DraftKings -272 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -126** / DraftKings -130 | — | -1.00 |

### 2026-07-06 — 2-3  (-1.64u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Colorado Rockies @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -230** / DraftKings -238 | — | +0.43 |
| ✅ WIN | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -108** / DraftKings -109 | — | +0.93 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Moneyline | Philadelphia Phillies ML | — | **FanDuel -200** / DraftKings -205 | — | -1.00 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Run Line | Philadelphia Phillies -1.5 | — | **DraftKings -125** / FanDuel -128 | — | -1.00 |
| ❌ LOSS | LEAN | Milwaukee Brewers @ St. Louis Cardinals | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +158** / DraftKings +148 | — | -1.00 |

### 2026-07-05 — 2-5  (-3.03u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | St. Louis Cardinals @ Chicago Cubs | Total | Over 8.0 | 8.0 | **DraftKings -110** / FanDuel -110 | — | +0.91 |
| ✅ WIN | LEAN | San Francisco Giants @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +106** / DraftKings +104 | — | +1.06 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Moneyline | Philadelphia Phillies ML | — | **FanDuel -136** / DraftKings -143 | — | -1.00 |
| ➖ PUSH | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 13.0 | 13.0 | **DraftKings -111** / FanDuel -118 | — | +0.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -220** / DraftKings -225 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -108** / DraftKings -109 | — | -1.00 |
| ❌ LOSS | LEAN | Miami Marlins @ Athletics | Total | Under 9.5 | 9.5 | **DraftKings -110** / FanDuel -112 | — | -1.00 |
| ❌ LOSS | LEAN | New York Mets @ Atlanta Braves | Total | Under 9.0 | 9.0 | **DraftKings -108** / FanDuel -110 | — | -1.00 |

### 2026-07-04 — 7-3  (+2.54u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel +100** / DraftKings -105 | — | +1.00 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Moneyline | Miami Marlins ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -240** / DraftKings -252 | — | +0.42 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -113 | — | +0.91 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -117** / FanDuel -120 | — | +0.85 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Washington Nationals | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -164** / DraftKings -167 | — | +0.61 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -109** / FanDuel -114 | — | +0.92 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Moneyline | Milwaukee Brewers ML | — | **FanDuel -148** / DraftKings -155 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings +102** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +108** / DraftKings +108 | — | -1.00 |

### 2026-07-03 — 7-3  (+2.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Houston Astros | Moneyline | Tampa Bay Rays ML | — | **FanDuel -108** / DraftKings -112 | — | +0.93 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Moneyline | Miami Marlins ML | — | **FanDuel +108** / DraftKings +104 | — | +1.08 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -245** / DraftKings -253 | — | +0.41 |
| ✅ WIN | PLAY | New York Mets @ Atlanta Braves | Total | Under 9.5 | 9.5 | **DraftKings -101** / FanDuel -124 | — | +0.99 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Run Line | Miami Marlins -1.5 | — | **DraftKings -182** / FanDuel -188 | — | +0.55 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Arizona Diamondbacks | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +105** / DraftKings +100 | — | +1.05 |
| ❌ LOSS | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -112** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -107** / FanDuel -114 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -113** / DraftKings -117 | — | -1.00 |

### 2026-07-02 — 5-4  (+0.18u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -118** / DraftKings -126 | — | +0.85 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -198** / DraftKings -198 | — | +0.51 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -109** / FanDuel -110 | — | +0.92 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings +108** / FanDuel +106 | — | +1.08 |
| ✅ WIN | LEAN | Cincinnati Reds @ Milwaukee Brewers | Total | Over 6.5 | 6.5 | **DraftKings -122** / FanDuel -124 | — | +0.82 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -196** / DraftKings -198 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **FanDuel -120** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -106** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +122** / DraftKings +119 | — | -1.00 |

### 2026-07-01 — 9-5  (+3.08u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -132** / DraftKings -136 | — | +0.76 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -110** / FanDuel -114 | — | +0.91 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -168** / DraftKings -168 | — | +0.60 |
| ✅ WIN | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -117** / FanDuel -120 | — | +0.85 |
| ✅ WIN | PLAY | Detroit Tigers @ New York Yankees | Total | Under 9.5 | 9.5 | **FanDuel -112** / DraftKings -112 | — | +0.89 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -102** / FanDuel -114 | — | +0.98 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +128** / FanDuel +120 | — | +1.28 |
| ✅ WIN | LEAN | San Diego Padres @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -120** / DraftKings -126 | — | +0.83 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Atlanta Braves | Total | Under 9.0 | 9.0 | **FanDuel -102** / DraftKings -107 | — | +0.98 |
| ❌ LOSS | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 12.0 | 12.0 | **FanDuel -110** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **FanDuel -154** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Boston Red Sox | Total | Under 9.5 | 9.5 | **FanDuel -106** / DraftKings -107 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Philadelphia Phillies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel +116** / DraftKings +113 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Run Line | Miami Marlins -1.5 | — | **FanDuel -105** / DraftKings -107 | — | -1.00 |

### 2026-06-30 — 9-5  (+2.96u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago White Sox @ Baltimore Orioles | Moneyline | Chicago White Sox ML | — | **DraftKings +119** / FanDuel +118 | — | +1.19 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -124** / DraftKings -132 | — | +0.81 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -172** / DraftKings -180 | — | +0.58 |
| ✅ WIN | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **DraftKings -156** / FanDuel -162 | — | +0.64 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Run Line | Tampa Bay Rays -1.5 | — | **DraftKings +119** / FanDuel +118 | — | +1.19 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +104** / DraftKings -103 | — | +1.04 |
| ✅ WIN | LEAN | Texas Rangers @ Cleveland Guardians | Moneyline | Texas Rangers ML | — | **DraftKings -119** / FanDuel -120 | — | +0.84 |
| ✅ WIN | LEAN | Washington Nationals @ Boston Red Sox | Total | Under 9.5 | 9.5 | **DraftKings +102** / FanDuel -115 | — | +1.02 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -104** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 11.5 | 11.5 | **DraftKings -101** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -118** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Houston Astros | Moneyline | Minnesota Twins ML | — | **DraftKings -115** / FanDuel -116 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Athletics | Total | Under 11.0 | 11.0 | **DraftKings -121** / FanDuel -122 | — | -1.00 |

### 2026-06-29 — 9-2  (+6.68u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago White Sox @ Baltimore Orioles | Moneyline | Chicago White Sox ML | — | **FanDuel +114** / DraftKings +114 | — | +1.14 |
| ✅ WIN | PLAY | Washington Nationals @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -168** / DraftKings -175 | — | +0.60 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -152** / DraftKings -156 | — | +0.66 |
| ✅ WIN | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Philadelphia Phillies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -106** / DraftKings -108 | — | +0.94 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +135** / FanDuel +134 | — | +1.35 |
| ✅ WIN | LEAN | San Diego Padres @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -154** / DraftKings -156 | — | +0.65 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Philadelphia Phillies | Run Line | Pittsburgh Pirates -1.5 | — | **DraftKings +156** / FanDuel +152 | — | +1.56 |
| ✅ WIN | LEAN | Los Angeles Angels @ Seattle Mariners | Total | Over 7.5 | 7.5 | **FanDuel -115** / DraftKings -119 | — | +0.87 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -105** / DraftKings -107 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -107** / FanDuel -114 | — | -1.00 |

### 2026-06-28 — 6-4  (+1.15u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -132** / DraftKings -136 | — | +0.76 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -184** / DraftKings -193 | — | +0.54 |
| ✅ WIN | PLAY | Texas Rangers @ Toronto Blue Jays | Moneyline | Texas Rangers ML | — | **FanDuel +114** / DraftKings +109 | — | +1.14 |
| ✅ WIN | PLAY | Miami Marlins @ St. Louis Cardinals | Total | Under 9.5 | 9.5 | **DraftKings -120** / FanDuel -124 | — | +0.83 |
| ✅ WIN | PLAY | Philadelphia Phillies @ New York Mets | Moneyline | Philadelphia Phillies ML | — | **FanDuel -144** / DraftKings -149 | — | +0.69 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **DraftKings +119** / FanDuel +116 | — | +1.19 |
| ❌ LOSS | PLAY | Kansas City Royals @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **DraftKings -137** / FanDuel -142 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ St. Louis Cardinals | Moneyline | Miami Marlins ML | — | **FanDuel +114** / DraftKings +109 | — | -1.00 |
| ❌ LOSS | PLAY | Kansas City Royals @ Chicago White Sox | Run Line | Chicago White Sox -1.5 | — | **FanDuel +146** / DraftKings +143 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Tampa Bay Rays | Total | Over 7.5 | 7.5 | **DraftKings -114** / FanDuel -118 | — | -1.00 |

### 2026-06-27 — 5-3  (+0.88u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Kansas City Royals @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -148** / DraftKings -148 | — | +0.68 |
| ✅ WIN | PLAY | Chicago Cubs @ Milwaukee Brewers | Total | Over 8.0 | 8.0 | **DraftKings -104** / FanDuel -112 | — | +0.96 |
| ✅ WIN | PLAY | Athletics @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **DraftKings -111** / FanDuel -112 | — | +0.90 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -205** / DraftKings -205 | — | +0.49 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -117** / FanDuel -118 | — | +0.85 |
| ❌ LOSS | PLAY | Chicago Cubs @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -164** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +125** / DraftKings +124 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel -138** / DraftKings -144 | — | -1.00 |

### 2026-06-26 — 5-5  (-0.14u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ✅ WIN | PLAY | Chicago Cubs @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings +101** / FanDuel +100 | — | +1.01 |
| ✅ WIN | PLAY | Philadelphia Phillies @ New York Mets | Moneyline | Philadelphia Phillies ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +158** / DraftKings +145 | — | +1.58 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Total | Over 7.5 | 7.5 | **DraftKings -110** / FanDuel -115 | — | +0.91 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -205** / FanDuel -210 | — | -1.00 |
| ❌ LOSS | PLAY | Athletics @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **FanDuel +108** / DraftKings +104 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ San Diego Padres | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -148** / DraftKings -148 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +112** / DraftKings +105 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ New York Mets | Run Line | Philadelphia Phillies -1.5 | — | **FanDuel +106** / DraftKings +102 | — | -1.00 |

### 2026-06-25 — 3-1  (+1.91u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +123** / FanDuel +122 | — | +1.23 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | **FanDuel -106** / DraftKings -108 | — | +0.94 |
| ✅ WIN | LEAN | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ❌ LOSS | PLAY | Athletics @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -130** / DraftKings -132 | — | -1.00 |

### 2026-06-24 — 3-3  (-0.69u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Dodgers @ Minnesota Twins | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -176** / DraftKings -181 | — | +0.57 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Baltimore Orioles @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ❌ LOSS | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -113** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Houston Astros @ Toronto Blue Jays | Moneyline | Toronto Blue Jays ML | — | **FanDuel -154** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Los Angeles Angels | Run Line | Los Angeles Angels -1.5 | — | **DraftKings +158** / FanDuel -194 | — | -1.00 |

### 2026-06-23 — 5-4  (+0.23u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 10.5 | 10.5 | **FanDuel -105** / DraftKings -105 | — | +0.95 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Minnesota Twins | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -176** / DraftKings -186 | — | +0.57 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | **FanDuel +100** / DraftKings -102 | — | +1.00 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Cincinnati Reds | Moneyline | Milwaukee Brewers ML | — | **DraftKings -114** / FanDuel -116 | — | +0.88 |
| ✅ WIN | LEAN | Athletics @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -120** / DraftKings -120 | — | +0.83 |
| ❌ LOSS | PLAY | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -184** / DraftKings -193 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +109** / FanDuel +108 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Washington Nationals | Moneyline | Washington Nationals ML | — | **DraftKings +143** / FanDuel +142 | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +116** / DraftKings +113 | — | -1.00 |

### 2026-06-22 — 5-4  (+0.10u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ Cincinnati Reds | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -142** / DraftKings -144 | — | +0.70 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Washington Nationals | Total | Under 10.0 | 10.0 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | LEAN | Texas Rangers @ Miami Marlins | Total | Under 8.5 | 8.5 | **FanDuel -114** / DraftKings -114 | — | +0.88 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Cincinnati Reds | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +102** / FanDuel +100 | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -188** / DraftKings -194 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ St. Louis Cardinals | Run Line | St. Louis Cardinals -1.5 | — | **FanDuel +146** / DraftKings +143 | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ San Diego Padres | Moneyline | Atlanta Braves ML | — | **FanDuel -106** / DraftKings -109 | — | -1.00 |

### 2026-06-21 — 3-4  (-1.02u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Minnesota Twins @ Arizona Diamondbacks | Moneyline | Minnesota Twins ML | — | **FanDuel +118** / DraftKings +109 | — | +1.18 |
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Moneyline | Los Angeles Angels ML | — | **FanDuel +108** / DraftKings +104 | — | +1.08 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -138** / DraftKings -149 | — | +0.72 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -108** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -105** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -104** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel +104** / DraftKings +104 | — | -1.00 |

### 2026-06-20 — 6-7  (-1.19u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Total | Under 9.5 | 9.5 | **FanDuel -105** / DraftKings -108 | — | +0.95 |
| ✅ WIN | PLAY | Minnesota Twins @ Arizona Diamondbacks | Moneyline | Minnesota Twins ML | — | **DraftKings +113** / FanDuel +110 | — | +1.13 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Colorado Rockies | Total | Under 10.5 | 10.5 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | LEAN | San Francisco Giants @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ✅ WIN | LEAN | Minnesota Twins @ Arizona Diamondbacks | Run Line | Minnesota Twins -1.5 | — | **DraftKings -180** / FanDuel -196 | — | +0.56 |
| ✅ WIN | LEAN | San Francisco Giants @ Miami Marlins | Run Line | Miami Marlins -1.5 | — | **FanDuel +152** / DraftKings +149 | — | +1.52 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -200** / DraftKings -205 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -126** / DraftKings -131 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -267** / FanDuel -270 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel +100** / DraftKings +100 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -122** / FanDuel -125 | — | -1.00 |
| ➖ PUSH | LEAN | Milwaukee Brewers @ Atlanta Braves | Total | Over 7.0 | 7.0 | **FanDuel -120** / DraftKings -122 | — | +0.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Texas Rangers | Moneyline | Texas Rangers ML | — | **FanDuel -134** / DraftKings -136 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -206** / FanDuel -210 | — | -1.00 |

### 2026-06-19 — 4-6  (-3.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -270** / DraftKings -286 | — | +0.37 |
| ✅ WIN | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -199** / FanDuel -200 | — | +0.50 |
| ✅ WIN | PLAY | San Francisco Giants @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -130** / DraftKings -131 | — | +0.77 |
| ✅ WIN | PLAY | Cincinnati Reds @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Athletics | Moneyline | Los Angeles Angels ML | — | **DraftKings +139** / FanDuel +134 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Athletics | Total | Under 10.0 | 10.0 | **DraftKings -112** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Tampa Bay Rays | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -103** / FanDuel -105 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -136** / DraftKings -143 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Athletics | Run Line | Los Angeles Angels -1.5 | — | **DraftKings -143** / FanDuel -152 | — | -1.00 |

### 2026-06-18 — 5-3  (+2.06u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -113** / FanDuel -120 | — | +0.88 |
| ✅ WIN | PLAY | Minnesota Twins @ Texas Rangers | Moneyline | Minnesota Twins ML | — | **FanDuel -124** / DraftKings -126 | — | +0.81 |
| ✅ WIN | PLAY | Toronto Blue Jays @ Boston Red Sox | Total | Under 9.0 | 9.0 | **DraftKings -108** / FanDuel -115 | — | +0.93 |
| ✅ WIN | LEAN | New York Mets @ Philadelphia Phillies | Moneyline | New York Mets ML | — | **FanDuel +104** / DraftKings +104 | — | +1.04 |
| ✅ WIN | LEAN | Minnesota Twins @ Texas Rangers | Run Line | Minnesota Twins -1.5 | — | **FanDuel +140** / DraftKings +130 | — | +1.40 |
| ❌ LOSS | PLAY | Chicago White Sox @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -158** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -146** / DraftKings -156 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +150** / FanDuel +146 | — | -1.00 |

### 2026-06-17 — 8-5  (+1.92u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ St. Louis Cardinals | Total | Under 10.5 | 10.5 | **DraftKings -102** / FanDuel -120 | — | +0.98 |
| ✅ WIN | PLAY | Los Angeles Angels @ Arizona Diamondbacks | Total | Under 9.5 | 9.5 | **DraftKings -102** / FanDuel -128 | — | +0.98 |
| ✅ WIN | PLAY | Chicago White Sox @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -184** / DraftKings -186 | — | +0.54 |
| ✅ WIN | PLAY | Chicago White Sox @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel +116** / DraftKings +113 | — | +1.16 |
| ✅ WIN | LEAN | Cleveland Guardians @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -112** / FanDuel -115 | — | +0.89 |
| ✅ WIN | LEAN | Miami Marlins @ Philadelphia Phillies | Moneyline | Miami Marlins ML | — | **DraftKings +103** / FanDuel +102 | — | +1.03 |
| ✅ WIN | LEAN | Colorado Rockies @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -188** / DraftKings -194 | — | +0.53 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Athletics | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -124** / DraftKings -125 | — | +0.81 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -154** / DraftKings -156 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **DraftKings +135** / FanDuel +132 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Chicago Cubs | Total | Under 10.0 | 10.0 | **FanDuel -106** / DraftKings -108 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Arizona Diamondbacks | Moneyline | Los Angeles Angels ML | — | **FanDuel +146** / DraftKings +141 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Athletics | Total | Under 10.0 | 10.0 | **FanDuel -104** / DraftKings -105 | — | -1.00 |

### 2026-06-16 — 4-6  (-2.26u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -118** / DraftKings -157 | — | +0.85 |
| ✅ WIN | LEAN | Kansas City Royals @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -118** / DraftKings -144 | — | +0.85 |
| ✅ WIN | LEAN | San Diego Padres @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -118** / DraftKings -120 | — | +0.85 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Athletics | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +119** / FanDuel -126 | — | +1.19 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -138** / DraftKings -171 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Total | Over 8.0 | 8.0 | **DraftKings -119** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | PLAY | Minnesota Twins @ Texas Rangers | Moneyline | Texas Rangers ML | — | **DraftKings -132** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +146** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +135** / FanDuel -205 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -180** / DraftKings -198 | — | -1.00 |

### 2026-06-15 — 3-2  (+0.29u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Kansas City Royals @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -118** / DraftKings -132 | — | +0.85 |
| ✅ WIN | LEAN | San Diego Padres @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -110** / DraftKings -157 | — | +0.91 |
| ✅ WIN | LEAN | Colorado Rockies @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -190** / DraftKings -219 | — | +0.53 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel -102** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | LEAN | Detroit Tigers @ Houston Astros | Total | Under 9.0 | 9.0 | **DraftKings -117** / FanDuel -118 | — | -1.00 |

### 2026-06-14 — 2-4  (-2.41u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel +102** / DraftKings -101 | — | +1.02 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings -175** / FanDuel -182 | — | +0.57 |
| ❌ LOSS | PLAY | St. Louis Cardinals @ Minnesota Twins | Moneyline | St. Louis Cardinals ML | — | **FanDuel -102** / DraftKings -103 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Chicago White Sox | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -193** / FanDuel -196 | — | -1.00 |
| ❌ LOSS | PLAY | Seattle Mariners @ Washington Nationals | Moneyline | Seattle Mariners ML | — | **DraftKings -144** / FanDuel -148 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Boston Red Sox | Total | Under 9.0 | 9.0 | **DraftKings -105** / FanDuel -110 | — | -1.00 |

### 2026-06-13 — 6-7  (-0.18u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Dodgers @ Chicago White Sox | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -205** / DraftKings -207 | — | +0.49 |
| ✅ WIN | PLAY | St. Louis Cardinals @ Minnesota Twins | Moneyline | St. Louis Cardinals ML | — | **FanDuel +100** / DraftKings -105 | — | +1.00 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Los Angeles Angels | Total | Over 6.5 | 6.5 | **DraftKings +289** / FanDuel -110 | — | +2.89 |
| ✅ WIN | LEAN | Arizona Diamondbacks @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings -105** / FanDuel -122 | — | +0.95 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Milwaukee Brewers | Total | Over 8.0 | 8.0 | **FanDuel -110** / DraftKings -115 | — | +0.91 |
| ✅ WIN | LEAN | Colorado Rockies @ Athletics | Moneyline | Athletics ML | — | **FanDuel -172** / DraftKings -175 | — | +0.58 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -142** / DraftKings -143 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Athletics | Total | Under 11.5 | 11.5 | **FanDuel -104** / DraftKings -127 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Baltimore Orioles | Total | Under 10.0 | 10.0 | **FanDuel -106** / DraftKings -107 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Baltimore Orioles | Total | Under 9.5 | 9.5 | **DraftKings -105** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Pittsburgh Pirates | Moneyline | Miami Marlins ML | — | **FanDuel +120** | — | -1.00 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +158** / DraftKings +157 | — | -1.00 |
| ❌ LOSS | LEAN | Houston Astros @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel -126** / DraftKings -126 | — | -1.00 |

### 2026-06-12 — 5-3  (+0.67u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -250** / DraftKings -251 | — | +0.40 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -108** / DraftKings -115 | — | +0.93 |
| ✅ WIN | LEAN | Arizona Diamondbacks @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **FanDuel -105** / DraftKings -107 | — | +0.95 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Los Angeles Angels | Total | Under 9.0 | 9.0 | **DraftKings -114** / FanDuel -120 | — | +0.88 |
| ✅ WIN | LEAN | Colorado Rockies @ Athletics | Moneyline | Athletics ML | — | **FanDuel -196** / DraftKings -198 | — | +0.51 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Chicago White Sox | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -149** / FanDuel -152 | — | -1.00 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **FanDuel -118** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -118** / DraftKings -120 | — | -1.00 |

### 2026-06-11 — 5-3  (+0.97u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Arizona Diamondbacks @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -112** / DraftKings -114 | — | +0.89 |
| ✅ WIN | PLAY | Texas Rangers @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -114** / FanDuel -120 | — | +0.88 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Pittsburgh Pirates | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Miami Marlins | Run Line | Miami Marlins -1.5 | — | **DraftKings -186** / FanDuel -188 | — | +0.54 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Pittsburgh Pirates | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +104** / DraftKings -101 | — | +1.04 |
| ❌ LOSS | PLAY | Chicago Cubs @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -103** / FanDuel -105 | — | -1.00 |
| ➖ PUSH | PLAY | St. Louis Cardinals @ New York Mets | Total | Under 9.0 | 9.0 | **FanDuel -115** / DraftKings -117 | — | +0.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +130** / DraftKings +123 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Detroit Tigers | Total | Under 9.5 | 9.5 | **DraftKings -114** / FanDuel -118 | — | -1.00 |

### 2026-06-10 — 4-6  (-2.55u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago Cubs @ Colorado Rockies | Total | Under 12.5 | 12.5 | **FanDuel -106** / DraftKings -117 | — | +0.94 |
| ✅ WIN | PLAY | Chicago Cubs @ Colorado Rockies | Total | Under 12.0 | 12.0 | **DraftKings -112** / FanDuel -114 | — | +0.89 |
| ✅ WIN | LEAN | Boston Red Sox @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -146** / DraftKings -156 | — | +0.68 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ Pittsburgh Pirates | Total | Over 8.0 | 8.0 | **FanDuel -106** / DraftKings -106 | — | +0.94 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Pittsburgh Pirates | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -196** / DraftKings -201 | — | -1.00 |
| ➖ PUSH | PLAY | Texas Rangers @ Kansas City Royals | Total | Under 10.0 | 10.0 | **FanDuel +112** / DraftKings -110 | — | +0.00 |
| ❌ LOSS | PLAY | Atlanta Braves @ Chicago White Sox | Total | Over 7.0 | 7.0 | **DraftKings -117** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Athletics | Moneyline | Milwaukee Brewers ML | — | **FanDuel -110** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ Pittsburgh Pirates | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -114** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ Chicago White Sox | Total | Over 7.5 | 7.5 | **DraftKings -106** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Colorado Rockies | Moneyline | Chicago Cubs ML | — | **FanDuel -166** / DraftKings -168 | — | -1.00 |

### 2026-06-09 — 5-0  (+4.44u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Baltimore Orioles | Moneyline | Seattle Mariners ML | — | **DraftKings -115** / FanDuel -116 | — | +0.87 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Toronto Blue Jays | Moneyline | Toronto Blue Jays ML | — | **FanDuel -110** / DraftKings -111 | — | +0.91 |
| ✅ WIN | PLAY | Texas Rangers @ Kansas City Royals | Total | Under 9.5 | 9.5 | **FanDuel -115** / DraftKings -121 | — | +0.87 |
| ✅ WIN | PLAY | Chicago Cubs @ Colorado Rockies | Total | Under 12.5 | 12.5 | **FanDuel -110** / DraftKings -114 | — | +0.91 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Athletics | Total | Under 13.0 | 13.0 | **DraftKings -113** / FanDuel -115 | — | +0.88 |

### 2026-06-08 — 3-5  (-2.27u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ Athletics | Moneyline | Milwaukee Brewers ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Seattle Mariners @ Baltimore Orioles | Moneyline | Seattle Mariners ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Houston Astros @ Los Angeles Angels | Moneyline | Houston Astros ML | — | — | — | +0.91 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Athletics | Total | Under 11.0 | 11.0 | — | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Tampa Bay Rays | Moneyline | Boston Red Sox ML | — | — | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Athletics | Run Line | Milwaukee Brewers -1.5 | — | — | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ San Francisco Giants | Total | Over 8.0 | 8.0 | — | — | -1.00 |
| ❌ LOSS | LEAN | Houston Astros @ Los Angeles Angels | Run Line | Houston Astros -1.5 | — | — | — | -1.00 |

### 2026-06-07 — 6-5  (+0.46u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Colorado Rockies | Moneyline | Milwaukee Brewers ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Cincinnati Reds @ St. Louis Cardinals | Run Line | St. Louis Cardinals -1.5 | — | — | — | +0.91 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | — | — | +0.91 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Colorado Rockies | Run Line | Milwaukee Brewers -1.5 | — | — | — | +0.91 |
| ✅ WIN | LEAN | Baltimore Orioles @ Toronto Blue Jays | Moneyline | Toronto Blue Jays ML | — | — | — | +0.91 |
| ❌ LOSS | PLAY | Chicago White Sox @ Philadelphia Phillies | Moneyline | Chicago White Sox ML | — | — | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Colorado Rockies | Total | Under 12.5 | 12.5 | — | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Arizona Diamondbacks | Moneyline | Washington Nationals ML | — | — | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Angels @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | — | — | -1.00 |
| ❌ LOSS | LEAN | San Francisco Giants @ Chicago Cubs | Total | Over 8.0 | 8.0 | — | — | -1.00 |

### 2026-06-06 — 9-1  (+7.19u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Chicago White Sox @ Philadelphia Phillies | Moneyline | Chicago White Sox ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Colorado Rockies | Total | Under 10.5 | 10.5 | — | — | +0.91 |
| ✅ WIN | PLAY | Seattle Mariners @ Detroit Tigers | Total | Under 9.0 | 9.0 | — | — | +0.91 |
| ✅ WIN | PLAY | Los Angeles Angels @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Colorado Rockies | Moneyline | Milwaukee Brewers ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Chicago White Sox @ Philadelphia Phillies | Run Line | Chicago White Sox -1.5 | — | — | — | +0.91 |
| ✅ WIN | LEAN | Los Angeles Angels @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | — | — | +0.91 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Colorado Rockies | Run Line | Milwaukee Brewers -1.5 | — | — | — | +0.91 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Toronto Blue Jays | Moneyline | Baltimore Orioles ML | — | — | — | -1.00 |

## Model B — picks by date

### 2026-08-06 — 4-4  (-1.55u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Cincinnati Reds | Moneyline | Cincinnati Reds ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Washington Nationals @ Philadelphia Phillies | Moneyline | Philadelphia Phillies ML | — | **FanDuel -335** / DraftKings -354 | — | +0.30 |
| ✅ WIN | PLAY | Chicago White Sox @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -184** / DraftKings -192 | — | +0.54 |
| ✅ WIN | LEAN | Los Angeles Angels @ Baltimore Orioles | Total | Under 10.0 | 10.0 | **DraftKings -104** / FanDuel -114 | — | +0.96 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **FanDuel -106** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago White Sox @ Boston Red Sox | Run Line | Boston Red Sox -1.5 | — | **FanDuel +116** / DraftKings +109 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **DraftKings -114** / FanDuel -116 | — | -1.00 |

### 2026-08-05 — 4-7  (-3.74u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -108** / FanDuel -110 | — | +0.93 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -130** / DraftKings -136 | — | +0.77 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -110 | — | +0.91 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Moneyline | Tampa Bay Rays ML | — | **FanDuel -154** / DraftKings -167 | — | +0.65 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -158** / DraftKings -169 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Arizona Diamondbacks | Moneyline | San Diego Padres ML | — | **FanDuel -112** / DraftKings -121 | — | -1.00 |
| ❌ LOSS | PLAY | Detroit Tigers @ Seattle Mariners | Moneyline | Detroit Tigers ML | — | **DraftKings +128** / FanDuel +124 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 7.0 | 7.0 | **DraftKings -117** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Run Line | Houston Astros -1.5 | — | **FanDuel +130** / DraftKings +118 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Arizona Diamondbacks | Total | Under 9.5 | 9.5 | **DraftKings +101** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | LEAN | New York Mets @ Cleveland Guardians | Total | Under 8.5 | 8.5 | **DraftKings -112** / FanDuel -115 | — | -1.00 |

### 2026-08-04 — 4-4  (-1.22u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Pittsburgh Pirates @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -167 | — | +0.65 |
| ✅ WIN | PLAY | Athletics @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings -106** / FanDuel -122 | — | +0.94 |
| ✅ WIN | PLAY | Washington Nationals @ Philadelphia Phillies | Moneyline | Philadelphia Phillies ML | — | **FanDuel -250** / DraftKings -263 | — | +0.40 |
| ✅ WIN | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -126** / DraftKings -131 | — | +0.79 |
| ❌ LOSS | PLAY | Minnesota Twins @ Kansas City Royals | Total | Under 9.5 | 9.5 | **DraftKings -105** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Texas Rangers | Moneyline | San Francisco Giants ML | — | **DraftKings +167** / FanDuel +166 | — | -1.00 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -108** / FanDuel -114 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Chicago Cubs | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -208** / FanDuel -210 | — | -1.00 |

### 2026-08-03 — 3-3  (-0.39u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Texas Rangers | Moneyline | San Francisco Giants ML | — | **FanDuel +100** / DraftKings -110 | — | +1.00 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Colorado Rockies | Moneyline | Tampa Bay Rays ML | — | **FanDuel -156** / DraftKings -166 | — | +0.64 |
| ✅ WIN | LEAN | San Diego Padres @ Arizona Diamondbacks | Total | Under 9.0 | 9.0 | **DraftKings -103** / FanDuel -115 | — | +0.97 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -115** / DraftKings -115 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -126** / DraftKings -136 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Milwaukee Brewers | Total | Over 8.5 | 8.5 | **FanDuel -104** / DraftKings -106 | — | -1.00 |

### 2026-08-02 — 8-2  (+5.66u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Texas Rangers @ Houston Astros | Moneyline | Houston Astros ML | — | **FanDuel -122** / DraftKings -126 | — | +0.82 |
| ✅ WIN | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 12.5 | 12.5 | **DraftKings -103** / FanDuel -110 | — | +0.97 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -106** / DraftKings -115 | — | +0.94 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Total | Under 11.5 | 11.5 | **DraftKings -112** / FanDuel -122 | — | +0.89 |
| ✅ WIN | PLAY | Texas Rangers @ Houston Astros | Run Line | Houston Astros -1.5 | — | **DraftKings +163** / FanDuel +160 | — | +1.63 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Baltimore Orioles | Moneyline | Philadelphia Phillies ML | — | **FanDuel -128** / DraftKings -137 | — | +0.78 |
| ✅ WIN | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -138** / DraftKings -150 | — | +0.72 |
| ✅ WIN | LEAN | Kansas City Royals @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel -110** / DraftKings -114 | — | +0.91 |
| ❌ LOSS | PLAY | New York Yankees @ Chicago Cubs | Total | Over 6.5 | 6.5 | **DraftKings -111** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Houston Astros | Total | Under 9.0 | 9.0 | **DraftKings +101** / FanDuel -120 | — | -1.00 |

### 2026-08-01 — 7-4  (+1.52u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | New York Yankees @ Chicago Cubs | Total | Over 6.5 | 6.5 | **DraftKings +100** / FanDuel -104 | — | +1.00 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -132** / DraftKings -137 | — | +0.76 |
| ✅ WIN | PLAY | Miami Marlins @ New York Mets | Total | Under 9.0 | 9.0 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -114** / DraftKings -123 | — | +0.88 |
| ✅ WIN | PLAY | Washington Nationals @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -184** / DraftKings -197 | — | +0.54 |
| ✅ WIN | PLAY | Philadelphia Phillies @ Baltimore Orioles | Moneyline | Philadelphia Phillies ML | — | **FanDuel -138** / DraftKings -148 | — | +0.72 |
| ✅ WIN | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -134** / DraftKings -136 | — | +0.75 |
| ❌ LOSS | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 12.0 | 12.0 | **DraftKings -115** / FanDuel -118 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -161 | — | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +138** / DraftKings +131 | — | -1.00 |
| ❌ LOSS | LEAN | Detroit Tigers @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel +100** / DraftKings +100 | — | -1.00 |

### 2026-07-31 — 6-6  (-0.99u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Kansas City Royals @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -107** / FanDuel -120 | — | +0.93 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Moneyline | Detroit Tigers ML | — | **FanDuel -154** / DraftKings -163 | — | +0.65 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -120 | — | +0.85 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Los Angeles Angels | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -171 | — | +0.62 |
| ✅ WIN | PLAY | Detroit Tigers @ Athletics | Run Line | Detroit Tigers -1.5 | — | **FanDuel +100** / DraftKings -105 | — | +1.00 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Los Angeles Angels | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -126** / DraftKings -135 | — | -1.00 |
| ❌ LOSS | PLAY | Detroit Tigers @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel +100** / DraftKings +100 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | — | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +136** / DraftKings +128 | — | -1.00 |
| ❌ LOSS | LEAN | Boston Red Sox @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | — | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Colorado Rockies | Moneyline | Kansas City Royals ML | — | **FanDuel -108** / DraftKings -111 | — | -1.00 |

### 2026-07-30 — 5-4  (+0.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel +102** / DraftKings +100 | — | +1.02 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -108** / FanDuel -110 | — | +0.93 |
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -156** / FanDuel -162 | — | +0.64 |
| ✅ WIN | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -144** / DraftKings -150 | — | +0.69 |
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings +135** / FanDuel +134 | — | +1.35 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -112** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Cincinnati Reds | Run Line | Pittsburgh Pirates -1.5 | — | **DraftKings +135** / FanDuel +134 | — | -1.00 |
| ❌ LOSS | LEAN | Texas Rangers @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +160** / DraftKings +153 | — | -1.00 |
| ❌ LOSS | LEAN | San Francisco Giants @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -124** / DraftKings -131 | — | -1.00 |

### 2026-07-29 — 5-7  (-3.11u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -144** / DraftKings -150 | — | +0.69 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 10.5 | 10.5 | **FanDuel -102** / DraftKings -106 | — | +0.98 |
| ✅ WIN | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -138** / DraftKings -143 | — | +0.72 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -154** / DraftKings -156 | — | +0.65 |
| ✅ WIN | LEAN | Seattle Mariners @ Los Angeles Dodgers | Total | Under 9.5 | 9.5 | **DraftKings -117** / FanDuel -122 | — | +0.85 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -174** / DraftKings -180 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel -116** / DraftKings -127 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +140** / DraftKings +138 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ St. Louis Cardinals | Run Line | Chicago Cubs -1.5 | — | **FanDuel +146** / DraftKings +131 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -129** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel +106** / DraftKings +102 | — | -1.00 |

### 2026-07-28 — 10-6  (+2.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago Cubs @ St. Louis Cardinals | Moneyline | Chicago Cubs ML | — | **FanDuel -112** / DraftKings -115 | — | +0.89 |
| ✅ WIN | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -143 | — | +0.75 |
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Total | Under 9.5 | 9.5 | **FanDuel -102** / DraftKings -108 | — | +0.98 |
| ✅ WIN | PLAY | Milwaukee Brewers @ San Francisco Giants | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +130** / DraftKings +124 | — | +1.30 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -110** / DraftKings -117 | — | +0.91 |
| ✅ WIN | LEAN | Colorado Rockies @ San Diego Padres | Moneyline | San Diego Padres ML | — | **FanDuel -180** / DraftKings -191 | — | +0.56 |
| ✅ WIN | LEAN | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -136** / DraftKings -144 | — | +0.74 |
| ✅ WIN | LEAN | Kansas City Royals @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | LEAN | Kansas City Royals @ Minnesota Twins | Total | Under 9.5 | 9.5 | **DraftKings -103** / FanDuel -124 | — | +0.97 |
| ✅ WIN | LEAN | Cleveland Guardians @ Cincinnati Reds | Total | Under 9.0 | 9.0 | **FanDuel -110** / DraftKings -113 | — | +0.91 |
| ❌ LOSS | PLAY | Texas Rangers @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **DraftKings -175** / FanDuel -178 | — | -1.00 |
| ❌ LOSS | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -144** / DraftKings -155 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Detroit Tigers | Total | Under 9.5 | 9.5 | **DraftKings -103** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -184** / DraftKings -192 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -110** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Miami Marlins | Run Line | Miami Marlins -1.5 | — | **DraftKings -194** / FanDuel -196 | — | -1.00 |

### 2026-07-27 — 3-4  (-1.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Boston Red Sox @ Athletics | Moneyline | Boston Red Sox ML | — | **FanDuel -168** / DraftKings -182 | — | +0.60 |
| ✅ WIN | LEAN | Arizona Diamondbacks @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -116** / DraftKings -123 | — | +0.86 |
| ✅ WIN | LEAN | Boston Red Sox @ Athletics | Total | Under 9.5 | 9.5 | **DraftKings -110** / FanDuel -110 | — | +0.91 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ San Francisco Giants | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -137 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -130** / DraftKings -131 | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ New York Mets | Moneyline | Atlanta Braves ML | — | **DraftKings -115** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | LEAN | Toronto Blue Jays @ Washington Nationals | Run Line | Washington Nationals -1.5 | — | **FanDuel +155** / DraftKings +143 | — | -1.00 |

### 2026-07-26 — 6-2  (+2.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -142** / DraftKings -143 | — | +0.70 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -320** / DraftKings -340 | — | +0.31 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **FanDuel -114** / DraftKings -118 | — | +0.88 |
| ✅ WIN | PLAY | Atlanta Braves @ Baltimore Orioles | Moneyline | Atlanta Braves ML | — | **FanDuel -104** / DraftKings -106 | — | +0.96 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -144** / DraftKings -149 | — | +0.69 |
| ✅ WIN | LEAN | Cincinnati Reds @ St. Louis Cardinals | Total | Under 9.0 | 9.0 | **DraftKings -101** / FanDuel -122 | — | +0.99 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ New York Mets | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -172 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Texas Rangers | Moneyline | Texas Rangers ML | — | **FanDuel -110** / DraftKings -111 | — | -1.00 |

### 2026-07-25 — 6-2  (+3.30u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -134** / DraftKings -134 | — | +0.75 |
| ✅ WIN | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -215** / DraftKings -228 | — | +0.47 |
| ✅ WIN | PLAY | Athletics @ Minnesota Twins | Total | Under 10.5 | 10.5 | **FanDuel -110** / DraftKings -114 | — | +0.91 |
| ✅ WIN | PLAY | Cleveland Guardians @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +168** / DraftKings +159 | — | +1.68 |
| ✅ WIN | LEAN | Colorado Rockies @ Milwaukee Brewers | Total | Over 8.5 | 8.5 | **DraftKings -114** / FanDuel -115 | — | +0.88 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ New York Mets | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -163** / FanDuel -164 | — | +0.61 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -112** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -132** / DraftKings -136 | — | -1.00 |

### 2026-07-24 — 3-3  (+0.43u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Atlanta Braves @ Baltimore Orioles | Moneyline | Atlanta Braves ML | — | **FanDuel +100** / DraftKings -101 | — | +1.00 |
| ✅ WIN | LEAN | Cleveland Guardians @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -134** / DraftKings -142 | — | +0.75 |
| ✅ WIN | LEAN | Cleveland Guardians @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +168** / DraftKings +153 | — | +1.68 |
| ❌ LOSS | PLAY | Colorado Rockies @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -240** / DraftKings -258 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel -108** / DraftKings -115 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |

### 2026-07-23 — 1-2  (-1.57u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -235** / DraftKings -249 | — | +0.43 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **DraftKings -107** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -110** / DraftKings -123 | — | -1.00 |

### 2026-07-22 — 5-1  (+3.95u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Washington Nationals @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -104** / DraftKings -110 | — | +0.96 |
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -118** / DraftKings -120 | — | +0.85 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Philadelphia Phillies | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -112** / DraftKings -120 | — | +0.89 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ Philadelphia Phillies | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +138** / DraftKings +129 | — | +1.38 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -144** / DraftKings -147 | — | -1.00 |

### 2026-07-21 — 2-5  (-2.59u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Tampa Bay Rays @ Toronto Blue Jays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -112** / DraftKings -115 | — | +0.89 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Toronto Blue Jays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +152** / DraftKings +149 | — | +1.52 |
| ❌ LOSS | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -144** / DraftKings -149 | — | -1.00 |
| ❌ LOSS | PLAY | New York Mets @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -142** / DraftKings -149 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Colorado Rockies | Total | Under 13.0 | 13.0 | **FanDuel +100** / DraftKings -113 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +140** / DraftKings +138 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Colorado Rockies | Moneyline | Washington Nationals ML | — | **FanDuel -102** / DraftKings -106 | — | -1.00 |

### 2026-07-20 — 7-3  (+3.38u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -115** / FanDuel -118 | — | +0.87 |
| ✅ WIN | PLAY | San Diego Padres @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -144** / DraftKings -144 | — | +0.69 |
| ✅ WIN | PLAY | Chicago White Sox @ Texas Rangers | Moneyline | Chicago White Sox ML | — | **DraftKings +144** / FanDuel +142 | — | +1.44 |
| ✅ WIN | PLAY | New York Mets @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -198** / DraftKings -199 | — | +0.51 |
| ✅ WIN | PLAY | Washington Nationals @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -102** / DraftKings -114 | — | +0.98 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **DraftKings -120** / FanDuel -124 | — | +0.83 |
| ✅ WIN | LEAN | New York Mets @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +106** / DraftKings +100 | — | +1.06 |
| ❌ LOSS | PLAY | Detroit Tigers @ Chicago Cubs | Total | Under 12.0 | 12.0 | **DraftKings -111** / FanDuel -112 | — | -1.00 |
| ❌ LOSS | LEAN | Athletics @ Arizona Diamondbacks | Moneyline | Arizona Diamondbacks ML | — | **FanDuel -162** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +142** / DraftKings +131 | — | -1.00 |

### 2026-07-19 — 8-6  (+1.32u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel +104** / DraftKings +100 | — | +1.04 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Cleveland Guardians | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -124** / DraftKings -131 | — | +0.81 |
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -156** / DraftKings -163 | — | +0.64 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Cleveland Guardians | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +146** / DraftKings +139 | — | +1.46 |
| ✅ WIN | LEAN | Minnesota Twins @ Chicago Cubs | Total | Over 8.0 | 8.0 | **FanDuel -102** / DraftKings -110 | — | +0.98 |
| ✅ WIN | LEAN | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel -130** / DraftKings -143 | — | +0.77 |
| ✅ WIN | LEAN | Minnesota Twins @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -162** / DraftKings -169 | — | +0.62 |
| ✅ WIN | LEAN | New York Mets @ Philadelphia Phillies | Total | Under 9.0 | 9.0 | **FanDuel +100** / DraftKings -119 | — | +1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -108** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ New York Yankees | Total | Over 7.5 | 7.5 | **FanDuel -110** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **DraftKings -131** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -105** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Cincinnati Reds @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Arizona Diamondbacks | Total | Under 9.0 | 9.0 | **FanDuel -112** / DraftKings -112 | — | -1.00 |

### 2026-07-18 — 4-8  (-4.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel +100** / DraftKings -102 | — | +1.00 |
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings +100** / FanDuel -104 | — | +1.00 |
| ✅ WIN | PLAY | San Diego Padres @ Kansas City Royals | Run Line | Kansas City Royals -1.5 | — | **FanDuel -156** / DraftKings -163 | — | +0.64 |
| ✅ WIN | LEAN | Tampa Bay Rays @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -120** / DraftKings -120 | — | +0.83 |
| ➖ PUSH | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 13.0 | 13.0 | **FanDuel -106** / DraftKings -115 | — | +0.00 |
| ❌ LOSS | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -112** / DraftKings -117 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel +110** / DraftKings +108 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Seattle Mariners | Moneyline | San Francisco Giants ML | — | **FanDuel +116** / DraftKings +112 | — | -1.00 |
| ❌ LOSS | PLAY | Texas Rangers @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel -192** / DraftKings -192 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Chicago Cubs | Moneyline | Minnesota Twins ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Cleveland Guardians | Moneyline | Pittsburgh Pirates ML | — | **FanDuel +108** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | LEAN | Tampa Bay Rays @ Boston Red Sox | Total | Under 9.5 | 9.5 | **FanDuel -110** / DraftKings -111 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -106** / FanDuel -110 | — | -1.00 |

### 2026-07-17 — 4-2  (+1.01u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Colorado Rockies | Total | Under 12.0 | 12.0 | **DraftKings -111** / FanDuel -114 | — | +0.90 |
| ✅ WIN | PLAY | Washington Nationals @ Athletics | Moneyline | Washington Nationals ML | — | **FanDuel -104** / DraftKings -108 | — | +0.96 |
| ✅ WIN | PLAY | Texas Rangers @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -215** / DraftKings -217 | — | +0.47 |
| ✅ WIN | LEAN | Miami Marlins @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -146** / DraftKings -149 | — | +0.68 |
| ❌ LOSS | PLAY | San Diego Padres @ Kansas City Royals | Total | Under 10.0 | 10.0 | **DraftKings -103** / FanDuel -104 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Athletics | Total | Under 10.0 | 10.0 | **DraftKings -108** / FanDuel -110 | — | -1.00 |

### 2026-07-16 — 1-0  (+0.96u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | New York Mets @ Philadelphia Phillies | Total | Under 9.5 | 9.5 | **FanDuel -104** / DraftKings -109 | — | +0.96 |

### 2026-07-12 — 4-3  (+0.51u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ Pittsburgh Pirates | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -122 | — | +0.87 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel -120** / DraftKings -126 | — | +0.83 |
| ✅ WIN | LEAN | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **DraftKings +113** / FanDuel +110 | — | +1.13 |
| ✅ WIN | LEAN | Kansas City Royals @ Baltimore Orioles | Moneyline | Baltimore Orioles ML | — | **FanDuel -148** / DraftKings -155 | — | +0.68 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -219** / FanDuel -225 | — | -1.00 |
| ❌ LOSS | PLAY | Seattle Mariners @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -130** / DraftKings -136 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -112** / DraftKings -112 | — | -1.00 |

### 2026-07-11 — 4-7  (-3.30u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ✅ WIN | LEAN | Seattle Mariners @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -108** / DraftKings -114 | — | +0.93 |
| ✅ WIN | LEAN | New York Yankees @ Washington Nationals | Moneyline | New York Yankees ML | — | **FanDuel -190** / DraftKings -199 | — | +0.53 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel +128** | — | +1.28 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **FanDuel -116** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -260** / DraftKings -287 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Pittsburgh Pirates | Moneyline | Milwaukee Brewers ML | — | **DraftKings -125** / FanDuel -130 | — | -1.00 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Run Line | Atlanta Braves -1.5 | — | **FanDuel +142** / DraftKings +139 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -122** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel +120** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | Colorado Rockies ML | — | **DraftKings +130** / FanDuel +124 | — | -1.00 |

### 2026-07-10 — 3-7  (-4.53u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Philadelphia Phillies @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ✅ WIN | LEAN | Boston Red Sox @ New York Mets | Moneyline | Boston Red Sox ML | — | **FanDuel +104** / DraftKings +104 | — | +1.04 |
| ✅ WIN | LEAN | Athletics @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -166** / DraftKings -175 | — | +0.60 |
| ❌ LOSS | PLAY | Atlanta Braves @ St. Louis Cardinals | Moneyline | Atlanta Braves ML | — | **FanDuel -164** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Arizona Diamondbacks @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -255** / DraftKings -272 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Cincinnati Reds | Moneyline | Chicago Cubs ML | — | **FanDuel -110** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -114** / DraftKings -120 | — | -1.00 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -118** / DraftKings -119 | — | -1.00 |
| ❌ LOSS | LEAN | Chicago Cubs @ Cincinnati Reds | Run Line | Chicago Cubs -1.5 | — | **DraftKings +142** / FanDuel +140 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **DraftKings -163** / FanDuel -166 | — | -1.00 |

### 2026-07-09 — 3-2  (+0.39u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **DraftKings -137** / FanDuel -138 | — | +0.73 |
| ✅ WIN | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -130** / DraftKings -136 | — | +0.77 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings -112** / FanDuel -118 | — | +0.89 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel +114** / DraftKings +108 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ San Francisco Giants | Moneyline | Colorado Rockies ML | — | — | — | -1.00 |

### 2026-07-08 — 4-1  (+2.57u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Moneyline | Detroit Tigers ML | — | **FanDuel -158** / DraftKings -163 | — | +0.63 |
| ✅ WIN | PLAY | Athletics @ Detroit Tigers | Run Line | Detroit Tigers -1.5 | — | **FanDuel +128** / DraftKings +128 | — | +1.28 |
| ✅ WIN | LEAN | Kansas City Royals @ New York Mets | Moneyline | New York Mets ML | — | — | — | +0.91 |
| ✅ WIN | LEAN | Houston Astros @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -134** / DraftKings -136 | — | +0.75 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -134** / DraftKings -143 | — | -1.00 |

### 2026-07-07 — 1-2  (-1.13u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Total | Over 7.5 | 7.5 | **DraftKings -115** / FanDuel -122 | — | +0.87 |
| ❌ LOSS | PLAY | Colorado Rockies @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -250** / DraftKings -272 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -126** / DraftKings -130 | — | -1.00 |

### 2026-07-06 — 2-3  (-1.64u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Colorado Rockies @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -230** / DraftKings -238 | — | +0.43 |
| ✅ WIN | PLAY | Milwaukee Brewers @ St. Louis Cardinals | Moneyline | Milwaukee Brewers ML | — | **FanDuel -108** / DraftKings -109 | — | +0.93 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Moneyline | Philadelphia Phillies ML | — | **FanDuel -200** / DraftKings -205 | — | -1.00 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Run Line | Philadelphia Phillies -1.5 | — | **DraftKings -125** / FanDuel -128 | — | -1.00 |
| ❌ LOSS | LEAN | Milwaukee Brewers @ St. Louis Cardinals | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +158** / DraftKings +148 | — | -1.00 |

### 2026-07-05 — 2-5  (-3.03u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | St. Louis Cardinals @ Chicago Cubs | Total | Over 8.0 | 8.0 | **DraftKings -110** / FanDuel -110 | — | +0.91 |
| ✅ WIN | LEAN | San Francisco Giants @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +106** / DraftKings +104 | — | +1.06 |
| ❌ LOSS | PLAY | Philadelphia Phillies @ Kansas City Royals | Moneyline | Philadelphia Phillies ML | — | **FanDuel -136** / DraftKings -143 | — | -1.00 |
| ➖ PUSH | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 13.0 | 13.0 | **DraftKings -111** / FanDuel -118 | — | +0.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -220** / DraftKings -225 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -108** / DraftKings -109 | — | -1.00 |
| ❌ LOSS | LEAN | Miami Marlins @ Athletics | Total | Under 9.5 | 9.5 | **DraftKings -110** / FanDuel -112 | — | -1.00 |
| ❌ LOSS | LEAN | New York Mets @ Atlanta Braves | Total | Under 9.0 | 9.0 | **DraftKings -108** / FanDuel -110 | — | -1.00 |

### 2026-07-04 — 7-4  (+1.54u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel +100** / DraftKings -105 | — | +1.00 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Moneyline | Miami Marlins ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -240** / DraftKings -252 | — | +0.42 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -113 | — | +0.91 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -117** / FanDuel -120 | — | +0.85 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Washington Nationals | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -164** / DraftKings -167 | — | +0.61 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -109** / FanDuel -114 | — | +0.92 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Moneyline | Milwaukee Brewers ML | — | **FanDuel -148** / DraftKings -155 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Cincinnati Reds | Total | Under 9.5 | 9.5 | **DraftKings +102** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +108** / DraftKings +108 | — | -1.00 |
| ❌ LOSS | LEAN | San Francisco Giants @ Colorado Rockies | Moneyline | Colorado Rockies ML | — | **FanDuel +110** / DraftKings +109 | — | -1.00 |

### 2026-07-03 — 7-3  (+2.63u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Houston Astros | Moneyline | Tampa Bay Rays ML | — | **FanDuel -108** / DraftKings -112 | — | +0.93 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Moneyline | Miami Marlins ML | — | **FanDuel +108** / DraftKings +104 | — | +1.08 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -245** / DraftKings -253 | — | +0.41 |
| ✅ WIN | PLAY | New York Mets @ Atlanta Braves | Total | Under 9.5 | 9.5 | **DraftKings -101** / FanDuel -124 | — | +0.99 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Arizona Diamondbacks | Moneyline | Milwaukee Brewers ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | PLAY | Miami Marlins @ Athletics | Run Line | Miami Marlins -1.5 | — | **DraftKings -182** / FanDuel -188 | — | +0.55 |
| ✅ WIN | LEAN | Milwaukee Brewers @ Arizona Diamondbacks | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +105** / DraftKings +100 | — | +1.05 |
| ❌ LOSS | PLAY | San Francisco Giants @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -112** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -107** / FanDuel -114 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel -113** / DraftKings -117 | — | -1.00 |

### 2026-07-02 — 4-4  (-0.64u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -118** / DraftKings -126 | — | +0.85 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -109** / FanDuel -110 | — | +0.92 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -198** / DraftKings -198 | — | +0.51 |
| ✅ WIN | PLAY | San Diego Padres @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings +108** / FanDuel +106 | — | +1.08 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -196** / DraftKings -198 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **FanDuel -120** / DraftKings -126 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -106** / DraftKings -112 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +122** / DraftKings +119 | — | -1.00 |

### 2026-07-01 — 9-5  (+3.08u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -132** / DraftKings -136 | — | +0.76 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -110** / FanDuel -114 | — | +0.91 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -168** / DraftKings -168 | — | +0.60 |
| ✅ WIN | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -117** / FanDuel -120 | — | +0.85 |
| ✅ WIN | PLAY | Detroit Tigers @ New York Yankees | Total | Under 9.5 | 9.5 | **FanDuel -112** / DraftKings -112 | — | +0.89 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -102** / FanDuel -114 | — | +0.98 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +128** / FanDuel +120 | — | +1.28 |
| ✅ WIN | LEAN | St. Louis Cardinals @ Atlanta Braves | Total | Under 9.0 | 9.0 | **FanDuel -102** / DraftKings -107 | — | +0.98 |
| ✅ WIN | LEAN | San Diego Padres @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -120** / DraftKings -126 | — | +0.83 |
| ❌ LOSS | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 12.0 | 12.0 | **FanDuel -110** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **FanDuel -154** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Washington Nationals @ Boston Red Sox | Total | Under 9.5 | 9.5 | **FanDuel -106** / DraftKings -107 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Philadelphia Phillies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel +116** / DraftKings +113 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Run Line | Miami Marlins -1.5 | — | **FanDuel -105** / DraftKings -107 | — | -1.00 |

### 2026-06-30 — 8-5  (+1.77u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago White Sox @ Baltimore Orioles | Moneyline | Chicago White Sox ML | — | **DraftKings +119** / FanDuel +118 | — | +1.19 |
| ✅ WIN | PLAY | Tampa Bay Rays @ Kansas City Royals | Moneyline | Tampa Bay Rays ML | — | **FanDuel -124** / DraftKings -132 | — | +0.81 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -172** / DraftKings -180 | — | +0.58 |
| ✅ WIN | PLAY | Miami Marlins @ Colorado Rockies | Moneyline | Miami Marlins ML | — | **DraftKings -156** / FanDuel -162 | — | +0.64 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Athletics | Run Line | Los Angeles Dodgers -1.5 | — | **FanDuel +104** / DraftKings -103 | — | +1.04 |
| ✅ WIN | LEAN | Washington Nationals @ Boston Red Sox | Total | Under 9.5 | 9.5 | **DraftKings +102** / FanDuel -115 | — | +1.02 |
| ✅ WIN | LEAN | Texas Rangers @ Cleveland Guardians | Moneyline | Texas Rangers ML | — | **DraftKings -119** / FanDuel -120 | — | +0.84 |
| ❌ LOSS | PLAY | Tampa Bay Rays @ Kansas City Royals | Total | Under 10.5 | 10.5 | **DraftKings -104** / FanDuel -120 | — | -1.00 |
| ❌ LOSS | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 11.5 | 11.5 | **DraftKings -101** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.5 | 11.5 | **DraftKings -118** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Athletics | Total | Under 11.0 | 11.0 | **DraftKings -121** / FanDuel -122 | — | -1.00 |
| ❌ LOSS | LEAN | Minnesota Twins @ Houston Astros | Moneyline | Minnesota Twins ML | — | **DraftKings -115** / FanDuel -116 | — | -1.00 |

### 2026-06-29 — 10-2  (+7.64u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Chicago White Sox @ Baltimore Orioles | Moneyline | Chicago White Sox ML | — | **FanDuel +114** / DraftKings +114 | — | +1.14 |
| ✅ WIN | PLAY | Washington Nationals @ Boston Red Sox | Moneyline | Boston Red Sox ML | — | **FanDuel -168** / DraftKings -175 | — | +0.60 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -152** / DraftKings -156 | — | +0.66 |
| ✅ WIN | PLAY | San Diego Padres @ Chicago Cubs | Total | Under 11.0 | 11.0 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Philadelphia Phillies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -106** / DraftKings -108 | — | +0.94 |
| ✅ WIN | PLAY | Cincinnati Reds @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +135** / FanDuel +134 | — | +1.35 |
| ✅ WIN | LEAN | San Diego Padres @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -154** / DraftKings -156 | — | +0.65 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Philadelphia Phillies | Run Line | Pittsburgh Pirates -1.5 | — | **DraftKings +156** / FanDuel +152 | — | +1.56 |
| ✅ WIN | LEAN | New York Mets @ Toronto Blue Jays | Total | Under 9.0 | 9.0 | **FanDuel -104** / DraftKings -120 | — | +0.96 |
| ✅ WIN | LEAN | Los Angeles Angels @ Seattle Mariners | Total | Over 7.5 | 7.5 | **FanDuel -115** / DraftKings -119 | — | +0.87 |
| ❌ LOSS | PLAY | Miami Marlins @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -105** / DraftKings -107 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Dodgers @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -107** / FanDuel -114 | — | -1.00 |

### 2026-06-28 — 6-3  (+2.15u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -132** / DraftKings -136 | — | +0.76 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -184** / DraftKings -193 | — | +0.54 |
| ✅ WIN | PLAY | Miami Marlins @ St. Louis Cardinals | Total | Under 9.5 | 9.5 | **DraftKings -120** / FanDuel -124 | — | +0.83 |
| ✅ WIN | PLAY | Texas Rangers @ Toronto Blue Jays | Moneyline | Texas Rangers ML | — | **FanDuel +114** / DraftKings +109 | — | +1.14 |
| ✅ WIN | PLAY | Philadelphia Phillies @ New York Mets | Moneyline | Philadelphia Phillies ML | — | **FanDuel -144** / DraftKings -149 | — | +0.69 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **DraftKings +119** / FanDuel +116 | — | +1.19 |
| ❌ LOSS | PLAY | Kansas City Royals @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **DraftKings -137** / FanDuel -142 | — | -1.00 |
| ❌ LOSS | PLAY | Miami Marlins @ St. Louis Cardinals | Moneyline | Miami Marlins ML | — | **FanDuel +114** / DraftKings +109 | — | -1.00 |
| ❌ LOSS | PLAY | Kansas City Royals @ Chicago White Sox | Run Line | Chicago White Sox -1.5 | — | **FanDuel +146** / DraftKings +143 | — | -1.00 |

### 2026-06-27 — 5-3  (+0.88u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Kansas City Royals @ Chicago White Sox | Moneyline | Chicago White Sox ML | — | **FanDuel -148** / DraftKings -148 | — | +0.68 |
| ✅ WIN | PLAY | Athletics @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **DraftKings -111** / FanDuel -112 | — | +0.90 |
| ✅ WIN | PLAY | Chicago Cubs @ Milwaukee Brewers | Total | Over 8.0 | 8.0 | **DraftKings -104** / FanDuel -112 | — | +0.96 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -205** / DraftKings -205 | — | +0.49 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -117** / FanDuel -118 | — | +0.85 |
| ❌ LOSS | PLAY | Chicago Cubs @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -164** / DraftKings -168 | — | -1.00 |
| ❌ LOSS | PLAY | Chicago Cubs @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **FanDuel +125** / DraftKings +124 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Minnesota Twins | Moneyline | Minnesota Twins ML | — | **FanDuel -138** / DraftKings -144 | — | -1.00 |

### 2026-06-26 — 5-4  (+0.86u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ✅ WIN | PLAY | Chicago Cubs @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings +101** / FanDuel +100 | — | +1.01 |
| ✅ WIN | PLAY | Philadelphia Phillies @ New York Mets | Moneyline | Philadelphia Phillies ML | — | **FanDuel -162** / DraftKings -163 | — | +0.62 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +158** / DraftKings +145 | — | +1.58 |
| ✅ WIN | LEAN | Los Angeles Dodgers @ San Diego Padres | Total | Over 7.5 | 7.5 | **DraftKings -110** / FanDuel -115 | — | +0.91 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -205** / FanDuel -210 | — | -1.00 |
| ❌ LOSS | PLAY | Athletics @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **FanDuel +108** / DraftKings +104 | — | -1.00 |
| ❌ LOSS | PLAY | Los Angeles Dodgers @ San Diego Padres | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -148** / DraftKings -148 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ Pittsburgh Pirates | Run Line | Pittsburgh Pirates -1.5 | — | **FanDuel +112** / DraftKings +105 | — | -1.00 |

### 2026-06-25 — 3-1  (+1.91u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Seattle Mariners @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +123** / FanDuel +122 | — | +1.23 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | **FanDuel -106** / DraftKings -108 | — | +0.94 |
| ✅ WIN | LEAN | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ❌ LOSS | PLAY | Athletics @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -130** / DraftKings -132 | — | -1.00 |

### 2026-06-24 — 3-3  (-0.69u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Dodgers @ Minnesota Twins | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -176** / DraftKings -181 | — | +0.57 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | — | — | +0.91 |
| ✅ WIN | PLAY | Baltimore Orioles @ Los Angeles Angels | Moneyline | Los Angeles Angels ML | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ❌ LOSS | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 11.0 | 11.0 | **DraftKings -113** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Houston Astros @ Toronto Blue Jays | Moneyline | Toronto Blue Jays ML | — | **FanDuel -154** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | LEAN | Baltimore Orioles @ Los Angeles Angels | Run Line | Los Angeles Angels -1.5 | — | **DraftKings +158** / FanDuel -194 | — | -1.00 |

### 2026-06-23 — 5-4  (+0.23u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 10.5 | 10.5 | **FanDuel -105** / DraftKings -105 | — | +0.95 |
| ✅ WIN | PLAY | Los Angeles Dodgers @ Minnesota Twins | Moneyline | Los Angeles Dodgers ML | — | **FanDuel -176** / DraftKings -186 | — | +0.57 |
| ✅ WIN | PLAY | Chicago Cubs @ New York Mets | Moneyline | Chicago Cubs ML | — | **FanDuel +100** / DraftKings -102 | — | +1.00 |
| ✅ WIN | PLAY | Milwaukee Brewers @ Cincinnati Reds | Moneyline | Milwaukee Brewers ML | — | **DraftKings -114** / FanDuel -116 | — | +0.88 |
| ✅ WIN | LEAN | Athletics @ San Francisco Giants | Moneyline | San Francisco Giants ML | — | **FanDuel -120** / DraftKings -120 | — | +0.83 |
| ❌ LOSS | PLAY | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -184** / DraftKings -193 | — | -1.00 |
| ❌ LOSS | LEAN | Seattle Mariners @ Pittsburgh Pirates | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +109** / FanDuel +108 | — | -1.00 |
| ❌ LOSS | LEAN | Philadelphia Phillies @ Washington Nationals | Moneyline | Washington Nationals ML | — | **DraftKings +143** / FanDuel +142 | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Tampa Bay Rays | Run Line | Tampa Bay Rays -1.5 | — | **FanDuel +116** / DraftKings +113 | — | -1.00 |

### 2026-06-22 — 5-4  (+0.10u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Milwaukee Brewers @ Cincinnati Reds | Moneyline | Milwaukee Brewers ML | — | **FanDuel -154** / DraftKings -157 | — | +0.65 |
| ✅ WIN | PLAY | Boston Red Sox @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -104** / DraftKings -105 | — | +0.96 |
| ✅ WIN | PLAY | Arizona Diamondbacks @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -142** / DraftKings -144 | — | +0.70 |
| ✅ WIN | LEAN | Philadelphia Phillies @ Washington Nationals | Total | Under 10.0 | 10.0 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | LEAN | Texas Rangers @ Miami Marlins | Total | Under 8.5 | 8.5 | **FanDuel -114** / DraftKings -114 | — | +0.88 |
| ❌ LOSS | PLAY | Milwaukee Brewers @ Cincinnati Reds | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +102** / FanDuel +100 | — | -1.00 |
| ❌ LOSS | LEAN | Kansas City Royals @ Tampa Bay Rays | Moneyline | Tampa Bay Rays ML | — | **FanDuel -188** / DraftKings -194 | — | -1.00 |
| ❌ LOSS | LEAN | Arizona Diamondbacks @ St. Louis Cardinals | Run Line | St. Louis Cardinals -1.5 | — | **FanDuel +146** / DraftKings +143 | — | -1.00 |
| ❌ LOSS | LEAN | Atlanta Braves @ San Diego Padres | Moneyline | Atlanta Braves ML | — | **FanDuel -106** / DraftKings -109 | — | -1.00 |

### 2026-06-21 — 3-4  (-1.02u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Minnesota Twins @ Arizona Diamondbacks | Moneyline | Minnesota Twins ML | — | **FanDuel +118** / DraftKings +109 | — | +1.18 |
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Moneyline | Los Angeles Angels ML | — | **FanDuel +108** / DraftKings +104 | — | +1.08 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -138** / DraftKings -149 | — | +0.72 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -108** / DraftKings -110 | — | -1.00 |
| ❌ LOSS | PLAY | Pittsburgh Pirates @ Colorado Rockies | Total | Under 12.0 | 12.0 | **FanDuel -104** / DraftKings -114 | — | -1.00 |
| ❌ LOSS | PLAY | St. Louis Cardinals @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -105** / FanDuel -110 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Kansas City Royals | Moneyline | Kansas City Royals ML | — | **FanDuel +104** / DraftKings +104 | — | -1.00 |

### 2026-06-20 — 6-8  (-2.19u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Total | Under 9.5 | 9.5 | **FanDuel -105** / DraftKings -108 | — | +0.95 |
| ✅ WIN | PLAY | Pittsburgh Pirates @ Colorado Rockies | Total | Under 10.5 | 10.5 | **FanDuel -110** / DraftKings -112 | — | +0.91 |
| ✅ WIN | PLAY | Minnesota Twins @ Arizona Diamondbacks | Moneyline | Minnesota Twins ML | — | **DraftKings +113** / FanDuel +110 | — | +1.13 |
| ✅ WIN | LEAN | San Francisco Giants @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -136** / DraftKings -143 | — | +0.74 |
| ✅ WIN | LEAN | Minnesota Twins @ Arizona Diamondbacks | Run Line | Minnesota Twins -1.5 | — | **DraftKings -180** / FanDuel -196 | — | +0.56 |
| ✅ WIN | LEAN | San Francisco Giants @ Miami Marlins | Run Line | Miami Marlins -1.5 | — | **FanDuel +152** / DraftKings +149 | — | +1.52 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -200** / DraftKings -205 | — | -1.00 |
| ❌ LOSS | PLAY | Toronto Blue Jays @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -126** / DraftKings -131 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -267** / FanDuel -270 | — | -1.00 |
| ❌ LOSS | PLAY | Cincinnati Reds @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel +100** / DraftKings +100 | — | -1.00 |
| ❌ LOSS | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Run Line | Los Angeles Dodgers -1.5 | — | **DraftKings -122** / FanDuel -125 | — | -1.00 |
| ❌ LOSS | LEAN | San Diego Padres @ Texas Rangers | Moneyline | Texas Rangers ML | — | **FanDuel -134** / DraftKings -136 | — | -1.00 |
| ➖ PUSH | LEAN | Milwaukee Brewers @ Atlanta Braves | Total | Over 7.0 | 7.0 | **FanDuel -120** / DraftKings -122 | — | +0.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **DraftKings -206** / FanDuel -210 | — | -1.00 |
| ❌ LOSS | LEAN | Cincinnati Reds @ New York Yankees | Total | Under 9.5 | 9.5 | **FanDuel -115** / DraftKings -119 | — | -1.00 |

### 2026-06-19 — 5-5  (-1.65u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cincinnati Reds @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -270** / DraftKings -286 | — | +0.37 |
| ✅ WIN | PLAY | Baltimore Orioles @ Los Angeles Dodgers | Moneyline | Los Angeles Dodgers ML | — | **DraftKings -199** / FanDuel -200 | — | +0.50 |
| ✅ WIN | PLAY | San Francisco Giants @ Miami Marlins | Moneyline | Miami Marlins ML | — | **FanDuel -130** / DraftKings -131 | — | +0.77 |
| ✅ WIN | PLAY | Cincinnati Reds @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel -120** / DraftKings -125 | — | +0.83 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Colorado Rockies | Total | Under 11.5 | 11.5 | **FanDuel -114** / DraftKings -114 | — | +0.88 |
| ❌ LOSS | PLAY | Los Angeles Angels @ Athletics | Total | Under 10.0 | 10.0 | **DraftKings -112** / FanDuel -115 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Athletics | Moneyline | Los Angeles Angels ML | — | **DraftKings +139** / FanDuel +134 | — | -1.00 |
| ❌ LOSS | LEAN | St. Louis Cardinals @ Kansas City Royals | Total | Under 9.0 | 9.0 | **DraftKings -103** / FanDuel -105 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Colorado Rockies | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -136** / DraftKings -143 | — | -1.00 |
| ❌ LOSS | LEAN | Washington Nationals @ Tampa Bay Rays | Total | Over 7.5 | 7.5 | **DraftKings -118** / FanDuel -120 | — | -1.00 |

### 2026-06-18 — 5-3  (+2.06u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Los Angeles Angels @ Athletics | Total | Under 10.5 | 10.5 | **DraftKings -113** / FanDuel -120 | — | +0.88 |
| ✅ WIN | PLAY | Toronto Blue Jays @ Boston Red Sox | Total | Under 9.0 | 9.0 | **DraftKings -108** / FanDuel -115 | — | +0.93 |
| ✅ WIN | PLAY | Minnesota Twins @ Texas Rangers | Moneyline | Minnesota Twins ML | — | **FanDuel -124** / DraftKings -126 | — | +0.81 |
| ✅ WIN | LEAN | New York Mets @ Philadelphia Phillies | Moneyline | New York Mets ML | — | **FanDuel +104** / DraftKings +104 | — | +1.04 |
| ✅ WIN | LEAN | Minnesota Twins @ Texas Rangers | Run Line | Minnesota Twins -1.5 | — | **FanDuel +140** / DraftKings +130 | — | +1.40 |
| ❌ LOSS | PLAY | Chicago White Sox @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -158** / DraftKings -163 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -146** / DraftKings -156 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +150** / FanDuel +146 | — | -1.00 |

### 2026-06-17 — 8-5  (+1.92u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | San Diego Padres @ St. Louis Cardinals | Total | Under 10.5 | 10.5 | **DraftKings -102** / FanDuel -120 | — | +0.98 |
| ✅ WIN | PLAY | Los Angeles Angels @ Arizona Diamondbacks | Total | Under 9.5 | 9.5 | **DraftKings -102** / FanDuel -128 | — | +0.98 |
| ✅ WIN | PLAY | Chicago White Sox @ New York Yankees | Moneyline | New York Yankees ML | — | **FanDuel -184** / DraftKings -186 | — | +0.54 |
| ✅ WIN | PLAY | Chicago White Sox @ New York Yankees | Run Line | New York Yankees -1.5 | — | **FanDuel +116** / DraftKings +113 | — | +1.16 |
| ✅ WIN | LEAN | Miami Marlins @ Philadelphia Phillies | Moneyline | Miami Marlins ML | — | **DraftKings +103** / FanDuel +102 | — | +1.03 |
| ✅ WIN | LEAN | Colorado Rockies @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -188** / DraftKings -194 | — | +0.53 |
| ✅ WIN | LEAN | Cleveland Guardians @ Milwaukee Brewers | Total | Over 7.5 | 7.5 | **DraftKings -112** / FanDuel -115 | — | +0.89 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Athletics | Moneyline | Pittsburgh Pirates ML | — | **FanDuel -124** / DraftKings -125 | — | +0.81 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -154** / DraftKings -156 | — | -1.00 |
| ❌ LOSS | PLAY | Colorado Rockies @ Chicago Cubs | Total | Under 10.0 | 10.0 | **FanDuel -106** / DraftKings -108 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **DraftKings +135** / FanDuel +132 | — | -1.00 |
| ❌ LOSS | LEAN | Pittsburgh Pirates @ Athletics | Total | Under 10.0 | 10.0 | **FanDuel -104** / DraftKings -105 | — | -1.00 |
| ❌ LOSS | LEAN | Los Angeles Angels @ Arizona Diamondbacks | Moneyline | Los Angeles Angels ML | — | **FanDuel +146** / DraftKings +141 | — | -1.00 |

### 2026-06-16 — 4-6  (-2.26u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | PLAY | Cleveland Guardians @ Milwaukee Brewers | Moneyline | Milwaukee Brewers ML | — | **FanDuel -118** / DraftKings -157 | — | +0.85 |
| ✅ WIN | LEAN | Kansas City Royals @ Washington Nationals | Moneyline | Washington Nationals ML | — | **FanDuel -118** / DraftKings -144 | — | +0.85 |
| ✅ WIN | LEAN | San Diego Padres @ St. Louis Cardinals | Moneyline | St. Louis Cardinals ML | — | **FanDuel -118** / DraftKings -120 | — | +0.85 |
| ✅ WIN | LEAN | Pittsburgh Pirates @ Athletics | Moneyline | Pittsburgh Pirates ML | — | **DraftKings +119** / FanDuel -126 | — | +1.19 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Moneyline | Atlanta Braves ML | — | **FanDuel -138** / DraftKings -171 | — | -1.00 |
| ❌ LOSS | PLAY | Cleveland Guardians @ Milwaukee Brewers | Total | Over 8.0 | 8.0 | **DraftKings -119** / FanDuel -124 | — | -1.00 |
| ❌ LOSS | PLAY | Minnesota Twins @ Texas Rangers | Moneyline | Texas Rangers ML | — | **DraftKings -132** / FanDuel -134 | — | -1.00 |
| ❌ LOSS | PLAY | San Francisco Giants @ Atlanta Braves | Run Line | Atlanta Braves -1.5 | — | **FanDuel +146** / DraftKings +119 | — | -1.00 |
| ❌ LOSS | LEAN | Cleveland Guardians @ Milwaukee Brewers | Run Line | Milwaukee Brewers -1.5 | — | **DraftKings +135** / FanDuel -205 | — | -1.00 |
| ❌ LOSS | LEAN | Colorado Rockies @ Chicago Cubs | Moneyline | Chicago Cubs ML | — | **FanDuel -180** / DraftKings -198 | — | -1.00 |
