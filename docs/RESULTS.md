# Results

## Scoreboard

| Board | Record | Hit rate | Model predicted | Standing |
|---|---|---|---|---|
| **Locked bets** (ML/Total) | 327-282 | **53.7%** | — | -3.54u · CLV -7.31% |
| NRFI/YRFI forced calls | 58-70 | **45.3%** | 59.7% | 🔴 behind its own number · ⚠️ below 58% naive baseline |
| HR board (top 10 daily) | 14-76 | **15.6%** | 24.5% | 🔴 behind its own number |
| Player props (all tiers) | 1658-1923 | **46.3%** | 53.0% | 🔴 behind its own number · CLV -0.21% |
| &nbsp;&nbsp;↳ props · tier A (HR, pitcher K) | 85-61 | **58.2%** | 57.8% | 🟡 tracking its number |
| &nbsp;&nbsp;↳ props · tier B (hits, batter K) | 580-555 | **51.1%** | 57.0% | 🔴 behind its own number |
| &nbsp;&nbsp;↳ props · tier C (RBI, H+R+RBI) | 980-1290 | **43.2%** | 50.5% | 🔴 behind its own number |

**Hit rate vs predicted is the whole test.** A board that hits at the rate it claims is trustworthy even when it loses; a board that hits below its own number is telling you it does not know what it claims to know.

---

**Model A** = current model (control). **Model B** = retired variant, history preserved. CLV measured from the real price vs close. Each unique bet counted once. Paper only — no real money.

**Model A: 327-282  ·  54% win  ·  -3.54u  ·  -0.6% ROI  ·  avg CLV -7.31%**
**Model B: 237-191  ·  55% win  ·  +14.16u  ·  +3.3% ROI  ·  avg CLV n/a (no closing lines yet)**

## Board calibration standings

These boards are calibration records, not bets. The question is not whether they won — it is whether a call at a stated confidence lands at that rate. A tier that hits BELOW its stated probability is a model telling you it does not know what it claims to know.

### NRFI/YRFI forced calls

| Confidence | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|
| High | 74 | 27 | 47 | 36% | 64% | -27% |
| Medium | 22 | 13 | 9 | 59% | 57% | +2% |
| Low | 11 | 5 | 6 | 45% | 53% | -8% |
| Coin flip | 21 | 13 | 8 | 62% | 53% | +9% |
| **All** | **128** | **58** | **70** | **45%** | **60%** | **-14%** |

YRFI share of calls: **98/128 (77%)** — hitting 42%.

**Naive baseline check.** First innings were scoreless in **57.8%** of these games, so always calling NRFI scores **57.8%**. The model scores **45.3%**.

> ⚠️ **The model is losing to a coin that always says the same thing.** Until it beats this line, its calls carry no information and should not be treated as analysis — a forced call is only worth making if it beats the majority class.

> ⚠️ **Confidence is inverted**: the High tier is hitting BELOW the Coin flip tier. Whatever the confidence metric is measuring, it is not the probability of being right. Calls at this tier should carry no weight until this reverses.

### HR board (top-10 daily)

- listed and graded: **90**
- homered: **14** · model expected **22.0**
- actual rate **15.6%** vs predicted **24.5%** (**-8.9%**)

### Prop divergence board

| Tier | Market | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|---|
| A | Ks (P) | 146 | 85 | 61 | 58% | 58% | +0% |
| B | Hits | 1135 | 580 | 555 | 51% | 57% | -6% |
| C | H+R+RBI | 1135 | 547 | 588 | 48% | 58% | -9% |
| C | RBI | 1135 | 433 | 702 | 38% | 44% | -5% |
| **All** | | **3581** | **1658** | **1923** | **46%** | **53%** | **-7%** |

Gate-clearing calls only: **40-32** (56% vs 60% predicted).

> **Sample-size reality check.** Distinguishing a real edge from noise needs hundreds of graded calls per tier. Gaps below are indicative, not verdicts — except where a tier is inverted against a lower tier, which is a structural signal rather than variance.

## Daily ledger — every call, every result

Last 4 graded slates in full. Most recent first.

### 2026-08-19 — props 7-55

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Paul Skenes | Ks (P) | Over | 6.5 | +136 | 48% | 1 | — | ❌ |
| Gleyber Torres | Hits | Over | 0.5 | -181 | 75% | 0 | — | ❌ |
| Oneil Cruz | Hits | Over | 0.5 | -163 | 72% | 1 | — | ✅ |
| Esmerlyn Valdez | Hits | Over | 0.5 | -154 | 70% | 0 | — | ❌ |
| Colt Keith | Hits | Over | 0.5 | -179 | 73% | 0 | — | ❌ |
| Nick Gonzales | Hits | Over | 0.5 | -247 | 81% | 0 | — | ❌ |
| Ty France | Hits | Over | 0.5 | -226 | 79% | 0 | — | ❌ |
| Spencer Torkelson | Hits | Over | 0.5 | -117 | 61% | 0 | — | ❌ |
| Jared Young | Hits | Over | 0.5 | -176 | 72% | 0 | — | ❌ |
| Jacob Gonzalez | RBI | Over | 0.5 | +224 | 36% | 0 | — | ❌ |
| Jacob Gonzalez | Hits | Over | 0.5 | -172 | 70% | 0 | — | ❌ |
| Hao-Yu Lee | Hits | Over | 0.5 | -138 | 64% | 0 | — | ❌ |
| Hao-Yu Lee | H+R+RBI | Over | 0.5 | -166 | 72% | 0 | — | ❌ |
| Colt Keith | H+R+RBI | Over | 1.5 | +111 | 55% | 0 | — | ❌ |
| Kevin McGonigle | Hits | Over | 0.5 | -209 | 74% | 0 | — | ❌ |
| Gleyber Torres | H+R+RBI | Over | 1.5 | +110 | 55% | 0 | — | ❌ |
| Oneil Cruz | H+R+RBI | Over | 1.5 | -105 | 58% | 2 | — | ✅ |
| Brandon Lowe | RBI | Over | 0.5 | +171 | 41% | 0 | — | ❌ |
| Dillon Dingler | RBI | Over | 0.5 | +190 | 38% | 0 | — | ❌ |
| Zach McKinstry | Hits | Over | 0.5 | -161 | 66% | 0 | — | ❌ |
| Brandon Lowe | Hits | Over | 0.5 | -227 | 74% | 0 | — | ❌ |
| Spencer Torkelson | H+R+RBI | Over | 0.5 | -156 | 68% | 0 | — | ❌ |
| Esmerlyn Valdez | H+R+RBI | Over | 1.5 | +105 | 54% | 0 | — | ❌ |
| Brandon Lowe | H+R+RBI | Over | 1.5 | -124 | 61% | 0 | — | ❌ |
| Jacob Gonzalez | H+R+RBI | Over | 1.5 | +113 | 51% | 0 | — | ❌ |
| Henry Davis | H+R+RBI | Over | 0.5 | -165 | 68% | 0 | — | ❌ |
| Henry Davis | RBI | Over | 0.5 | +239 | 32% | 0 | — | ❌ |
| Nick Gonzales | H+R+RBI | Over | 1.5 | -117 | 58% | 0 | — | ❌ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +177 | 39% | 0 | — | ❌ |
| Oneil Cruz | RBI | Over | 0.5 | +160 | 41% | 1 | — | ✅ |
| Nick Gonzales | RBI | Over | 0.5 | +228 | 32% | 0 | — | ❌ |
| Dillon Dingler | Hits | Over | 0.5 | -200 | 69% | 0 | — | ❌ |
| Spencer Horwitz | RBI | Over | 0.5 | +202 | 35% | 0 | — | ❌ |
| Dillon Dingler | H+R+RBI | Over | 1.5 | -102 | 53% | 0 | — | ❌ |
| Spencer Horwitz | Hits | Over | 0.5 | -233 | 72% | 0 | — | ❌ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | -108 | 54% | 1 | — | ❌ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -103 | 53% | 0 | — | ❌ |
| Paul Skenes | Ks (P) | Over | 5.5 | -162 | 63% | 1 | — | ❌ |
| Bryan Reynolds | RBI | Over | 0.5 | +198 | 35% | 0 | — | ❌ |
| Bryan Reynolds | Hits | Over | 0.5 | -205 | 68% | 1 | — | ✅ |
| Ty France | H+R+RBI | Over | 1.5 | -128 | 57% | 0 | — | ❌ |
| Jake Cronenworth | Hits | Over | 0.5 | -206 | 68% | 0 | — | ❌ |
| Jared Young | H+R+RBI | Over | 1.5 | +104 | 49% | 0 | — | ❌ |
| Manny Machado | H+R+RBI | Under | 1.5 | +102 | 49% | 0 | — | ✅ |
| Fernando Tatis Jr. | H+R+RBI | Over | 1.5 | -154 | 59% | 0 | — | ❌ |
| Manny Machado | Hits | Under | 0.5 | +187 | 34% | 0 | — | ✅ |
| Fernando Tatis Jr. | RBI | Over | 0.5 | +160 | 37% | 0 | — | ❌ |
| Ty France | RBI | Over | 0.5 | +161 | 37% | 0 | — | ❌ |
| Spencer Horwitz | H+R+RBI | Over | 1.5 | -126 | 54% | 0 | — | ❌ |
| Manny Machado | RBI | Over | 0.5 | +156 | 37% | 0 | — | ❌ |
| Zach McKinstry | H+R+RBI | Over | 1.5 | +126 | 42% | 0 | — | ❌ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -117 | 51% | 0 | — | ✅ |
| Fernando Tatis Jr. | Hits | Over | 1.5 | +179 | 34% | 0 | — | ❌ |
| Jared Young | RBI | Over | 0.5 | +191 | 32% | 0 | — | ❌ |
| Henry Davis | Hits | Over | 0.5 | -118 | 51% | 0 | — | ❌ |
| Jake Cronenworth | RBI | Over | 0.5 | +211 | 29% | 0 | — | ❌ |
| Kevin McGonigle | RBI | Over | 0.5 | +201 | 29% | 0 | — | ❌ |
| Hao-Yu Lee | RBI | Over | 0.5 | +293 | 32% | 0 | — | ❌ |
| Gleyber Torres | RBI | Over | 0.5 | +278 | 32% | 0 | — | ❌ |
| Spencer Torkelson | RBI | Over | 0.5 | +255 | 32% | 0 | — | ❌ |
| Colt Keith | RBI | Over | 0.5 | +268 | 30% | 0 | — | ❌ |
| Zach McKinstry | RBI | Over | 0.5 | +268 | 24% | 0 | — | ❌ |

*Bold = cleared its edge and EV gate.*

---

### 2026-08-18 — bets 4-3 (-0.42u)

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Los Angeles Dodgers ML | — | -180 | 9.5 | +3.4% | ✅ +0.56u |
| Moneyline | Atlanta Braves ML | — | -126 | 8.5 | -9.4% | ❌ -1.00u |
| Moneyline | St. Louis Cardinals ML | — | -120 | 8.1 | -18.1% | ✅ +0.83u |
| Moneyline | Boston Red Sox ML | — | -171 | 8.1 | -6.5% | ✅ +0.58u |
| Moneyline | Chicago Cubs ML | — | -164 | 5.9 | +0.9% | ✅ +0.61u |
| Moneyline | Tampa Bay Rays ML | — | -146 | 5.1 | +14.1% | ❌ -1.00u |
| Total | Over 8.5 | 8.5 | -115 | 5.0 | — | ❌ -1.00u |

### 2026-08-17 — bets 3-2 (-0.09u) · props 183-215 · NRFI 7-4 · HR 3-5

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Tampa Bay Rays ML | — | -156 | 9.5 | -30.2% | ✅ +0.64u |
| Moneyline | Los Angeles Dodgers ML | — | -255 | 9.5 | -11.6% | ✅ +0.39u |
| Moneyline | Atlanta Braves ML | — | -122 | 8.5 | +0.7% | ❌ -1.00u |
| Total | Under 11.0 | 11.0 | -115 | 6.0 | — | ❌ -1.00u |
| F5 Total | F5 Over 4.5 | 4.5 | -113 | 5.4 | -2.1% | ✅ +0.88u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Gleyber Torres | RBI | Over | 0.5 | +264 | 36% | 0 | +4.9% | ❌ |
| Carmen Mlodzinski | Ks (P) | Over | 2.5 | -166 | 80% | 3 | +0.9% | ✅ |
| Jake Cronenworth | Hits | Under | 0.5 | +143 | 52% | 2 | +4.3% | ❌ |
| Jake Rogers | H+R+RBI | Over | 0.5 | -119 | 68% | 0 | -2.0% | ❌ |
| Brandon Lowe | H+R+RBI | Over | 1.5 | +118 | 57% | 2 | +7.4% | ✅ |
| J.T. Realmuto | Hits | Under | 0.5 | +163 | 47% | 1 | +7.3% | ❌ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +104 | 61% | 0 | +0.0% | ❌ |
| Chase Meidroth | RBI | Over | 0.5 | +292 | 31% | 0 | -3.5% | ❌ |
| Carter Jensen | H+R+RBI | Under | 1.5 | +124 | 54% | 2 | +2.8% | ❌ |
| Jonah Heim | Hits | Under | 0.5 | +116 | 56% | 0 | — | ✅ |
| Braden Montgomery | RBI | Over | 0.5 | +262 | 33% | 0 | +2.3% | ❌ |
| Otto Lopez | H+R+RBI | Over | 1.5 | -118 | 65% | 4 | — | ✅ |
| Brandon Lowe | RBI | Over | 0.5 | +203 | 40% | 0 | +5.6% | ❌ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | -115 | 64% | 4 | +0.0% | ✅ |
| Carter Jensen | Hits | Under | 0.5 | +200 | 40% | 1 | +5.3% | ❌ |
| Seiya Suzuki | RBI | Over | 0.5 | +182 | 42% | 1 | +0.0% | ✅ |
| Javier Baez | H+R+RBI | Over | 1.5 | +117 | 55% | 0 | +3.8% | ❌ |
| Salvador Perez | Hits | Under | 0.5 | +198 | 40% | 1 | +9.6% | ❌ |
| Jake McCarthy | RBI | Over | 0.5 | +230 | 36% | 1 | -4.3% | ✅ |
| Javier Baez | Hits | Over | 0.5 | -168 | 74% | 0 | +2.8% | ❌ |
| Richie Palacios | H+R+RBI | Over | 0.5 | -168 | 74% | 2 | -20.2% | ✅ |
| Gleyber Torres | H+R+RBI | Over | 1.5 | -123 | 65% | 3 | +3.8% | ✅ |
| Ryan Kreidler | Hits | Under | 0.5 | -103 | 60% | 0 | — | ✅ |
| Jakob Marsee | H+R+RBI | Over | 0.5 | -160 | 72% | 0 | — | ❌ |
| Ezequiel Tovar | H+R+RBI | Over | 0.5 | -170 | 74% | 1 | -0.7% | ✅ |
| Hunter Feduccia | H+R+RBI | Under | 1.5 | -127 | 66% | 0 | +4.3% | ✅ |
| Heriberto Hernandez | RBI | Over | 0.5 | +245 | 34% | 0 | -6.8% | ❌ |
| Leody Taveras | Hits | Under | 0.5 | +107 | 57% | 0 | — | ✅ |
| Hunter Feduccia | Hits | Under | 0.5 | +126 | 52% | 0 | +8.1% | ✅ |
| Esmerlyn Valdez | H+R+RBI | Over | 1.5 | +108 | 56% | 0 | +5.0% | ❌ |
| Pete Alonso | RBI | Over | 0.5 | +222 | 36% | 1 | -16.4% | ✅ |
| Pete Alonso | H+R+RBI | Over | 1.5 | +110 | 56% | 4 | — | ✅ |
| Coby Mayo | H+R+RBI | Over | 0.5 | -160 | 72% | 5 | — | ✅ |
| Liam Hicks | H+R+RBI | Over | 1.5 | -108 | 61% | 0 | — | ❌ |
| Chase Meidroth | Hits | Over | 0.5 | -209 | 79% | 0 | -1.4% | ❌ |
| Liam Hicks | RBI | Over | 0.5 | +203 | 38% | 0 | -42.3% | ❌ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | -108 | 60% | 0 | +1.8% | ❌ |
| Lawrence Butler | Hits | Under | 0.5 | +135 | 49% | 1 | -2.9% | ❌ |
| Alex Bregman | H+R+RBI | Over | 1.5 | -113 | 62% | 3 | +0.0% | ✅ |
| Kyle Isbel | H+R+RBI | Under | 1.5 | -123 | 64% | 3 | +3.1% | ❌ |
| Otto Lopez | RBI | Over | 0.5 | +273 | 31% | 1 | -9.0% | ✅ |
| Miguel Vargas | H+R+RBI | Over | 1.5 | -107 | 60% | 2 | +1.8% | ✅ |
| Tommy Edman | Hits | Under | 1.5 | -211 | 78% | 1 | +0.0% | ✅ |
| Connor Norby | Hits | Under | 0.5 | +103 | 56% | 1 | -2.4% | ❌ |
| Gunnar Henderson | H+R+RBI | Over | 1.5 | +126 | 51% | 3 | — | ✅ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | +116 | 53% | 2 | +0.0% | ✅ |
| Gleyber Torres | Hits | Over | 0.5 | -237 | 80% | 1 | +1.3% | ✅ |
| Shohei Ohtani | H+R+RBI | Under | 2.5 | +114 | 53% | 11 | -0.9% | ❌ |
| Xander Bogaerts | Hits | Under | 0.5 | +122 | 51% | 0 | +4.2% | ✅ |
| Carson Benge | H+R+RBI | Over | 1.5 | -102 | 57% | 1 | +0.0% | ❌ |
| Dillon Dingler | H+R+RBI | Over | 1.5 | -129 | 64% | 1 | +3.5% | ❌ |
| Teoscar Hernandez | Hits | Under | 1.5 | -261 | 81% | 0 | +0.5% | ✅ |
| Luis Rengifo | H+R+RBI | Over | 1.5 | +139 | 47% | 1 | — | ❌ |
| Framber Valdez | Ks (P) | Under | 5.5 | -150 | 67% | 5 | +0.0% | ✅ |
| Carson Benge | Hits | Over | 0.5 | -198 | 75% | 1 | -1.0% | ✅ |
| Yandy Diaz | RBI | Over | 0.5 | +203 | 37% | 1 | — | ✅ |
| Dillon Dingler | RBI | Over | 0.5 | +165 | 42% | 0 | +7.3% | ❌ |
| Salvador Perez | H+R+RBI | Under | 1.5 | +110 | 53% | 3 | +7.6% | ❌ |
| Kyle Schwarber | H+R+RBI | Under | 2.5 | -138 | 65% | 2 | — | ✅ |
| Mauricio Dubon | H+R+RBI | Over | 1.5 | -104 | 57% | 0 | +4.5% | ❌ |
| Braden Montgomery | H+R+RBI | Over | 1.5 | +134 | 48% | 1 | +0.0% | ❌ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +199 | 37% | 0 | -2.6% | ❌ |
| Otto Lopez | Hits | Over | 0.5 | -271 | 81% | 2 | -15.8% | ✅ |
| Mauricio Dubon | RBI | Over | 0.5 | +228 | 34% | 0 | +4.1% | ❌ |
| Jonathan Aranda | RBI | Over | 0.5 | +190 | 38% | 1 | -37.0% | ✅ |
| Luis Arraez | Hits | Over | 1.5 | +174 | 40% | 1 | — | ❌ |
| Jac Caglianone | H+R+RBI | Under | 2.5 | -147 | 66% | 6 | +3.4% | ❌ |
| Brandon Marsh | Hits | Over | 0.5 | -212 | 75% | 0 | -1.1% | ❌ |
| Tommy Edman | H+R+RBI | Under | 2.5 | -154 | 67% | 2 | +0.0% | ✅ |
| Michael Conforto | Hits | Under | 0.5 | -114 | 59% | 0 | -3.0% | ✅ |
| Nico Hoerner | RBI | Over | 0.5 | +229 | 34% | 2 | -2.4% | ✅ |
| Donovan Walton | Hits | Under | 0.5 | +112 | 52% | 1 | +3.9% | ❌ |
| Bryson Stott | Hits | Under | 0.5 | +190 | 38% | 1 | +7.4% | ❌ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -140 | 64% | 6 | +0.0% | ✅ |
| Bryan Reynolds | Hits | Over | 0.5 | -216 | 75% | 0 | +0.6% | ❌ |
| Willi Castro | H+R+RBI | Over | 1.5 | -102 | 56% | 2 | +2.4% | ✅ |
| Michael Massey | Hits | Under | 0.5 | +172 | 40% | 1 | +12.9% | ❌ |
| Jake McCarthy | Hits | Over | 1.5 | +187 | 38% | 0 | — | ❌ |
| Nico Hoerner | H+R+RBI | Over | 1.5 | -107 | 57% | 6 | +0.0% | ✅ |
| Alex Bregman | RBI | Over | 0.5 | +188 | 38% | 0 | +0.0% | ❌ |
| Henry Davis | H+R+RBI | Over | 0.5 | -154 | 66% | 2 | +3.6% | ✅ |
| Willi Castro | Hits | Over | 0.5 | -194 | 72% | 1 | +2.0% | ✅ |
| Bobby Witt Jr. | H+R+RBI | Under | 2.5 | -148 | 65% | 10 | +1.6% | ❌ |
| Henry Davis | Hits | Under | 0.5 | -107 | 56% | 1 | -0.5% | ❌ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -131 | 62% | 2 | +3.8% | ❌ |
| Jonathan Aranda | H+R+RBI | Over | 1.5 | -132 | 62% | 4 | -2.4% | ✅ |
| Gabriel Moreno | H+R+RBI | Over | 1.5 | -123 | 60% | 1 | +1.8% | ❌ |
| Hunter Feduccia | RBI | Under | 0.5 | -280 | 80% | 0 | +2.6% | ✅ |
| Manny Machado | Hits | Under | 0.5 | +157 | 42% | 1 | +2.4% | ❌ |
| Matt Olson | H+R+RBI | Over | 1.5 | -143 | 64% | 1 | -2.7% | ❌ |
| Francisco Lindor | H+R+RBI | Over | 1.5 | -124 | 60% | 1 | -1.8% | ❌ |
| Munetaka Murakami | RBI | Over | 0.5 | +193 | 37% | 0 | +0.0% | ❌ |
| Isaac Collins | H+R+RBI | Under | 1.5 | -123 | 60% | 0 | +3.1% | ✅ |
| Bo Bichette | H+R+RBI | Over | 1.5 | -122 | 60% | 2 | -2.3% | ✅ |
| Lawrence Butler | H+R+RBI | Under | 1.5 | -138 | 63% | 1 | -0.6% | ✅ |
| Wilyer Abreu | H+R+RBI | Over | 1.5 | -138 | 63% | 5 | +0.0% | ✅ |
| Bobby Witt Jr. | RBI | Under | 0.5 | -185 | 70% | 3 | +2.0% | ❌ |
| Kevin McGonigle | Hits | Over | 0.5 | -262 | 78% | 2 | +0.2% | ✅ |
| Jared Young | Hits | Over | 0.5 | -168 | 68% | 0 | -2.5% | ❌ |
| Rhett Lowder | Ks (P) | Under | 4.5 | -156 | 66% | 5 | — | ❌ |
| Kyle Isbel | RBI | Under | 0.5 | -276 | 79% | 1 | +2.3% | ❌ |
| Alec Bohm | RBI | Over | 0.5 | +186 | 38% | 1 | -9.2% | ✅ |
| Carson Kelly | RBI | Over | 0.5 | +243 | 31% | 0 | -5.2% | ❌ |
| Seiya Suzuki | Hits | Over | 0.5 | -204 | 72% | 1 | -1.5% | ✅ |
| Gabriel Moreno | RBI | Over | 0.5 | +184 | 38% | 0 | +0.0% | ❌ |
| Jake McCarthy | H+R+RBI | Over | 1.5 | -133 | 61% | 1 | -3.7% | ❌ |
| Cole Carrigg | H+R+RBI | Over | 1.5 | -120 | 59% | 0 | -0.8% | ❌ |
| Brandon Marsh | H+R+RBI | Over | 1.5 | -116 | 58% | 0 | -4.6% | ❌ |
| Heriberto Hernandez | H+R+RBI | Over | 1.5 | +117 | 50% | 0 | — | ❌ |
| Michael Massey | H+R+RBI | Under | 1.5 | -108 | 56% | 2 | +9.6% | ❌ |
| Wilyer Abreu | Hits | Over | 0.5 | -256 | 77% | 2 | +0.1% | ✅ |
| Richie Palacios | Hits | Over | 0.5 | -132 | 61% | 1 | -23.6% | ✅ |
| Francisco Alvarez | Hits | Over | 0.5 | -130 | 60% | 0 | -1.7% | ❌ |
| Mauricio Dubon | Hits | Over | 0.5 | -223 | 74% | 0 | +1.6% | ❌ |
| Jonathan Aranda | Hits | Over | 0.5 | -263 | 77% | 2 | — | ✅ |
| Randal Grichuk | RBI | Under | 0.5 | -302 | 80% | 3 | -0.8% | ❌ |
| Luis Campusano | Hits | Over | 0.5 | -151 | 64% | 0 | +0.0% | ❌ |
| Byron Buxton | Hits | Under | 0.5 | +187 | 37% | 1 | +0.7% | ❌ |
| Luis Rengifo | Hits | Over | 0.5 | -139 | 62% | 1 | -0.3% | ✅ |
| Ian Happ | Hits | Over | 0.5 | -173 | 68% | 1 | -1.3% | ✅ |
| Zack Gelof | Hits | Under | 0.5 | +170 | 40% | 1 | +2.7% | ❌ |
| Francisco Alvarez | H+R+RBI | Over | 1.5 | +132 | 46% | 0 | — | ❌ |
| Michael Conforto | H+R+RBI | Over | 0.5 | -160 | 66% | 0 | +1.6% | ❌ |
| Carlos Cortes | Hits | Under | 0.5 | +133 | 46% | 1 | -2.1% | ❌ |
| Junior Caminero | H+R+RBI | Over | 1.5 | -144 | 63% | 1 | — | ❌ |
| Javier Sanoja | RBI | Over | 0.5 | +254 | 30% | 2 | — | ✅ |
| Kyle Isbel | Hits | Under | 0.5 | +144 | 44% | 1 | +3.4% | ❌ |
| Yandy Diaz | H+R+RBI | Over | 1.5 | -155 | 65% | 5 | — | ✅ |
| Isaac Collins | Hits | Under | 0.5 | +139 | 44% | 0 | +2.1% | ✅ |
| Freddie Freeman | H+R+RBI | Under | 2.5 | -117 | 57% | 6 | +0.0% | ❌ |
| Javier Baez | RBI | Over | 0.5 | +258 | 30% | 0 | +1.1% | ❌ |
| Jackson Holliday | Hits | Under | 0.5 | +123 | 48% | 1 | — | ❌ |
| Ian Happ | H+R+RBI | Over | 1.5 | -102 | 54% | 2 | +0.0% | ✅ |
| Brett Sullivan | RBI | Over | 0.5 | +249 | 30% | 1 | -2.8% | ✅ |
| Connor Norby | H+R+RBI | Under | 1.5 | -178 | 68% | 2 | -2.3% | ❌ |
| Willson Contreras | Hits | Under | 0.5 | +170 | 39% | 2 | +1.5% | ❌ |
| Xavier Edwards | H+R+RBI | Over | 1.5 | +101 | 53% | 4 | — | ✅ |
| Bryce Harper | Hits | Over | 0.5 | -259 | 76% | 3 | — | ✅ |
| Ildemaro Vargas | RBI | Over | 0.5 | +207 | 34% | 0 | +0.0% | ❌ |
| Leody Taveras | H+R+RBI | Over | 0.5 | -177 | 67% | 0 | — | ❌ |
| Salvador Perez | RBI | Under | 0.5 | -180 | 68% | 2 | +8.1% | ❌ |
| Pete Alonso | Hits | Over | 0.5 | -177 | 67% | 2 | -28.9% | ✅ |
| Bryce Harper | H+R+RBI | Over | 1.5 | -139 | 61% | 4 | — | ✅ |
| Luis Arraez | H+R+RBI | Over | 1.5 | -155 | 64% | 2 | -17.7% | ✅ |
| Esteury Ruiz | RBI | Under | 0.5 | -458 | 86% | 0 | +3.8% | ✅ |
| Spencer Torkelson | H+R+RBI | Over | 1.5 | +105 | 51% | 0 | — | ❌ |
| Gavin Sheets | Hits | Under | 0.5 | -103 | 53% | 1 | -1.0% | ❌ |
| Spencer Torkelson | RBI | Over | 0.5 | +195 | 36% | 0 | — | ❌ |
| Gavin Sheets | H+R+RBI | Over | 0.5 | -166 | 66% | 2 | +1.8% | ✅ |
| Pete Crow-Armstrong | H+R+RBI | Over | 1.5 | -152 | 63% | 9 | — | ✅ |
| Nick Gonzales | RBI | Over | 0.5 | +235 | 31% | 0 | +19.6% | ❌ |
| Richie Palacios | RBI | Over | 0.5 | +283 | 27% | 0 | -27.1% | ❌ |
| Brenton Doyle | RBI | Under | 0.5 | -400 | 84% | 0 | -1.9% | ✅ |
| Francisco Lindor | Hits | Over | 0.5 | -230 | 73% | 0 | -1.4% | ❌ |
| Adley Rutschman | RBI | Over | 0.5 | +190 | 36% | 1 | +2.1% | ✅ |
| Ryan Kreidler | RBI | Under | 0.5 | -393 | 83% | 0 | — | ✅ |
| Byron Buxton | RBI | Under | 0.5 | -198 | 69% | 0 | +0.2% | ✅ |
| Miguel Vargas | Hits | Over | 0.5 | -204 | 70% | 1 | +0.0% | ✅ |
| Brooks Lee | RBI | Over | 0.5 | +226 | 32% | 0 | -8.4% | ❌ |
| Randal Grichuk | H+R+RBI | Under | 1.5 | -169 | 65% | 5 | +0.0% | ❌ |
| TJ Rumfield | Hits | Over | 0.5 | -209 | 70% | 1 | -1.6% | ✅ |
| Caleb Durbin | RBI | Over | 0.5 | +201 | 34% | 1 | +0.0% | ✅ |
| Colt Keith | Hits | Over | 0.5 | -186 | 68% | 1 | +0.9% | ✅ |
| Gabriel Moreno | Hits | Over | 0.5 | -257 | 75% | 1 | +0.8% | ✅ |
| Zach McKinstry | RBI | Under | 0.5 | -303 | 78% | 1 | -0.5% | ❌ |
| Xavier Edwards | Hits | Over | 0.5 | -224 | 72% | 2 | -19.6% | ✅ |
| Carlos Cortes | H+R+RBI | Under | 1.5 | -150 | 62% | 2 | -1.4% | ❌ |
| Jake Rogers | Hits | Over | 0.5 | -101 | 52% | 0 | -2.5% | ❌ |
| Michael Harris II | H+R+RBI | Under | 2.5 | -159 | 64% | 1 | — | ✅ |
| Ryan Kreidler | H+R+RBI | Under | 0.5 | +126 | 46% | 0 | — | ✅ |
| Cole Carrigg | RBI | Over | 0.5 | +202 | 34% | 0 | +0.0% | ❌ |
| Alex Bregman | Hits | Over | 0.5 | -215 | 71% | 3 | -1.1% | ✅ |
| Ceddanne Rafaela | RBI | Over | 0.5 | +193 | 35% | 1 | +5.0% | ✅ |
| Isaac Collins | RBI | Under | 0.5 | -281 | 76% | 0 | +4.1% | ✅ |
| Tomoyuki Sugano | Ks (P) | Under | 2.5 | +133 | 44% | 3 | +8.9% | ❌ |
| Esteury Ruiz | Hits | Under | 0.5 | -107 | 53% | 2 | +14.5% | ❌ |
| Shohei Ohtani | RBI | Under | 0.5 | -121 | 57% | 3 | +0.0% | ❌ |
| Zack Gelof | H+R+RBI | Over | 1.5 | -111 | 54% | 1 | +2.1% | ❌ |
| Jakob Marsee | Hits | Under | 0.5 | -104 | 53% | 0 | — | ✅ |
| Jackson Merrill | Hits | Under | 0.5 | +163 | 39% | 1 | +1.9% | ❌ |
| Freddie Freeman | RBI | Under | 0.5 | -166 | 64% | 1 | -0.2% | ❌ |
| Nolan McLean | Ks (P) | Over | 5.5 | -140 | 60% | 3 | +3.4% | ❌ |
| Brenton Doyle | H+R+RBI | Over | 0.5 | -158 | 63% | 0 | +3.3% | ❌ |
| Brett Sullivan | Hits | Over | 0.5 | -140 | 60% | 1 | -1.8% | ✅ |
| Gunnar Henderson | RBI | Over | 0.5 | +266 | 28% | 0 | — | ❌ |
| Mitch Bratt | Ks (P) | Under | 3.5 | +112 | 48% | 0 | +5.0% | ✅ |
| Jeff McNeil | Hits | Under | 0.5 | +180 | 37% | 1 | -1.8% | ❌ |
| Colt Keith | RBI | Under | 0.5 | -264 | 74% | 0 | -0.6% | ✅ |
| Mookie Betts | H+R+RBI | Under | 2.5 | -148 | 61% | 3 | -1.7% | ❌ |
| Ozzie Albies | H+R+RBI | Over | 1.5 | -110 | 54% | 1 | -3.6% | ❌ |
| Brandon Lowe | Hits | Over | 0.5 | -149 | 61% | 2 | +6.6% | ✅ |
| Bailey Ober | Ks (P) | Under | 3.5 | -119 | 56% | 4 | -2.0% | ❌ |
| Teoscar Hernandez | RBI | Under | 0.5 | -186 | 67% | 0 | +1.1% | ✅ |
| Ceddanne Rafaela | H+R+RBI | Over | 1.5 | -141 | 60% | 6 | +1.2% | ✅ |
| Trea Turner | H+R+RBI | Over | 1.5 | -152 | 62% | 3 | -19.1% | ✅ |
| Dillon Dingler | Hits | Over | 0.5 | -259 | 74% | 1 | — | ✅ |
| Kyle Schwarber | Hits | Under | 1.5 | -275 | 75% | 1 | — | ✅ |
| Carlos Narvaez | H+R+RBI | Over | 0.5 | -117 | 55% | 0 | -17.6% | ❌ |
| Austin Riley | Hits | Over | 0.5 | -181 | 66% | 1 | -1.4% | ✅ |
| Carter Jensen | RBI | Under | 0.5 | -216 | 70% | 0 | +1.4% | ✅ |
| Michael Massey | RBI | Under | 0.5 | -253 | 73% | 0 | +4.6% | ✅ |
| Matt Olson | Hits | Over | 0.5 | -235 | 72% | 1 | -1.4% | ✅ |
| Michael Busch | Hits | Over | 0.5 | -225 | 71% | 0 | +0.0% | ❌ |
| Alec Bohm | H+R+RBI | Over | 1.5 | -122 | 56% | 3 | +2.9% | ✅ |
| Jac Caglianone | RBI | Under | 0.5 | -170 | 64% | 2 | +1.7% | ❌ |
| Jared Young | H+R+RBI | Over | 1.5 | +111 | 48% | 0 | -2.8% | ❌ |
| Xavier Edwards | RBI | Over | 0.5 | +250 | 29% | 0 | -27.1% | ❌ |
| Javier Sanoja | H+R+RBI | Over | 1.5 | +106 | 49% | 4 | — | ✅ |
| Esmerlyn Valdez | Hits | Over | 0.5 | -162 | 63% | 0 | +3.8% | ❌ |
| Jonah Heim | RBI | Over | 0.5 | +240 | 30% | 0 | — | ❌ |
| Coby Mayo | Hits | Over | 0.5 | -128 | 57% | 2 | — | ✅ |
| Royce Lewis | RBI | Under | 0.5 | -219 | 70% | 1 | +0.7% | ❌ |
| Nick Gonzales | H+R+RBI | Over | 1.5 | -124 | 56% | 2 | +0.0% | ✅ |
| Tyler O'Neill | H+R+RBI | Under | 1.5 | -173 | 64% | 2 | — | ❌ |
| Michael Harris II | RBI | Under | 0.5 | -173 | 64% | 0 | +0.0% | ✅ |
| Ildemaro Vargas | H+R+RBI | Over | 1.5 | +104 | 50% | 1 | +2.0% | ❌ |
| Michael Busch | H+R+RBI | Over | 1.5 | -121 | 56% | 0 | +0.0% | ❌ |
| Caleb Durbin | H+R+RBI | Over | 1.5 | -114 | 54% | 6 | +0.0% | ✅ |
| Bo Bichette | Hits | Over | 0.5 | -272 | 74% | 1 | -1.0% | ✅ |
| Bo Bichette | RBI | Over | 0.5 | +195 | 34% | 1 | -4.8% | ✅ |
| Andy Pages | H+R+RBI | Under | 2.5 | -129 | 57% | 7 | -3.5% | ❌ |
| Byron Buxton | H+R+RBI | Under | 1.5 | +110 | 48% | 2 | +1.4% | ❌ |
| Jeff McNeil | H+R+RBI | Under | 1.5 | -117 | 55% | 3 | -2.9% | ❌ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +159 | 39% | 3 | +5.7% | ✅ |
| Alec Bohm | Hits | Over | 0.5 | -234 | 71% | 1 | +1.9% | ✅ |
| Justin Crawford | Hits | Over | 0.5 | -184 | 66% | 1 | -0.8% | ✅ |
| Donovan Walton | H+R+RBI | Under | 1.5 | -176 | 65% | 2 | — | ❌ |
| Lawrence Butler | RBI | Under | 0.5 | -293 | 76% | 0 | +0.4% | ✅ |
| Liam Hicks | Hits | Over | 0.5 | -206 | 68% | 0 | -32.5% | ❌ |
| Ryan Jeffers | H+R+RBI | Over | 1.5 | -112 | 54% | 1 | -0.8% | ❌ |
| Cedric Mullins | H+R+RBI | Over | 1.5 | +124 | 45% | 1 | +22.2% | ❌ |
| Tommy Edman | RBI | Under | 0.5 | -193 | 67% | 0 | +1.2% | ✅ |
| Javier Sanoja | Hits | Over | 0.5 | -216 | 69% | 2 | — | ✅ |
| Carson Kelly | H+R+RBI | Over | 1.5 | +119 | 46% | 2 | -3.5% | ✅ |
| Caleb Durbin | Hits | Under | 0.5 | +163 | 38% | 3 | -3.0% | ❌ |
| Spencer Torkelson | Hits | Under | 0.5 | +127 | 44% | 0 | — | ✅ |
| Janson Junk | Ks (P) | Over | 3.5 | +127 | 44% | 2 | +28.3% | ❌ |
| Mookie Betts | RBI | Under | 0.5 | -177 | 64% | 2 | +0.0% | ❌ |
| Brooks Lee | Hits | Under | 0.5 | +125 | 45% | 0 | -0.9% | ✅ |
| Tim Tawa | RBI | Over | 0.5 | +256 | 28% | 0 | -2.2% | ❌ |
| Luke Keaschall | Hits | Under | 0.5 | +140 | 42% | 2 | -8.8% | ❌ |
| Freddie Freeman | Hits | Over | 1.5 | +123 | 45% | 3 | +2.3% | ✅ |
| Josh Bell | Hits | Over | 0.5 | -198 | 67% | 2 | +0.3% | ✅ |
| Nico Hoerner | Hits | Over | 0.5 | -237 | 71% | 4 | -1.2% | ✅ |
| Connor Norby | RBI | Under | 0.5 | -355 | 78% | 0 | -1.3% | ✅ |
| Andy Pages | Hits | Under | 1.5 | -185 | 65% | 3 | +0.0% | ❌ |
| J.T. Realmuto | H+R+RBI | Under | 1.5 | -113 | 53% | 2 | +4.7% | ❌ |
| A.J. Ewing | Hits | Over | 0.5 | -214 | 68% | 1 | -3.4% | ✅ |
| Martin Perez | Ks (P) | Over | 3.5 | -117 | 54% | 3 | +0.8% | ❌ |
| Jackson Holliday | H+R+RBI | Under | 1.5 | -172 | 63% | 2 | — | ❌ |
| Bobby Witt Jr. | Hits | Under | 1.5 | -231 | 70% | 3 | +1.3% | ❌ |
| Luis Rengifo | RBI | Over | 0.5 | +290 | 26% | 0 | +2.4% | ❌ |
| Shohei Ohtani | Hits | Under | 1.5 | -151 | 60% | 4 | -1.4% | ❌ |
| Luke Keaschall | RBI | Under | 0.5 | -334 | 77% | 0 | +4.1% | ✅ |
| Luis Campusano | RBI | Over | 0.5 | +259 | 28% | 0 | +0.3% | ❌ |
| Donovan Walton | RBI | Under | 0.5 | -391 | 80% | 0 | +1.1% | ✅ |
| TJ Rumfield | H+R+RBI | Over | 1.5 | -109 | 52% | 2 | -2.2% | ✅ |
| Royce Lewis | Hits | Over | 0.5 | -205 | 67% | 1 | -0.3% | ✅ |
| Michael Wacha | Ks (P) | Under | 4.5 | -120 | 54% | 3 | +0.8% | ✅ |
| Kyle Schwarber | RBI | Under | 0.5 | -157 | 61% | 1 | +11.7% | ❌ |
| Austin Riley | H+R+RBI | Over | 1.5 | -104 | 51% | 2 | -1.9% | ✅ |
| Jeff McNeil | RBI | Over | 0.5 | +267 | 27% | 1 | +14.3% | ✅ |
| Carlos Narvaez | Hits | Under | 0.5 | -135 | 57% | 0 | +18.8% | ✅ |
| Gunnar Henderson | Hits | Over | 0.5 | -156 | 61% | 2 | — | ✅ |
| Jake Cronenworth | RBI | Under | 0.5 | -346 | 77% | 0 | +1.1% | ✅ |
| Junior Caminero | Hits | Over | 0.5 | -267 | 72% | 1 | -31.3% | ✅ |
| Cedric Mullins | Hits | Under | 0.5 | +112 | 47% | 1 | — | ❌ |
| Ezequiel Tovar | Hits | Over | 0.5 | -125 | 55% | 0 | -0.7% | ❌ |
| Pete Crow-Armstrong | Hits | Over | 0.5 | -261 | 72% | 4 | — | ✅ |
| Carlos Narvaez | RBI | Under | 0.5 | -547 | 84% | 0 | +3.5% | ✅ |
| Corbin Carroll | H+R+RBI | Over | 1.5 | -134 | 57% | 0 | -1.6% | ❌ |
| Kyle Tucker | RBI | Under | 0.5 | -194 | 65% | 0 | -1.4% | ✅ |
| Cole Carrigg | Hits | Over | 0.5 | -236 | 70% | 0 | +0.0% | ❌ |
| Shane McClanahan | Ks (P) | Over | 4.5 | -123 | 55% | 3 | — | ❌ |
| Andruw Monasterio | Hits | Over | 0.5 | -173 | 63% | 0 | -3.8% | ❌ |
| Yandy Diaz | Hits | Over | 1.5 | +168 | 37% | 2 | +46.2% | ✅ |
| Willson Contreras | H+R+RBI | Over | 1.5 | -131 | 56% | 5 | +1.6% | ✅ |
| Geraldo Perdomo | RBI | Over | 0.5 | +262 | 27% | 1 | +3.1% | ✅ |
| Leody Taveras | RBI | Over | 0.5 | +286 | 26% | 0 | — | ❌ |
| Shota Imanaga | Ks (P) | Under | 5.5 | -102 | 50% | 10 | +2.4% | ❌ |
| Brett Sullivan | H+R+RBI | Over | 1.5 | +131 | 43% | 2 | -0.9% | ✅ |
| Tyler O'Neill | RBI | Under | 0.5 | -351 | 77% | 0 | +11.4% | ✅ |
| Munetaka Murakami | Hits | Over | 0.5 | -142 | 58% | 0 | +0.0% | ❌ |
| Jonah Heim | H+R+RBI | Under | 1.5 | -166 | 62% | 0 | — | ✅ |
| Ildemaro Vargas | Hits | Under | 0.5 | +143 | 41% | 0 | -4.3% | ✅ |
| Zach McKinstry | H+R+RBI | Under | 1.5 | -142 | 58% | 5 | -2.1% | ❌ |
| Bryan Reynolds | RBI | Over | 0.5 | +199 | 33% | 0 | +1.7% | ❌ |
| Manny Machado | H+R+RBI | Under | 1.5 | -121 | 54% | 1 | +3.2% | ✅ |
| Andre Pallante | Ks (P) | Under | 4.5 | -115 | 53% | 5 | — | ❌ |
| Ronald Acuna Jr. | Hits | Under | 1.5 | -258 | 71% | 1 | +1.2% | ✅ |
| Ty France | RBI | Under | 0.5 | -281 | 72% | 0 | +1.4% | ✅ |
| Jac Caglianone | Hits | Under | 1.5 | -213 | 67% | 3 | +3.0% | ❌ |
| Tyler O'Neill | Hits | Under | 0.5 | +101 | 49% | 2 | +37.2% | ❌ |
| Zack Gelof | RBI | Under | 0.5 | -245 | 70% | 0 | -1.2% | ✅ |
| Brandon Young | Ks (P) | Over | 3.5 | -127 | 55% | 3 | +4.3% | ❌ |
| Ty France | Hits | Under | 0.5 | +150 | 39% | 1 | +4.2% | ❌ |
| Carlos Cortes | RBI | Over | 0.5 | +233 | 29% | 0 | +2.5% | ❌ |
| Trea Turner | Hits | Under | 1.5 | -244 | 69% | 1 | — | ✅ |
| Teoscar Hernandez | H+R+RBI | Under | 1.5 | +120 | 44% | 0 | +0.5% | ✅ |
| Drake Baldwin | RBI | Over | 0.5 | +157 | 38% | 0 | +0.4% | ❌ |
| Drake Baldwin | Hits | Over | 1.5 | +177 | 35% | 2 | +2.2% | ✅ |
| Geraldo Perdomo | Hits | Over | 0.5 | -244 | 69% | 0 | +0.9% | ❌ |
| Walker Buehler | Ks (P) | Under | 3.5 | +122 | 44% | 4 | — | ❌ |
| Mike Yastrzemski | Hits | Over | 0.5 | -140 | 57% | 0 | +3.1% | ❌ |
| Gavin Sheets | RBI | Under | 0.5 | -373 | 77% | 0 | +0.2% | ✅ |
| Randal Grichuk | Hits | Under | 0.5 | +110 | 46% | 1 | +0.0% | ❌ |
| Luis Castillo | Ks (P) | Over | 4.5 | -126 | 54% | 1 | -1.8% | ❌ |
| Josh Bell | H+R+RBI | Over | 1.5 | -110 | 51% | 5 | -1.8% | ✅ |
| Xander Bogaerts | H+R+RBI | Under | 1.5 | -162 | 60% | 0 | +2.3% | ✅ |
| Bryson Stott | RBI | Under | 0.5 | -217 | 66% | 0 | +7.1% | ✅ |
| Mookie Betts | Hits | Under | 1.5 | -217 | 66% | 1 | -1.4% | ✅ |
| Miguel Vargas | RBI | Over | 0.5 | +165 | 36% | 0 | +0.0% | ❌ |
| Fernando Tatis Jr. | RBI | Under | 0.5 | -259 | 70% | 1 | +1.4% | ❌ |
| Geraldo Perdomo | H+R+RBI | Under | 1.5 | -103 | 49% | 1 | +0.0% | ✅ |
| Ronald Acuna Jr. | RBI | Under | 0.5 | -210 | 65% | 2 | +0.0% | ❌ |
| Ian Happ | RBI | Under | 0.5 | -256 | 69% | 0 | +0.0% | ✅ |
| Luis Campusano | H+R+RBI | Over | 1.5 | +126 | 43% | 0 | -1.7% | ❌ |
| Fernando Tatis Jr. | H+R+RBI | Over | 1.5 | -130 | 55% | 1 | -2.8% | ❌ |
| Henry Bolte | Hits | Under | 0.5 | +136 | 41% | 1 | -17.2% | ❌ |
| Corbin Carroll | Hits | Over | 0.5 | -246 | 68% | 0 | -1.6% | ❌ |
| Jake Mangum | Hits | Under | 0.5 | +183 | 34% | 0 | +2.5% | ✅ |
| J.T. Realmuto | RBI | Under | 0.5 | -253 | 69% | 0 | +0.8% | ✅ |
| Jake Mangum | H+R+RBI | Over | 1.5 | -112 | 51% | 2 | -2.2% | ✅ |
| Ty France | H+R+RBI | Under | 1.5 | -127 | 54% | 1 | +2.7% | ✅ |
| Luis Arraez | RBI | Under | 0.5 | -228 | 67% | 1 | +6.5% | ❌ |
| Kyle Tucker | H+R+RBI | Under | 1.5 | +121 | 44% | 0 | -0.5% | ✅ |
| Trea Turner | RBI | Under | 0.5 | -256 | 69% | 1 | +6.7% | ❌ |
| Marcus Semien | Hits | Over | 0.5 | -167 | 60% | 1 | -1.9% | ✅ |
| Matt Olson | RBI | Under | 0.5 | -171 | 60% | 0 | +0.0% | ✅ |
| Carson Kelly | Hits | Under | 0.5 | +116 | 44% | 1 | +5.4% | ❌ |
| Ronald Acuna Jr. | H+R+RBI | Over | 1.5 | -158 | 59% | 3 | -1.5% | ✅ |
| Michael Harris II | Hits | Over | 1.5 | +177 | 34% | 1 | +0.0% | ❌ |
| Justin Crawford | H+R+RBI | Under | 1.5 | -136 | 55% | 2 | +1.2% | ❌ |
| Ryan Jeffers | Hits | Under | 0.5 | +157 | 37% | 0 | +2.4% | ✅ |
| A.J. Ewing | RBI | Over | 0.5 | +274 | 26% | 0 | -3.9% | ❌ |
| Luke Keaschall | H+R+RBI | Under | 1.5 | -142 | 56% | 3 | -10.0% | ❌ |
| Drake Baldwin | H+R+RBI | Under | 2.5 | -161 | 59% | 3 | -1.2% | ❌ |
| Kyle Tucker | Hits | Under | 0.5 | +200 | 32% | 0 | — | ✅ |
| Colt Keith | H+R+RBI | Over | 1.5 | +100 | 48% | 3 | +2.0% | ✅ |
| Braden Montgomery | Hits | Over | 0.5 | -149 | 57% | 1 | +0.0% | ✅ |
| Royce Lewis | H+R+RBI | Under | 1.5 | -112 | 50% | 2 | +4.0% | ❌ |
| Jackson Merrill | H+R+RBI | Over | 1.5 | -113 | 50% | 1 | -1.3% | ❌ |
| Henry Bolte | H+R+RBI | Over | 1.5 | +108 | 46% | 1 | +11.7% | ❌ |
| Andruw Monasterio | H+R+RBI | Under | 1.5 | -136 | 55% | 1 | +3.3% | ✅ |
| Zach McKinstry | Hits | Under | 0.5 | +134 | 40% | 3 | -2.1% | ❌ |
| Adley Rutschman | H+R+RBI | Over | 1.5 | -120 | 52% | 4 | +0.0% | ✅ |
| TJ Rumfield | RBI | Over | 0.5 | +189 | 33% | 0 | -4.6% | ❌ |
| Ceddanne Rafaela | Hits | Over | 1.5 | +201 | 31% | 3 | +0.7% | ✅ |
| Xander Bogaerts | RBI | Over | 0.5 | +259 | 26% | 0 | +0.3% | ❌ |
| Marcus Semien | H+R+RBI | Over | 1.5 | +113 | 44% | 1 | -0.9% | ❌ |
| Ozzie Albies | RBI | Over | 0.5 | +180 | 34% | 0 | -4.4% | ❌ |
| Heriberto Hernandez | Hits | Under | 0.5 | +128 | 41% | 0 | +19.4% | ✅ |
| Cristopher Sanchez | Ks (P) | Under | 6.5 | +112 | 44% | 6 | — | ✅ |
| Willi Castro | RBI | Over | 0.5 | +191 | 32% | 0 | +4.7% | ❌ |
| Brenton Doyle | Hits | Under | 0.5 | +100 | 47% | 0 | -4.8% | ✅ |
| Henry Davis | RBI | Over | 0.5 | +246 | 27% | 1 | +0.3% | ✅ |
| Brooks Lee | H+R+RBI | Over | 1.5 | +116 | 43% | 0 | -2.3% | ❌ |
| A.J. Ewing | H+R+RBI | Over | 1.5 | -110 | 49% | 2 | -3.6% | ✅ |
| Michael Busch | RBI | Over | 0.5 | +170 | 35% | 0 | +0.0% | ❌ |
| Jackson Merrill | RBI | Over | 0.5 | +182 | 33% | 0 | -2.1% | ❌ |
| Tim Tawa | Hits | Under | 0.5 | +119 | 42% | 2 | +1.9% | ❌ |
| Jakob Marsee | RBI | Over | 0.5 | +299 | 23% | 0 | — | ❌ |
| Mike Yastrzemski | H+R+RBI | Over | 1.5 | +118 | 42% | 0 | +1.4% | ❌ |
| Bryson Stott | H+R+RBI | Under | 1.5 | +104 | 45% | 2 | +4.5% | ❌ |
| Esteury Ruiz | H+R+RBI | Under | 0.5 | +116 | 43% | 2 | +13.1% | ❌ |
| Tim Tawa | H+R+RBI | Over | 1.5 | +121 | 42% | 2 | -1.8% | ✅ |
| Carson Benge | RBI | Over | 0.5 | +200 | 31% | 0 | -4.2% | ❌ |
| Bryce Harper | RBI | Over | 0.5 | +151 | 37% | 0 | -13.4% | ❌ |
| Kevin McGonigle | RBI | Over | 0.5 | +184 | 32% | 2 | +1.8% | ✅ |
| Francisco Lindor | RBI | Over | 0.5 | +165 | 35% | 0 | -1.1% | ❌ |
| Cedric Mullins | RBI | Over | 0.5 | +231 | 28% | 0 | -26.4% | ❌ |
| Fernando Tatis Jr. | Hits | Under | 0.5 | +195 | 31% | 0 | +6.1% | ✅ |
| Willson Contreras | RBI | Over | 0.5 | +146 | 37% | 1 | +4.7% | ✅ |
| Junior Caminero | RBI | Over | 0.5 | +125 | 41% | 0 | -43.8% | ❌ |
| Andy Pages | RBI | Over | 0.5 | +117 | 42% | 2 | +4.3% | ✅ |
| Adley Rutschman | Hits | Under | 0.5 | +164 | 34% | 2 | +2.7% | ❌ |
| Ozzie Albies | Hits | Under | 0.5 | +155 | 36% | 1 | +4.9% | ❌ |
| Nick Gonzales | Hits | Over | 1.5 | +201 | 30% | 1 | — | ❌ |
| Wilyer Abreu | RBI | Over | 0.5 | +150 | 36% | 2 | +0.4% | ✅ |
| Jared Young | RBI | Over | 0.5 | +211 | 29% | 0 | -0.3% | ❌ |
| Brandon Marsh | RBI | Over | 0.5 | +183 | 32% | 0 | -2.4% | ❌ |
| Ryan Jeffers | RBI | Over | 0.5 | +181 | 32% | 0 | -1.4% | ❌ |
| Manny Machado | RBI | Over | 0.5 | +179 | 32% | 0 | -2.1% | ❌ |
| Marcus Semien | RBI | Over | 0.5 | +205 | 29% | 0 | -5.3% | ❌ |
| Austin Riley | RBI | Over | 0.5 | +171 | 33% | 0 | -2.5% | ❌ |
| Corbin Carroll | RBI | Over | 0.5 | +172 | 33% | 0 | -3.9% | ❌ |
| Coby Mayo | RBI | Over | 0.5 | +237 | 26% | 1 | — | ✅ |
| Andruw Monasterio | RBI | Over | 0.5 | +200 | 30% | 1 | -4.2% | ✅ |
| Josh Bell | RBI | Over | 0.5 | +174 | 32% | 2 | -1.1% | ✅ |
| Henry Bolte | RBI | Over | 0.5 | +245 | 26% | 0 | +3.6% | ❌ |
| Michael Conforto | RBI | Over | 0.5 | +231 | 26% | 0 | +5.4% | ❌ |
| Francisco Alvarez | RBI | Over | 0.5 | +224 | 27% | 0 | +1.6% | ❌ |
| Justin Crawford | RBI | Over | 0.5 | +261 | 24% | 0 | +0.3% | ❌ |
| Mike Yastrzemski | RBI | Over | 0.5 | +211 | 28% | 0 | +0.0% | ❌ |
| Ezequiel Tovar | RBI | Over | 0.5 | +239 | 25% | 1 | +0.9% | ✅ |
| Jake Mangum | RBI | Over | 0.5 | +251 | 24% | 0 | +5.1% | ❌ |
| Jackson Holliday | RBI | Over | 0.5 | +267 | 23% | 0 | -21.9% | ❌ |
| Jake Rogers | RBI | Over | 0.5 | +265 | 23% | 0 | +0.0% | ❌ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| St. Louis Cardinals @ Cincinnati Reds | **YRFI** | High | 65% | 54% | ✅ |
| Baltimore Orioles @ Tampa Bay Rays | **YRFI** | High | 58% | 50% | ❌ |
| Detroit Tigers @ Pittsburgh Pirates | **YRFI** | High | 73% | 49% | ✅ |
| Arizona Diamondbacks @ Boston Red Sox | **YRFI** | High | 66% | 50% | ❌ |
| San Diego Padres @ New York Mets | **YRFI** | High | 71% | 44% | ✅ |
| Los Angeles Dodgers @ Colorado Rockies | **NRFI** | High | 50% | 42% | ✅ |
| St. Louis Cardinals @ Cincinnati Reds | **YRFI** | Medium | 60% | 54% | ✅ |
| Miami Marlins @ Philadelphia Phillies | **YRFI** | Medium | 58% | 51% | ❌ |
| Athletics @ Kansas City Royals | **YRFI** | Medium | 58% | 50% | ✅ |
| Atlanta Braves @ Minnesota Twins | **YRFI** | Coin flip | 57% | 55% | ✅ |
| Chicago White Sox @ Chicago Cubs | **NRFI** | Coin flip | 52% | 52% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Munetaka Murakami | Chicago White Sox @ Chicago Cubs | 29% | ❌ |
| 2 | Kyle Schwarber | Miami Marlins @ Philadelphia Phillies | 28% | ❌ |
| 3 | Matt Olson | Atlanta Braves @ Minnesota Twins | 26% | ❌ |
| 4 | Max Muncy | Los Angeles Dodgers @ Colorado Rockies | 25% | ✅ |
| 5 | Shohei Ohtani | Los Angeles Dodgers @ Colorado Rockies | 24% | ✅ |
| 6 | Miguel Vargas | Chicago White Sox @ Chicago Cubs | 24% | ❌ |
| 8 | Jordan Walker | St. Louis Cardinals @ Cincinnati Reds | 22% | ❌ |
| 10 | Pete Crow-Armstrong | Chicago White Sox @ Chicago Cubs | 21% | ✅ |

*3 homered · model expected 2.0*

### 2026-08-16 — bets 8-2 (+4.46u) · props 345-326 · NRFI 8-7 · HR 2-6

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Miami Marlins ML | — | -122 | 9.5 | — | ✅ +0.82u |
| F5 Total | F5 Over 4.5 | 4.5 | -144 | 9.5 | — | ✅ +0.69u |
| Total | Under 10.5 | 10.5 | -112 | 9.1 | — | ✅ +0.89u |
| Moneyline | San Francisco Giants ML | — | -134 | 8.1 | -95.8% | ❌ -1.00u |
| Total | Under 9.5 | 9.5 | -103 | 6.3 | — | ✅ +0.97u |
| NRFI | NRFI | 0.5 | -184 | 6.1 | — | ✅ +0.54u |
| Total | Over 8.0 | 8.0 | -102 | 6.0 | — | ✅ +0.98u |
| F5 Total | F5 Over 4.5 | 4.5 | +116 | 6.0 | — | ❌ -1.00u |
| Moneyline | New York Mets ML | — | -175 | 5.1 | — | ✅ +0.57u |
| NRFI | NRFI | 0.5 | +100 | 5.0 | — | ✅ +1.00u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Jorge Barrosa | Hits | Under | 0.5 | -106 | 81% | 0 | — | ✅ |
| Edmundo Sosa | Hits | Under | 0.5 | +179 | 54% | 1 | — | ❌ |
| Hunter Dobbins | Ks (P) | Over | 3.5 | -128 | 78% | 7 | — | ✅ |
| Jonathan Aranda | RBI | Over | 0.5 | +246 | 39% | 0 | — | ❌ |
| Freddy Fermin | Hits | Under | 0.5 | +104 | 66% | 1 | — | ❌ |
| Ryan Johnson | Ks (P) | Under | 3.5 | +131 | 58% | 4 | — | ❌ |
| Caleb Durbin | Hits | Under | 0.5 | +171 | 49% | 1 | — | ❌ |
| Brandon Lowe | RBI | Over | 0.5 | +218 | 41% | 2 | — | ✅ |
| Lawrence Butler | Hits | Under | 0.5 | +152 | 52% | 2 | — | ❌ |
| Coby Mayo | H+R+RBI | Over | 0.5 | -124 | 73% | 3 | — | ✅ |
| Dylan Beavers | H+R+RBI | Over | 0.5 | -139 | 75% | 0 | — | ❌ |
| Brandon Lowe | H+R+RBI | Over | 1.5 | +115 | 60% | 5 | — | ✅ |
| Sean Burke | Ks (P) | Over | 5.5 | -123 | 70% | 2 | — | ❌ |
| Jorge Mateo | Hits | Under | 0.5 | +112 | 60% | 1 | — | ❌ |
| Freddy Peralta | Ks (P) | Under | 6.5 | -145 | 75% | 2 | — | ✅ |
| Yordan Alvarez | Hits | Over | 1.5 | +204 | 42% | 1 | — | ❌ |
| Brady House | RBI | Over | 0.5 | +308 | 31% | 0 | — | ❌ |
| Edmundo Sosa | H+R+RBI | Under | 1.5 | -105 | 64% | 1 | — | ✅ |
| Michael Conforto | Hits | Under | 0.5 | +107 | 60% | 0 | — | ✅ |
| Pete Alonso | H+R+RBI | Over | 1.5 | -105 | 64% | 4 | — | ✅ |
| Jorge Mateo | H+R+RBI | Under | 1.5 | -162 | 77% | 2 | — | ❌ |
| Austin Hedges | H+R+RBI | Over | 0.5 | -126 | 69% | 0 | — | ❌ |
| Brady House | H+R+RBI | Over | 0.5 | -154 | 75% | 0 | — | ❌ |
| Gunnar Henderson | H+R+RBI | Over | 1.5 | +116 | 57% | 1 | — | ❌ |
| Jake Bauers | H+R+RBI | Over | 0.5 | -171 | 77% | 7 | — | ✅ |
| Jackson Chourio | H+R+RBI | Over | 1.5 | +117 | 56% | 6 | — | ✅ |
| Jose Caballero | H+R+RBI | Over | 0.5 | -124 | 67% | 3 | — | ✅ |
| Esmerlyn Valdez | H+R+RBI | Over | 1.5 | +107 | 59% | 4 | — | ✅ |
| Otto Lopez | Hits | Over | 1.5 | +158 | 47% | 1 | — | ❌ |
| Alec Burleson | H+R+RBI | Over | 1.5 | -132 | 69% | 9 | — | ✅ |
| Jake Cronenworth | Hits | Under | 0.5 | +147 | 49% | 1 | — | ❌ |
| Austin Hedges | Hits | Over | 0.5 | +103 | 59% | 0 | — | ❌ |
| Travis Bazzana | H+R+RBI | Over | 0.5 | -180 | 77% | 0 | — | ❌ |
| Myles Straw | Hits | Under | 0.5 | -120 | 66% | 0 | — | ✅ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | -111 | 63% | 6 | — | ✅ |
| Jordan Walker | H+R+RBI | Over | 1.5 | -113 | 64% | 8 | — | ✅ |
| TJ Friedl | Hits | Under | 0.5 | -120 | 65% | 0 | — | ✅ |
| Andres Gimenez | RBI | Over | 0.5 | +343 | 27% | 1 | — | ✅ |
| Trent Grisham | H+R+RBI | Over | 0.5 | -161 | 74% | 0 | — | ❌ |
| Joey Ortiz | H+R+RBI | Over | 0.5 | -128 | 67% | 0 | — | ❌ |
| Jonathan Aranda | H+R+RBI | Over | 1.5 | +106 | 58% | 0 | — | ❌ |
| Chase Meidroth | RBI | Over | 0.5 | +278 | 32% | 0 | — | ❌ |
| Leody Taveras | H+R+RBI | Over | 0.5 | -184 | 77% | 3 | — | ✅ |
| Jake McCarthy | RBI | Over | 0.5 | +249 | 34% | 0 | — | ❌ |
| Teoscar Hernandez | H+R+RBI | Over | 0.5 | -150 | 71% | 1 | — | ✅ |
| Dylan Beavers | RBI | Over | 0.5 | +303 | 29% | 0 | — | ❌ |
| Esteury Ruiz | H+R+RBI | Under | 1.5 | -150 | 71% | 1 | — | ✅ |
| Taylor Trammell | H+R+RBI | Over | 0.5 | -142 | 70% | 0 | — | ❌ |
| William Contreras | H+R+RBI | Over | 0.5 | -178 | 76% | 1 | — | ✅ |
| Brooks Lee | H+R+RBI | Over | 1.5 | -101 | 60% | 6 | — | ✅ |
| Dylan Beavers | Hits | Over | 0.5 | -106 | 61% | 0 | — | ❌ |
| Jose Caballero | RBI | Over | 0.5 | +386 | 24% | 1 | — | ✅ |
| Mike Trout | Hits | Over | 0.5 | -191 | 78% | 0 | — | ❌ |
| Jeremy Pena | RBI | Over | 0.5 | +249 | 34% | 1 | — | ✅ |
| Christian Walker | H+R+RBI | Over | 1.5 | +121 | 53% | 0 | — | ❌ |
| Andres Gimenez | H+R+RBI | Over | 0.5 | -144 | 70% | 3 | — | ✅ |
| Travis Bazzana | Hits | Over | 0.5 | -137 | 68% | 0 | — | ❌ |
| Brooks Lee | RBI | Over | 0.5 | +225 | 36% | 4 | — | ✅ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +191 | 40% | 0 | — | ❌ |
| Christian Walker | RBI | Over | 0.5 | +227 | 36% | 0 | — | ❌ |
| Cam Smith | H+R+RBI | Over | 0.5 | -178 | 75% | 0 | — | ❌ |
| Leody Taveras | RBI | Over | 0.5 | +285 | 30% | 0 | — | ❌ |
| Carter Jensen | Hits | Under | 0.5 | +144 | 48% | 1 | — | ❌ |
| Christian Scott | Ks (P) | Under | 5.5 | +112 | 55% | 7 | — | ❌ |
| Drew Romo | Hits | Under | 0.5 | -115 | 62% | 1 | — | ❌ |
| Xander Bogaerts | Hits | Under | 0.5 | +134 | 50% | 1 | — | ❌ |
| Corbin Carroll | Hits | Under | 0.5 | +188 | 40% | 1 | — | ❌ |
| Dylan Cease | Ks (P) | Over | 8.5 | -113 | 62% | 10 | — | ✅ |
| Junior Caminero | H+R+RBI | Over | 1.5 | -126 | 65% | 0 | — | ❌ |
| CJ Abrams | H+R+RBI | Over | 1.5 | -114 | 62% | 0 | — | ❌ |
| A.J. Ewing | H+R+RBI | Under | 1.5 | +122 | 52% | 0 | — | ✅ |
| Nick Loftin | Hits | Under | 0.5 | +141 | 48% | 0 | — | ✅ |
| Heliot Ramos | H+R+RBI | Over | 0.5 | -167 | 72% | 1 | — | ✅ |
| Andrés Chaparro | H+R+RBI | Over | 0.5 | -136 | 66% | 0 | — | ❌ |
| Masyn Winn | RBI | Over | 0.5 | +268 | 31% | 0 | — | ❌ |
| Jorge Mateo | RBI | Under | 0.5 | -306 | 87% | 1 | — | ❌ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +107 | 55% | 0 | — | ❌ |
| Austin Wells | H+R+RBI | Over | 0.5 | -105 | 59% | 0 | — | ❌ |
| Pete Alonso | Hits | Over | 0.5 | -196 | 76% | 1 | — | ✅ |
| Lawrence Butler | H+R+RBI | Under | 1.5 | -123 | 63% | 5 | — | ❌ |
| Brooks Lee | Hits | Over | 0.5 | -198 | 76% | 1 | — | ✅ |
| Elias Diaz | H+R+RBI | Under | 1.5 | -137 | 66% | 0 | — | ✅ |
| Jeremy Pena | H+R+RBI | Over | 1.5 | -123 | 63% | 3 | — | ✅ |
| Tristan Peters | H+R+RBI | Over | 0.5 | -181 | 73% | 3 | — | ✅ |
| Byron Buxton | H+R+RBI | Over | 1.5 | -130 | 64% | 0 | — | ❌ |
| Jorge Barrosa | H+R+RBI | Under | 0.5 | +116 | 53% | 0 | — | ✅ |
| Brayan Rocchio | Hits | Over | 0.5 | -152 | 69% | 0 | — | ❌ |
| Brandon Marsh | Hits | Over | 0.5 | -185 | 74% | 0 | — | ❌ |
| Jonah Heim | Hits | Under | 0.5 | +186 | 40% | 0 | — | ✅ |
| Brandon Nimmo | Hits | Over | 0.5 | -267 | 82% | 1 | — | ✅ |
| Ke'Bryan Hayes | Hits | Under | 0.5 | -128 | 64% | 0 | — | ✅ |
| Mike Trout | H+R+RBI | Over | 1.5 | -115 | 60% | 0 | — | ❌ |
| Justin Foscue | H+R+RBI | Under | 1.5 | -148 | 68% | 1 | — | ✅ |
| Logan Henderson | Ks (P) | Over | 5.5 | +108 | 54% | 6 | — | ✅ |
| Freddie Freeman | Hits | Over | 0.5 | -175 | 72% | 0 | — | ❌ |
| Henry Davis | H+R+RBI | Over | 0.5 | -162 | 70% | 1 | — | ✅ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | -101 | 57% | 4 | — | ✅ |
| James McCann | RBI | Over | 0.5 | +234 | 34% | 0 | — | ❌ |
| Alec Burleson | Hits | Over | 0.5 | -265 | 82% | 3 | — | ✅ |
| Colton Cowser | H+R+RBI | Over | 0.5 | -136 | 65% | 5 | — | ✅ |
| Ivan Herrera | H+R+RBI | Over | 1.5 | -105 | 57% | 3 | — | ✅ |
| Seiya Suzuki | RBI | Over | 0.5 | +168 | 42% | 0 | — | ❌ |
| Ezequiel Tovar | H+R+RBI | Over | 0.5 | -168 | 70% | 0 | — | ❌ |
| Isaac Paredes | RBI | Over | 0.5 | +209 | 36% | 0 | — | ❌ |
| Dansby Swanson | Hits | Under | 0.5 | +124 | 50% | 0 | — | ✅ |
| Michael Conforto | H+R+RBI | Under | 1.5 | -156 | 68% | 0 | — | ✅ |
| Gleyber Torres | RBI | Over | 0.5 | +247 | 32% | 0 | — | ❌ |
| Esteury Ruiz | RBI | Under | 0.5 | -317 | 85% | 0 | — | ✅ |
| Braden Montgomery | RBI | Over | 0.5 | +233 | 33% | 0 | — | ❌ |
| Jared Young | RBI | Under | 0.5 | -192 | 73% | 1 | — | ❌ |
| Yandy Diaz | RBI | Over | 0.5 | +197 | 38% | 0 | — | ❌ |
| Kazuma Okamoto | H+R+RBI | Over | 1.5 | +126 | 49% | 3 | — | ✅ |
| Dylan Crews | Hits | Under | 0.5 | +135 | 47% | 0 | — | ✅ |
| Jose Siri | Hits | Under | 0.5 | -123 | 61% | 0 | — | ✅ |
| Bryan Reynolds | Hits | Over | 0.5 | -227 | 77% | 2 | — | ✅ |
| Brandon Marsh | H+R+RBI | Over | 1.5 | +100 | 56% | 0 | — | ❌ |
| Zach McKinstry | Hits | Under | 0.5 | +130 | 48% | 0 | — | ✅ |
| Jake Irvin | Ks (P) | Over | 4.5 | +136 | 47% | 6 | — | ✅ |
| Jared Young | H+R+RBI | Under | 1.5 | -101 | 56% | 4 | — | ❌ |
| JJ Wetherholt | H+R+RBI | Over | 1.5 | -107 | 57% | 6 | — | ✅ |
| Alec Burleson | RBI | Over | 0.5 | +157 | 43% | 4 | — | ✅ |
| Yordan Alvarez | H+R+RBI | Over | 1.5 | -150 | 66% | 1 | — | ❌ |
| Spencer Torkelson | Hits | Under | 0.5 | +117 | 51% | 0 | — | ✅ |
| Zach McKinstry | H+R+RBI | Under | 1.5 | -148 | 66% | 1 | — | ✅ |
| Gary Sanchez | H+R+RBI | Over | 0.5 | -173 | 70% | 0 | — | ❌ |
| Jackson Chourio | Hits | Over | 0.5 | -172 | 70% | 3 | — | ✅ |
| Otto Lopez | H+R+RBI | Over | 1.5 | -168 | 69% | 2 | — | ✅ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | -133 | 63% | 2 | — | ✅ |
| Jarren Duran | Hits | Under | 0.5 | +139 | 46% | 1 | — | ❌ |
| Pete Alonso | RBI | Over | 0.5 | +175 | 40% | 2 | — | ✅ |
| Isaac Paredes | H+R+RBI | Over | 1.5 | +106 | 53% | 1 | — | ❌ |
| Cal Raleigh | H+R+RBI | Over | 0.5 | -152 | 66% | 3 | — | ✅ |
| Jac Caglianone | Hits | Over | 0.5 | -245 | 78% | 0 | — | ❌ |
| Jimmy Crooks | H+R+RBI | Over | 0.5 | -140 | 64% | 4 | — | ✅ |
| Jacob Lopez | Ks (P) | Over | 4.5 | -142 | 64% | 6 | — | ✅ |
| Rhys Hoskins | Hits | Under | 0.5 | +105 | 53% | 0 | — | ✅ |
| Braden Montgomery | H+R+RBI | Over | 1.5 | +101 | 55% | 1 | — | ❌ |
| Nolan Arenado | Hits | Under | 0.5 | +145 | 45% | 0 | — | ✅ |
| Jake Bauers | RBI | Over | 0.5 | +246 | 32% | 2 | — | ✅ |
| James McCann | H+R+RBI | Over | 1.5 | +115 | 51% | 2 | — | ✅ |
| Jose Altuve | H+R+RBI | Over | 1.5 | +107 | 53% | 1 | — | ❌ |
| Kazuma Okamoto | RBI | Over | 0.5 | +225 | 34% | 0 | — | ❌ |
| Matt McLain | Hits | Under | 0.5 | -108 | 57% | 0 | — | ✅ |
| Josh Bell | H+R+RBI | Over | 1.5 | -125 | 61% | 2 | — | ✅ |
| Javier Baez | Hits | Over | 0.5 | -168 | 68% | 0 | — | ❌ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -109 | 57% | 0 | — | ❌ |
| CJ Abrams | RBI | Over | 0.5 | +171 | 40% | 0 | — | ❌ |
| Bryson Stott | Hits | Under | 0.5 | +172 | 40% | 1 | — | ❌ |
| Luis Robert Jr. | Hits | Under | 0.5 | +127 | 48% | 1 | — | ❌ |
| Wyatt Langford | H+R+RBI | Under | 2.5 | -150 | 65% | 1 | — | ✅ |
| Trevor Larnach | RBI | Over | 0.5 | +244 | 32% | 0 | — | ❌ |
| Alex Bregman | H+R+RBI | Over | 1.5 | -126 | 61% | 0 | — | ❌ |
| Esteury Ruiz | Hits | Under | 0.5 | +116 | 50% | 1 | — | ❌ |
| Jonathan Aranda | Hits | Over | 0.5 | -183 | 70% | 0 | — | ❌ |
| Yandy Diaz | H+R+RBI | Over | 1.5 | -148 | 65% | 1 | — | ❌ |
| Tommy Edman | Hits | Under | 0.5 | +140 | 45% | 0 | — | ✅ |
| Matt Olson | H+R+RBI | Over | 1.5 | -128 | 61% | 5 | — | ✅ |
| Jose Ramirez | Hits | Under | 0.5 | +159 | 42% | 2 | — | ❌ |
| Eury Perez | Ks (P) | Over | 6.5 | -111 | 57% | 5 | — | ❌ |
| Munetaka Murakami | Hits | Over | 0.5 | -173 | 68% | 1 | — | ✅ |
| Jac Caglianone | H+R+RBI | Over | 1.5 | -132 | 62% | 0 | — | ❌ |
| Joey Ortiz | RBI | Over | 0.5 | +353 | 24% | 0 | — | ❌ |
| Ezequiel Duran | Hits | Under | 1.5 | -262 | 78% | 0 | — | ✅ |
| Gunnar Henderson | RBI | Over | 0.5 | +238 | 32% | 0 | — | ❌ |
| Colson Montgomery | H+R+RBI | Over | 1.5 | +124 | 48% | 3 | — | ✅ |
| Jordan Walker | RBI | Over | 0.5 | +165 | 41% | 4 | — | ✅ |
| Dominic Smith | RBI | Over | 0.5 | +257 | 30% | 0 | — | ❌ |
| Spencer Jones | H+R+RBI | Over | 0.5 | -121 | 59% | 0 | — | ❌ |
| Jordan Walker | Hits | Over | 0.5 | -221 | 74% | 3 | — | ✅ |
| Henry Bolte | Hits | Under | 0.5 | +195 | 36% | 3 | — | ❌ |
| Matt McLain | H+R+RBI | Over | 0.5 | -162 | 66% | 0 | — | ❌ |
| Miguel Vargas | H+R+RBI | Over | 1.5 | -107 | 56% | 3 | — | ✅ |
| Brayan Rocchio | RBI | Over | 0.5 | +291 | 28% | 0 | — | ❌ |
| Masyn Winn | H+R+RBI | Over | 1.5 | +123 | 48% | 1 | — | ❌ |
| Justin Foscue | RBI | Under | 0.5 | -284 | 79% | 0 | — | ✅ |
| Byron Buxton | Hits | Over | 0.5 | -225 | 74% | 0 | — | ❌ |
| Dean Kremer | Ks (P) | Over | 4.5 | +104 | 53% | 6 | — | ✅ |
| Colt Keith | H+R+RBI | Under | 1.5 | -147 | 64% | 5 | — | ❌ |
| Jorge Barrosa | RBI | Under | 0.5 | -428 | 87% | 0 | — | ✅ |
| Ryan McMahon | H+R+RBI | Over | 0.5 | -136 | 62% | 0 | — | ❌ |
| Kevin McGonigle | Hits | Over | 0.5 | -207 | 72% | 0 | — | ❌ |
| Colson Montgomery | RBI | Over | 0.5 | +198 | 36% | 1 | — | ✅ |
| Max Muncy | Hits | Under | 0.5 | +103 | 53% | 2 | — | ❌ |
| Rafael Devers | Hits | Over | 0.5 | -217 | 73% | 2 | — | ✅ |
| Gabriel Moreno | H+R+RBI | Over | 1.5 | -129 | 60% | 3 | — | ✅ |
| Ben Rice | H+R+RBI | Over | 1.5 | +117 | 49% | 4 | — | ✅ |
| Ozzie Albies | H+R+RBI | Over | 1.5 | +105 | 52% | 0 | — | ❌ |
| Daylen Lile | H+R+RBI | Over | 1.5 | +100 | 53% | 1 | — | ❌ |
| Luke Keaschall | H+R+RBI | Over | 1.5 | -107 | 55% | 0 | — | ❌ |
| Brett Sullivan | H+R+RBI | Over | 0.5 | -169 | 67% | 6 | — | ✅ |
| Christian Walker | Hits | Over | 0.5 | -162 | 66% | 0 | — | ❌ |
| Willi Castro | H+R+RBI | Over | 1.5 | +109 | 51% | 2 | — | ✅ |
| Freddie Freeman | H+R+RBI | Over | 1.5 | +110 | 51% | 0 | — | ❌ |
| Ivan Herrera | Hits | Over | 0.5 | -196 | 71% | 1 | — | ✅ |
| Colt Keith | RBI | Under | 0.5 | -294 | 80% | 1 | — | ❌ |
| Nick Lodolo | Ks (P) | Under | 4.5 | -104 | 54% | 2 | — | ✅ |
| Gabriel Moreno | Hits | Over | 0.5 | -270 | 78% | 1 | — | ✅ |
| Bryan Woo | Ks (P) | Under | 5.5 | -104 | 54% | 5 | — | ✅ |
| Francisco Lindor | H+R+RBI | Under | 2.5 | -154 | 64% | 2 | — | ✅ |
| Josh Bell | RBI | Over | 0.5 | +171 | 39% | 0 | — | ❌ |
| Gleyber Torres | Hits | Over | 0.5 | -216 | 73% | 2 | — | ✅ |
| Masyn Winn | Hits | Over | 0.5 | -160 | 65% | 0 | — | ❌ |
| Isaac Paredes | Hits | Over | 0.5 | -187 | 69% | 1 | — | ✅ |
| Brayan Rocchio | H+R+RBI | Over | 1.5 | +130 | 46% | 0 | — | ❌ |
| Austin Hedges | RBI | Over | 0.5 | +336 | 24% | 0 | — | ❌ |
| Zach McKinstry | RBI | Under | 0.5 | -325 | 81% | 0 | — | ✅ |
| Bryan Reynolds | RBI | Over | 0.5 | +212 | 34% | 2 | — | ✅ |
| Tristan Peters | Hits | Over | 0.5 | -144 | 62% | 1 | — | ✅ |
| Andrés Chaparro | Hits | Under | 0.5 | -120 | 58% | 0 | — | ✅ |
| Royce Lewis | H+R+RBI | Over | 1.5 | -130 | 60% | 2 | — | ✅ |
| Andruw Monasterio | H+R+RBI | Under | 1.5 | -151 | 64% | 0 | — | ✅ |
| Michael Soroka | Ks (P) | Over | 4.5 | +105 | 52% | 5 | — | ✅ |
| Willi Castro | Hits | Over | 0.5 | -180 | 68% | 1 | — | ✅ |
| Edward Cabrera | Ks (P) | Under | 3.5 | +122 | 48% | 2 | — | ✅ |
| Ben Rice | RBI | Over | 0.5 | +226 | 32% | 2 | — | ✅ |
| Elias Diaz | RBI | Under | 0.5 | -274 | 78% | 0 | — | ✅ |
| Chase Meidroth | Hits | Over | 0.5 | -195 | 70% | 0 | — | ❌ |
| Heriberto Hernandez | Hits | Under | 0.5 | +181 | 38% | 1 | — | ❌ |
| Edward Cabrera | Ks (P) | Under | 4.5 | -158 | 65% | 2 | — | ✅ |
| Jake Burger | Hits | Over | 0.5 | -251 | 76% | 3 | — | ✅ |
| Drake Baldwin | H+R+RBI | Over | 1.5 | -140 | 62% | 3 | — | ✅ |
| Coby Mayo | RBI | Over | 0.5 | +228 | 32% | 0 | — | ❌ |
| Ke'Bryan Hayes | RBI | Under | 0.5 | -418 | 85% | 0 | — | ✅ |
| Connor Wong | Hits | Under | 0.5 | -107 | 55% | 2 | — | ❌ |
| Junior Caminero | Hits | Over | 0.5 | -249 | 75% | 0 | — | ❌ |
| Sal Stewart | H+R+RBI | Over | 1.5 | -116 | 57% | 0 | — | ❌ |
| Cole Carrigg | RBI | Over | 0.5 | +245 | 30% | 2 | — | ✅ |
| James McCann | Hits | Over | 0.5 | -167 | 66% | 2 | — | ✅ |
| Rhys Hoskins | H+R+RBI | Under | 1.5 | -163 | 65% | 0 | — | ✅ |
| Joey Ortiz | Hits | Over | 0.5 | -105 | 54% | 0 | — | ❌ |
| Cam Smith | RBI | Over | 0.5 | +281 | 28% | 0 | — | ❌ |
| Oswald Peraza | H+R+RBI | Under | 1.5 | -152 | 64% | 0 | — | ✅ |
| Daulton Varsho | RBI | Under | 0.5 | -279 | 78% | 0 | — | ✅ |
| Oswald Peraza | RBI | Under | 0.5 | -316 | 80% | 0 | — | ✅ |
| Jake Irvin | Ks (P) | Over | 3.5 | -155 | 64% | 6 | — | ✅ |
| Cole Young | Hits | Over | 0.5 | -176 | 67% | 0 | — | ❌ |
| Rafael Devers | H+R+RBI | Over | 1.5 | -125 | 58% | 7 | — | ✅ |
| Esmerlyn Valdez | Hits | Over | 0.5 | -156 | 64% | 2 | — | ✅ |
| Yainer Diaz | RBI | Over | 0.5 | +268 | 28% | 0 | — | ❌ |
| Braden Montgomery | Hits | Over | 0.5 | -203 | 70% | 1 | — | ✅ |
| Jorbit Vivas | H+R+RBI | Over | 0.5 | -164 | 65% | 2 | — | ✅ |
| CJ Abrams | Hits | Over | 0.5 | -231 | 73% | 0 | — | ❌ |
| William Contreras | RBI | Over | 0.5 | +257 | 29% | 0 | — | ❌ |
| Gabriel Moreno | RBI | Over | 0.5 | +189 | 36% | 1 | — | ✅ |
| Gleyber Torres | H+R+RBI | Over | 1.5 | -116 | 56% | 3 | — | ✅ |
| Connor Norby | H+R+RBI | Under | 1.5 | -173 | 66% | 2 | — | ❌ |
| Bobby Witt Jr. | H+R+RBI | Under | 2.5 | -154 | 63% | 3 | — | ❌ |
| Xavier Edwards | Hits | Over | 0.5 | -255 | 75% | 1 | — | ✅ |
| Ernie Clement | Hits | Over | 0.5 | -187 | 68% | 0 | — | ❌ |
| Justin Foscue | Hits | Under | 0.5 | +113 | 49% | 1 | — | ❌ |
| Heliot Ramos | Hits | Over | 0.5 | -138 | 61% | 1 | — | ✅ |
| Brandon Nimmo | H+R+RBI | Over | 1.5 | -157 | 64% | 1 | — | ❌ |
| Andy Pages | H+R+RBI | Over | 1.5 | +108 | 50% | 3 | — | ✅ |
| Alejandro Kirk | RBI | Over | 0.5 | +235 | 31% | 0 | — | ❌ |
| Yainer Diaz | Hits | Over | 0.5 | -194 | 69% | 1 | — | ✅ |
| Zach Neto | H+R+RBI | Over | 1.5 | -123 | 58% | 0 | — | ❌ |
| Gavin Sheets | Hits | Under | 0.5 | +105 | 51% | 1 | — | ❌ |
| Travis Bazzana | RBI | Over | 0.5 | +279 | 28% | 0 | — | ❌ |
| Royce Lewis | Hits | Over | 0.5 | -236 | 73% | 1 | — | ✅ |
| Cole Young | H+R+RBI | Over | 1.5 | +116 | 48% | 0 | — | ❌ |
| Wilyer Abreu | Hits | Under | 0.5 | +160 | 40% | 0 | — | ✅ |
| Manny Machado | Hits | Under | 0.5 | +163 | 40% | 0 | — | ✅ |
| Drake Baldwin | RBI | Over | 0.5 | +189 | 36% | 1 | — | ✅ |
| Josh Bell | Hits | Over | 0.5 | -238 | 73% | 1 | — | ✅ |
| Andruw Monasterio | Hits | Under | 0.5 | +122 | 47% | 0 | — | ✅ |
| Zack Gelof | H+R+RBI | Over | 1.5 | -127 | 58% | 5 | — | ✅ |
| Trevor Larnach | H+R+RBI | Over | 1.5 | -113 | 55% | 1 | — | ❌ |
| Austin Riley | Hits | Over | 0.5 | -151 | 63% | 2 | — | ✅ |
| Caleb Durbin | H+R+RBI | Under | 1.5 | -116 | 56% | 1 | — | ✅ |
| Bryce Harper | Hits | Over | 0.5 | -250 | 74% | 1 | — | ✅ |
| Ernie Clement | H+R+RBI | Over | 1.5 | +112 | 49% | 1 | — | ❌ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -134 | 60% | 3 | — | ❌ |
| Jake Mangum | Hits | Under | 1.5 | -247 | 74% | 1 | — | ✅ |
| Jeremy Pena | Hits | Over | 0.5 | -254 | 74% | 1 | — | ✅ |
| Dansby Swanson | H+R+RBI | Over | 1.5 | +105 | 51% | 0 | — | ❌ |
| Nico Hoerner | RBI | Over | 0.5 | +216 | 33% | 0 | — | ❌ |
| Ceddanne Rafaela | Hits | Under | 1.5 | -247 | 74% | 0 | — | ✅ |
| Seiya Suzuki | Hits | Over | 0.5 | -221 | 71% | 1 | — | ✅ |
| Randy Arozarena | H+R+RBI | Over | 1.5 | +100 | 52% | 4 | — | ✅ |
| Dominic Canzone | Hits | Under | 0.5 | +118 | 47% | 2 | — | ❌ |
| Drew Gilbert | H+R+RBI | Under | 1.5 | -118 | 56% | 3 | — | ❌ |
| Trevor Larnach | Hits | Over | 0.5 | -193 | 68% | 1 | — | ✅ |
| Brandon Lowe | Hits | Over | 0.5 | -155 | 63% | 2 | — | ✅ |
| Ezequiel Tovar | Hits | Under | 0.5 | +103 | 51% | 0 | — | ✅ |
| Brady House | Hits | Over | 0.5 | -125 | 57% | 0 | — | ❌ |
| Dylan Crews | RBI | Under | 0.5 | -250 | 74% | 0 | — | ✅ |
| Bobby Witt Jr. | RBI | Under | 0.5 | -210 | 70% | 1 | — | ❌ |
| Austin Riley | H+R+RBI | Over | 1.5 | +118 | 47% | 4 | — | ✅ |
| Brendan Donovan | Hits | Under | 0.5 | +158 | 40% | 0 | — | ✅ |
| Taylor Trammell | Hits | Over | 0.5 | -109 | 54% | 0 | — | ❌ |
| JJ Wetherholt | Hits | Over | 0.5 | -193 | 68% | 2 | — | ✅ |
| Nick Loftin | H+R+RBI | Under | 1.5 | -138 | 60% | 0 | — | ✅ |
| Javier Baez | H+R+RBI | Over | 1.5 | +118 | 47% | 0 | — | ❌ |
| Nolan Arenado | RBI | Over | 0.5 | +197 | 35% | 0 | — | ❌ |
| Javier Sanoja | Hits | Over | 0.5 | -245 | 73% | 1 | — | ✅ |
| Brandon Nimmo | RBI | Under | 0.5 | -185 | 67% | 0 | — | ✅ |
| Spencer Jones | Hits | Under | 0.5 | -145 | 61% | 0 | — | ✅ |
| Edmundo Sosa | RBI | Under | 0.5 | -228 | 72% | 0 | — | ✅ |
| Carson Benge | RBI | Under | 0.5 | -207 | 69% | 0 | — | ✅ |
| Alec Bohm | Hits | Under | 1.5 | -260 | 74% | 2 | — | ❌ |
| Ian Happ | Hits | Over | 0.5 | -181 | 66% | 1 | — | ✅ |
| Hunter Brown | Ks (P) | Under | 5.5 | -102 | 52% | 5 | — | ✅ |
| Ketel Marte | RBI | Under | 0.5 | -174 | 65% | 0 | — | ✅ |
| Kazuma Okamoto | Hits | Over | 0.5 | -145 | 61% | 1 | — | ✅ |
| Justin Crawford | H+R+RBI | Under | 1.5 | -135 | 59% | 1 | — | ✅ |
| Connor Norby | RBI | Under | 0.5 | -357 | 80% | 0 | — | ✅ |
| Henry Bolte | H+R+RBI | Under | 1.5 | +102 | 51% | 4 | — | ❌ |
| Randy Arozarena | Hits | Over | 0.5 | -190 | 67% | 2 | — | ✅ |
| Henry Bolte | RBI | Under | 0.5 | -245 | 73% | 0 | — | ✅ |
| Jose Siri | RBI | Under | 0.5 | -356 | 80% | 0 | — | ✅ |
| Jackson Chourio | RBI | Over | 0.5 | +231 | 31% | 0 | — | ❌ |
| Ryan Weathers | Ks (P) | Over | 4.5 | -142 | 60% | 4 | — | ❌ |
| Ozzie Albies | RBI | Over | 0.5 | +212 | 33% | 0 | — | ❌ |
| Dominic Canzone | H+R+RBI | Under | 1.5 | -159 | 63% | 3 | — | ❌ |
| Gary Sanchez | Hits | Over | 0.5 | -135 | 59% | 0 | — | ❌ |
| Cole Carrigg | Hits | Under | 0.5 | +153 | 40% | 1 | — | ❌ |
| Zach Neto | Hits | Over | 0.5 | -211 | 69% | 0 | — | ❌ |
| Daulton Varsho | Hits | Under | 0.5 | +125 | 45% | 0 | — | ✅ |
| Yainer Diaz | H+R+RBI | Over | 1.5 | +111 | 48% | 1 | — | ❌ |
| Gavin Sheets | H+R+RBI | Under | 1.5 | -167 | 64% | 3 | — | ❌ |
| Josh Naylor | Hits | Over | 0.5 | -178 | 65% | 1 | — | ✅ |
| Gunnar Henderson | Hits | Over | 0.5 | -178 | 65% | 0 | — | ❌ |
| Patrick Sandoval | Ks (P) | Over | 5.5 | +126 | 45% | 6 | — | ✅ |
| TJ Friedl | RBI | Under | 0.5 | -428 | 83% | 0 | — | ✅ |
| Matt Olson | Hits | Over | 0.5 | -216 | 70% | 1 | — | ✅ |
| Jose Caballero | Hits | Over | 0.5 | +105 | 50% | 1 | — | ✅ |
| Yandy Diaz | Hits | Over | 1.5 | +179 | 36% | 1 | — | ❌ |
| Lawrence Butler | RBI | Under | 0.5 | -279 | 75% | 2 | — | ❌ |
| Sam Antonacci | H+R+RBI | Over | 1.5 | -106 | 52% | 2 | — | ✅ |
| Andy Pages | Hits | Over | 0.5 | -170 | 64% | 1 | — | ✅ |
| Wade Meckler | Hits | Over | 0.5 | -157 | 62% | 0 | — | ❌ |
| Leody Taveras | Hits | Over | 0.5 | -139 | 59% | 1 | — | ✅ |
| Nolan Arenado | H+R+RBI | Over | 1.5 | +100 | 51% | 0 | — | ❌ |
| Luis Arraez | H+R+RBI | Over | 1.5 | -157 | 62% | 2 | — | ✅ |
| William Contreras | Hits | Over | 0.5 | -145 | 60% | 1 | — | ✅ |
| Drake Baldwin | Hits | Over | 0.5 | -267 | 74% | 1 | — | ✅ |
| Sal Stewart | RBI | Over | 0.5 | +155 | 40% | 0 | — | ❌ |
| Max Muncy | RBI | Under | 0.5 | -252 | 73% | 0 | — | ✅ |
| A.J. Ewing | RBI | Under | 0.5 | -283 | 75% | 0 | — | ✅ |
| Keibert Ruiz | RBI | Under | 0.5 | -250 | 73% | 2 | — | ❌ |
| Michael Harris II | Hits | Over | 0.5 | -261 | 73% | 1 | — | ✅ |
| Jackson Holliday | Hits | Over | 0.5 | -147 | 60% | 2 | — | ✅ |
| Wyatt Langford | Hits | Under | 1.5 | -256 | 73% | 0 | — | ✅ |
| Kody Clemens | H+R+RBI | Over | 1.5 | -125 | 56% | 5 | — | ✅ |
| Munetaka Murakami | RBI | Over | 0.5 | +185 | 36% | 2 | — | ✅ |
| Alejandro Kirk | H+R+RBI | Over | 1.5 | +101 | 50% | 1 | — | ❌ |
| Corbin Carroll | RBI | Under | 0.5 | -208 | 68% | 0 | — | ✅ |
| Luis Garcia Jr. | H+R+RBI | Over | 1.5 | +116 | 47% | 2 | — | ✅ |
| Jimmy Crooks | Hits | Under | 0.5 | -120 | 55% | 2 | — | ❌ |
| Austin Wells | Hits | Over | 0.5 | +119 | 46% | 0 | — | ❌ |
| Shohei Ohtani | Hits | Over | 0.5 | -198 | 67% | 1 | — | ✅ |
| Andrew Benintendi | RBI | Over | 0.5 | +207 | 33% | 0 | — | ❌ |
| Vaughn Grissom | H+R+RBI | Over | 1.5 | -109 | 53% | 1 | — | ❌ |
| Connor Norby | Hits | Under | 0.5 | +107 | 49% | 1 | — | ❌ |
| Corbin Carroll | H+R+RBI | Under | 1.5 | +107 | 49% | 1 | — | ✅ |
| Ronald Acuna Jr. | H+R+RBI | Over | 1.5 | -126 | 56% | 2 | — | ✅ |
| Nico Hoerner | H+R+RBI | Over | 1.5 | -120 | 55% | 1 | — | ❌ |
| Ben Rice | Hits | Over | 0.5 | -153 | 61% | 1 | — | ✅ |
| Kyle Isbel | Hits | Over | 0.5 | -142 | 59% | 1 | — | ✅ |
| Xavier Edwards | H+R+RBI | Over | 1.5 | -129 | 57% | 2 | — | ✅ |
| Henry Davis | Hits | Under | 0.5 | -107 | 52% | 0 | — | ✅ |
| Francisco Lindor | RBI | Under | 0.5 | -186 | 66% | 0 | — | ✅ |
| JJ Wetherholt | RBI | Over | 0.5 | +236 | 30% | 1 | — | ✅ |
| Ketel Marte | Hits | Under | 0.5 | +184 | 36% | 0 | — | ✅ |
| Drew Romo | H+R+RBI | Over | 0.5 | -144 | 60% | 4 | — | ✅ |
| Vaughn Grissom | Hits | Under | 0.5 | +166 | 38% | 1 | — | ❌ |
| Ivan Herrera | RBI | Over | 0.5 | +221 | 31% | 1 | — | ✅ |
| Jose Altuve | Hits | Over | 0.5 | -199 | 67% | 1 | — | ✅ |
| Patrick Sandoval | Ks (P) | Over | 4.5 | -150 | 60% | 6 | — | ✅ |
| Freddy Fermin | RBI | Under | 0.5 | -384 | 80% | 0 | — | ✅ |
| Alex Bregman | Hits | Over | 0.5 | -226 | 70% | 0 | — | ❌ |
| Brett Baty | RBI | Under | 0.5 | -273 | 74% | 0 | — | ✅ |
| Dansby Swanson | RBI | Over | 0.5 | +204 | 33% | 0 | — | ❌ |
| Andrew Benintendi | Hits | Under | 0.5 | +141 | 42% | 0 | — | ✅ |
| Alex Bregman | RBI | Over | 0.5 | +170 | 37% | 0 | — | ❌ |
| Trent Grisham | Hits | Under | 0.5 | -111 | 53% | 0 | — | ✅ |
| Trent Grisham | RBI | Over | 0.5 | +243 | 29% | 0 | — | ❌ |
| Shohei Ohtani | H+R+RBI | Over | 1.5 | -115 | 54% | 1 | — | ❌ |
| Jake Burger | H+R+RBI | Over | 1.5 | -150 | 60% | 6 | — | ✅ |
| Austin Wells | RBI | Under | 0.5 | -480 | 83% | 0 | — | ✅ |
| Max Muncy | H+R+RBI | Under | 1.5 | -157 | 61% | 2 | — | ❌ |
| A.J. Ewing | Hits | Under | 1.5 | -290 | 75% | 0 | — | ✅ |
| Carson Benge | Hits | Over | 0.5 | -289 | 74% | 0 | — | ❌ |
| Jose Ramirez | RBI | Under | 0.5 | -245 | 71% | 0 | — | ✅ |
| Dominic Canzone | RBI | Under | 0.5 | -296 | 75% | 1 | — | ❌ |
| Luis Garcia Jr. | Hits | Under | 0.5 | +135 | 43% | 1 | — | ❌ |
| Myles Straw | RBI | Under | 0.5 | -545 | 85% | 0 | — | ✅ |
| Nick Fortes | Hits | Over | 0.5 | -154 | 61% | 1 | — | ✅ |
| Bryce Eldridge | Hits | Over | 0.5 | -202 | 67% | 1 | — | ✅ |
| Mike Yastrzemski | H+R+RBI | Under | 1.5 | -146 | 60% | 0 | — | ✅ |
| Wyatt Langford | RBI | Under | 0.5 | -197 | 66% | 0 | — | ✅ |
| Michael Conforto | RBI | Under | 0.5 | -291 | 75% | 0 | — | ✅ |
| Junior Caminero | RBI | Over | 0.5 | +145 | 41% | 0 | — | ❌ |
| Brett Baty | Hits | Under | 0.5 | +115 | 47% | 1 | — | ❌ |
| Brendan Donovan | H+R+RBI | Under | 1.5 | -124 | 55% | 0 | — | ✅ |
| Keibert Ruiz | Hits | Under | 0.5 | +142 | 41% | 2 | — | ❌ |
| Bobby Witt Jr. | Hits | Under | 1.5 | -211 | 68% | 1 | — | ✅ |
| Luis Torrens | RBI | Over | 0.5 | +252 | 28% | 2 | — | ✅ |
| Elly De La Cruz | H+R+RBI | Over | 1.5 | -111 | 53% | 0 | — | ❌ |
| Jung Hoo Lee | Hits | Over | 1.5 | +179 | 36% | 1 | — | ❌ |
| Andrew Vaughn | Hits | Over | 0.5 | -157 | 61% | 2 | — | ✅ |
| Colt Keith | Hits | Under | 0.5 | +131 | 43% | 2 | — | ❌ |
| Coby Mayo | Hits | Over | 0.5 | +104 | 49% | 1 | — | ✅ |
| Dylan Crews | H+R+RBI | Under | 1.5 | -139 | 58% | 0 | — | ✅ |
| Luke Keaschall | Hits | Over | 0.5 | -206 | 67% | 0 | — | ❌ |
| Nathan Church | Hits | Under | 0.5 | +139 | 42% | 0 | — | ✅ |
| Ronald Acuna Jr. | Hits | Over | 0.5 | -224 | 69% | 1 | — | ✅ |
| Jarren Duran | H+R+RBI | Under | 1.5 | -134 | 57% | 2 | — | ❌ |
| Connor Wong | RBI | Under | 0.5 | -411 | 80% | 3 | — | ❌ |
| Luis Robert Jr. | RBI | Under | 0.5 | -249 | 71% | 0 | — | ✅ |
| Dominic Smith | H+R+RBI | Over | 1.5 | +123 | 45% | 2 | — | ✅ |
| Luis Garcia Jr. | RBI | Over | 0.5 | +219 | 31% | 1 | — | ✅ |
| Spencer Jones | RBI | Over | 0.5 | +340 | 23% | 0 | — | ❌ |
| Dillon Dingler | H+R+RBI | Over | 1.5 | -125 | 55% | 2 | — | ✅ |
| Mookie Betts | Hits | Over | 0.5 | -169 | 62% | 1 | — | ✅ |
| Nathaniel Lowe | Hits | Over | 0.5 | -172 | 63% | 1 | — | ✅ |
| Kody Clemens | Hits | Over | 0.5 | -219 | 68% | 2 | — | ✅ |
| Kyle Schwarber | Hits | Over | 0.5 | -191 | 65% | 1 | — | ✅ |
| Mickey Moniak | Hits | Under | 0.5 | +144 | 41% | 1 | — | ❌ |
| Pete Crow-Armstrong | H+R+RBI | Over | 1.5 | -159 | 61% | 4 | — | ✅ |
| Colton Cowser | Hits | Under | 0.5 | -131 | 56% | 2 | — | ❌ |
| Jake Mangum | H+R+RBI | Over | 1.5 | -128 | 56% | 2 | — | ✅ |
| Wilyer Abreu | RBI | Under | 0.5 | -218 | 68% | 0 | — | ✅ |
| Bo Bichette | RBI | Under | 0.5 | -199 | 66% | 0 | — | ✅ |
| Tarik Skubal | Ks (P) | Under | 7.5 | -137 | 57% | 7 | — | ✅ |
| Carter Jensen | H+R+RBI | Under | 1.5 | -109 | 52% | 2 | — | ❌ |
| Anthony Seigler | RBI | Under | 0.5 | -360 | 78% | 0 | — | ✅ |
| Jung Hoo Lee | RBI | Under | 0.5 | -243 | 70% | 0 | — | ✅ |
| Michael Massey | RBI | Under | 0.5 | -266 | 72% | 1 | — | ❌ |
| Josh Naylor | H+R+RBI | Over | 1.5 | +110 | 47% | 1 | — | ❌ |
| JJ Bleday | RBI | Under | 0.5 | -258 | 71% | 0 | — | ✅ |
| Bryce Harper | RBI | Under | 0.5 | -186 | 64% | 0 | — | ✅ |
| Bryce Eldridge | RBI | Under | 0.5 | -245 | 70% | 1 | — | ❌ |
| Mike Yastrzemski | RBI | Under | 0.5 | -287 | 73% | 0 | — | ✅ |
| Mickey Moniak | H+R+RBI | Over | 1.5 | -106 | 51% | 4 | — | ✅ |
| Geraldo Perdomo | Hits | Over | 0.5 | -216 | 68% | 0 | — | ❌ |
| Gavin Sheets | RBI | Under | 0.5 | -329 | 76% | 1 | — | ❌ |
| Daulton Varsho | H+R+RBI | Under | 1.5 | -145 | 59% | 0 | — | ✅ |
| Jake McCarthy | H+R+RBI | Over | 1.5 | -129 | 56% | 3 | — | ✅ |
| Luis Arraez | Hits | Over | 1.5 | +155 | 39% | 1 | — | ❌ |
| Teoscar Hernandez | RBI | Under | 0.5 | -309 | 75% | 0 | — | ✅ |
| Jackson Merrill | Hits | Under | 0.5 | +166 | 37% | 1 | — | ❌ |
| Jake Mangum | RBI | Over | 0.5 | +268 | 27% | 0 | — | ❌ |
| Jackson Merrill | H+R+RBI | Over | 1.5 | -117 | 53% | 2 | — | ✅ |
| George Springer | H+R+RBI | Over | 1.5 | +103 | 49% | 0 | — | ❌ |
| Ty France | RBI | Under | 0.5 | -244 | 70% | 0 | — | ✅ |
| Justin Crawford | RBI | Under | 0.5 | -364 | 78% | 0 | — | ✅ |
| Ezequiel Duran | H+R+RBI | Over | 1.5 | -148 | 59% | 0 | — | ❌ |
| Rhys Hoskins | RBI | Under | 0.5 | -284 | 73% | 0 | — | ✅ |
| Tommy Edman | H+R+RBI | Under | 1.5 | -141 | 58% | 0 | — | ✅ |
| Michael Harris II | H+R+RBI | Over | 1.5 | -138 | 57% | 1 | — | ❌ |
| Julio Rodriguez | RBI | Under | 0.5 | -261 | 71% | 0 | — | ✅ |
| Geraldo Perdomo | H+R+RBI | Under | 1.5 | -106 | 51% | 0 | — | ✅ |
| Noah Cameron | Ks (P) | Over | 5.5 | -157 | 60% | 8 | — | ✅ |
| Rafael Devers | RBI | Over | 0.5 | +181 | 35% | 3 | — | ✅ |
| Ke'Bryan Hayes | H+R+RBI | Under | 0.5 | +102 | 49% | 0 | — | ✅ |
| Bryce Elder | Ks (P) | Over | 3.5 | -135 | 57% | 5 | — | ✅ |
| Jung Hoo Lee | H+R+RBI | Over | 1.5 | -143 | 58% | 1 | — | ❌ |
| Jackson Holliday | H+R+RBI | Over | 1.5 | +127 | 43% | 7 | — | ✅ |
| Jonny Deluca | H+R+RBI | Over | 1.5 | +107 | 48% | 0 | — | ❌ |
| Fernando Tatis Jr. | Hits | Under | 1.5 | -267 | 72% | 2 | — | ❌ |
| Ian Happ | RBI | Under | 0.5 | -246 | 70% | 0 | — | ✅ |
| Alec Bohm | H+R+RBI | Under | 1.5 | +101 | 49% | 8 | — | ❌ |
| Ian Happ | H+R+RBI | Over | 1.5 | -113 | 52% | 1 | — | ❌ |
| Brett Baty | H+R+RBI | Under | 1.5 | -149 | 59% | 2 | — | ❌ |
| Pete Crow-Armstrong | Hits | Under | 1.5 | -274 | 72% | 1 | — | ✅ |
| Chase DeLauter | H+R+RBI | Over | 1.5 | -121 | 54% | 0 | — | ❌ |
| Fernando Tatis Jr. | H+R+RBI | Over | 1.5 | -139 | 57% | 2 | — | ✅ |
| Victor Caratini | RBI | Over | 0.5 | +222 | 30% | 0 | — | ❌ |
| Andruw Monasterio | RBI | Under | 0.5 | -318 | 75% | 0 | — | ✅ |
| Elias Diaz | Hits | Under | 0.5 | +135 | 42% | 0 | — | ✅ |
| Myles Straw | H+R+RBI | Under | 0.5 | +101 | 49% | 0 | — | ✅ |
| Chase DeLauter | RBI | Over | 0.5 | +201 | 33% | 0 | — | ❌ |
| Victor Caratini | H+R+RBI | Over | 1.5 | +106 | 48% | 0 | — | ❌ |
| Luis Robert Jr. | H+R+RBI | Under | 1.5 | -132 | 56% | 1 | — | ✅ |
| Nick Fortes | H+R+RBI | Over | 1.5 | +124 | 44% | 1 | — | ❌ |
| Trevor Rogers | Ks (P) | Under | 4.5 | -138 | 57% | 6 | — | ❌ |
| Jonah Heim | H+R+RBI | Under | 1.5 | -104 | 50% | 0 | — | ✅ |
| Bryson Stott | RBI | Under | 0.5 | -226 | 68% | 0 | — | ✅ |
| George Springer | Hits | Over | 0.5 | -187 | 64% | 0 | — | ❌ |
| Mike Yastrzemski | Hits | Under | 0.5 | +118 | 45% | 0 | — | ✅ |
| Cole Young | RBI | Over | 0.5 | +245 | 28% | 0 | — | ❌ |
| Cole Carrigg | H+R+RBI | Over | 1.5 | -107 | 50% | 3 | — | ✅ |
| Luis Rengifo | Hits | Under | 0.5 | +171 | 36% | 2 | — | ❌ |
| Andrew Painter | Ks (P) | Over | 3.5 | -129 | 55% | 2 | — | ❌ |
| Teoscar Hernandez | Hits | Under | 0.5 | -109 | 51% | 1 | — | ❌ |
| Mookie Betts | H+R+RBI | Over | 1.5 | +110 | 46% | 1 | — | ❌ |
| Mookie Betts | RBI | Under | 0.5 | -294 | 73% | 0 | — | ✅ |
| Andrés Chaparro | RBI | Over | 0.5 | +236 | 29% | 0 | — | ❌ |
| Kyle Tucker | RBI | Under | 0.5 | -304 | 74% | 0 | — | ✅ |
| Tommy Edman | RBI | Under | 0.5 | -326 | 75% | 0 | — | ✅ |
| Casey Mize | Ks (P) | Over | 4.5 | +126 | 43% | 3 | — | ❌ |
| Chase DeLauter | Hits | Over | 0.5 | -241 | 69% | 0 | — | ❌ |
| Jake Cronenworth | RBI | Under | 0.5 | -365 | 76% | 1 | — | ❌ |
| Michael Harris II | RBI | Under | 0.5 | -206 | 66% | 0 | — | ✅ |
| Luis Torrens | Hits | Under | 0.5 | +114 | 46% | 1 | — | ❌ |
| Jackson Merrill | RBI | Over | 0.5 | +178 | 35% | 0 | — | ❌ |
| Julio Rodriguez | H+R+RBI | Over | 1.5 | -110 | 51% | 1 | — | ❌ |
| Dominic Smith | Hits | Over | 0.5 | -163 | 60% | 1 | — | ✅ |
| Jimmy Crooks | RBI | Over | 0.5 | +301 | 24% | 0 | — | ❌ |
| Jorbit Vivas | Hits | Over | 0.5 | -127 | 55% | 1 | — | ✅ |
| Carter Jensen | RBI | Under | 0.5 | -243 | 69% | 1 | — | ❌ |
| Julio Rodriguez | Hits | Over | 0.5 | -221 | 67% | 1 | — | ✅ |
| Miguel Vargas | RBI | Over | 0.5 | +174 | 36% | 1 | — | ✅ |
| Drew Romo | RBI | Under | 0.5 | -436 | 79% | 2 | — | ❌ |
| Ryan McMahon | RBI | Under | 0.5 | -443 | 79% | 0 | — | ✅ |
| Kyle Schwarber | H+R+RBI | Over | 1.5 | -137 | 56% | 2 | — | ✅ |
| Jackson Holliday | RBI | Over | 0.5 | +282 | 26% | 3 | — | ✅ |
| Xander Bogaerts | H+R+RBI | Under | 1.5 | -146 | 58% | 2 | — | ❌ |
| Jose Ramirez | H+R+RBI | Under | 1.5 | -117 | 52% | 2 | — | ❌ |
| Andrew Vaughn | RBI | Under | 0.5 | -380 | 77% | 1 | — | ❌ |
| Bo Bichette | Hits | Under | 1.5 | -266 | 70% | 3 | — | ❌ |
| Andrew Vaughn | H+R+RBI | Under | 1.5 | -179 | 62% | 3 | — | ❌ |
| Alejandro Kirk | Hits | Over | 0.5 | -217 | 66% | 1 | — | ✅ |
| Colton Cowser | RBI | Under | 0.5 | -396 | 78% | 2 | — | ❌ |
| Javier Sanoja | H+R+RBI | Over | 1.5 | -120 | 53% | 5 | — | ✅ |
| Evan Carter | H+R+RBI | Under | 1.5 | -157 | 59% | 1 | — | ✅ |
| Jose Altuve | RBI | Over | 0.5 | +239 | 29% | 0 | — | ❌ |
| Adley Rutschman | H+R+RBI | Under | 1.5 | -127 | 54% | 0 | — | ✅ |
| Alec Bohm | RBI | Over | 0.5 | +187 | 34% | 4 | — | ✅ |
| Ryan Vilade | RBI | Over | 0.5 | +227 | 30% | 1 | — | ✅ |
| Nick Fortes | RBI | Over | 0.5 | +247 | 28% | 0 | — | ❌ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +160 | 37% | 2 | — | ✅ |
| Jonny Deluca | Hits | Over | 0.5 | -187 | 63% | 0 | — | ❌ |
| Josh Naylor | RBI | Under | 0.5 | -320 | 74% | 0 | — | ✅ |
| Nathan Church | RBI | Over | 0.5 | +242 | 28% | 0 | — | ❌ |
| Isaac Collins | Hits | Over | 0.5 | -158 | 59% | 0 | — | ❌ |
| Tanner Bibee | Ks (P) | Over | 4.5 | +104 | 47% | 3 | — | ❌ |
| Willi Castro | RBI | Over | 0.5 | +217 | 30% | 0 | — | ❌ |
| Vaughn Grissom | RBI | Over | 0.5 | +185 | 34% | 0 | — | ❌ |
| Jake McCarthy | Hits | Under | 1.5 | -254 | 69% | 1 | — | ✅ |
| Byron Buxton | RBI | Over | 0.5 | +160 | 37% | 0 | — | ❌ |
| Andrew Benintendi | H+R+RBI | Over | 1.5 | +104 | 47% | 0 | — | ❌ |
| Salvador Perez | Hits | Under | 0.5 | +152 | 38% | 1 | — | ❌ |
| Oswald Peraza | Hits | Under | 0.5 | +123 | 43% | 0 | — | ✅ |
| Colson Montgomery | Hits | Over | 0.5 | -136 | 56% | 2 | — | ✅ |
| Zack Gelof | RBI | Under | 0.5 | -259 | 70% | 2 | — | ❌ |
| Eugenio Suarez | Hits | Over | 0.5 | -142 | 56% | 1 | — | ✅ |
| Kevin McGonigle | RBI | Over | 0.5 | +235 | 29% | 0 | — | ❌ |
| Ryan Vilade | Hits | Over | 0.5 | -158 | 59% | 3 | — | ✅ |
| George Springer | RBI | Under | 0.5 | -278 | 71% | 0 | — | ✅ |
| Sal Stewart | Hits | Over | 0.5 | -217 | 66% | 0 | — | ❌ |
| Jose Siri | H+R+RBI | Over | 0.5 | -141 | 56% | 0 | — | ❌ |
| Dillon Dingler | RBI | Over | 0.5 | +160 | 37% | 1 | — | ✅ |
| Javier Sanoja | RBI | Under | 0.5 | -264 | 70% | 3 | — | ❌ |
| Freddy Fermin | H+R+RBI | Under | 0.5 | +126 | 42% | 1 | — | ❌ |
| Manny Machado | RBI | Over | 0.5 | +183 | 34% | 0 | — | ❌ |
| Daylen Lile | RBI | Over | 0.5 | +179 | 34% | 0 | — | ❌ |
| Victor Caratini | Hits | Over | 0.5 | -179 | 62% | 0 | — | ❌ |
| Henry Davis | RBI | Over | 0.5 | +238 | 28% | 1 | — | ✅ |
| Miguel Vargas | Hits | Over | 0.5 | -200 | 64% | 1 | — | ✅ |
| Andres Gimenez | Hits | Over | 0.5 | -113 | 51% | 2 | — | ✅ |
| Jo Adell | Hits | Under | 0.5 | +137 | 40% | 0 | — | ✅ |
| TJ Friedl | H+R+RBI | Under | 0.5 | +114 | 45% | 0 | — | ✅ |
| Luis Arraez | RBI | Under | 0.5 | -247 | 68% | 1 | — | ❌ |
| Tim Tawa | H+R+RBI | Under | 1.5 | -153 | 58% | 1 | — | ✅ |
| Cal Raleigh | Hits | Under | 0.5 | -125 | 53% | 1 | — | ❌ |
| Heriberto Hernandez | H+R+RBI | Under | 1.5 | +103 | 47% | 4 | — | ❌ |
| Bryce Eldridge | H+R+RBI | Over | 1.5 | -110 | 50% | 3 | — | ✅ |
| Ryan Vilade | H+R+RBI | Over | 1.5 | +123 | 43% | 6 | — | ✅ |
| Matt Olson | RBI | Under | 0.5 | -197 | 64% | 3 | — | ❌ |
| Justin Crawford | Hits | Over | 0.5 | -183 | 62% | 1 | — | ✅ |
| Yordan Alvarez | RBI | Over | 0.5 | +138 | 40% | 0 | — | ❌ |
| Jacob Young | Hits | Under | 0.5 | +103 | 47% | 1 | — | ❌ |
| Spencer Torkelson | H+R+RBI | Under | 1.5 | -142 | 56% | 0 | — | ✅ |
| Evan Carter | Hits | Over | 0.5 | -140 | 56% | 1 | — | ✅ |
| Wilyer Abreu | H+R+RBI | Under | 1.5 | -113 | 51% | 0 | — | ✅ |
| Jake Burger | RBI | Under | 0.5 | -173 | 61% | 2 | — | ❌ |
| Kyle Tucker | H+R+RBI | Under | 1.5 | -154 | 58% | 0 | — | ✅ |
| Kyle Isbel | H+R+RBI | Under | 1.5 | -174 | 61% | 1 | — | ✅ |
| Bryce Harper | H+R+RBI | Over | 1.5 | -159 | 59% | 3 | — | ✅ |
| Ryan McMahon | Hits | Under | 0.5 | -124 | 53% | 0 | — | ✅ |
| Carson Benge | H+R+RBI | Over | 1.5 | -149 | 57% | 0 | — | ❌ |
| JJ Bleday | H+R+RBI | Under | 1.5 | -147 | 57% | 0 | — | ✅ |
| Keibert Ruiz | H+R+RBI | Under | 1.5 | -132 | 54% | 4 | — | ❌ |
| Ceddanne Rafaela | H+R+RBI | Under | 1.5 | +103 | 47% | 0 | — | ✅ |
| Sam Antonacci | RBI | Over | 0.5 | +271 | 26% | 1 | — | ✅ |
| Austin Riley | RBI | Over | 0.5 | +200 | 32% | 0 | — | ❌ |
| Ty France | Hits | Under | 0.5 | +177 | 34% | 0 | — | ✅ |
| Xander Bogaerts | RBI | Over | 0.5 | +249 | 27% | 1 | — | ✅ |
| Zach Neto | RBI | Over | 0.5 | +198 | 32% | 0 | — | ❌ |
| Sam Antonacci | Hits | Under | 0.5 | +156 | 37% | 0 | — | ✅ |
| Nathaniel Lowe | H+R+RBI | Over | 1.5 | +106 | 46% | 1 | — | ❌ |
| Elly De La Cruz | Hits | Under | 0.5 | +144 | 39% | 0 | — | ✅ |
| Brett Sullivan | Hits | Over | 0.5 | -138 | 55% | 1 | — | ✅ |
| Jared Young | Hits | Under | 0.5 | +163 | 36% | 2 | — | ❌ |
| Bryson Stott | H+R+RBI | Under | 1.5 | -104 | 48% | 2 | — | ❌ |
| Cam Smith | Hits | Under | 0.5 | +106 | 46% | 0 | — | ✅ |
| Kyle Tucker | Hits | Under | 0.5 | +118 | 44% | 0 | — | ✅ |
| Kody Clemens | RBI | Over | 0.5 | +161 | 36% | 1 | — | ✅ |
| Tristan Peters | RBI | Over | 0.5 | +270 | 26% | 0 | — | ❌ |
| Jake Bauers | Hits | Under | 0.5 | +102 | 47% | 4 | — | ❌ |
| Ezequiel Duran | RBI | Over | 0.5 | +158 | 37% | 0 | — | ❌ |
| Dillon Dingler | Hits | Under | 0.5 | +186 | 33% | 1 | — | ❌ |
| Manny Machado | H+R+RBI | Over | 1.5 | -110 | 49% | 0 | — | ❌ |
| Luis Rengifo | H+R+RBI | Over | 1.5 | -108 | 49% | 4 | — | ✅ |
| Ronald Acuna Jr. | RBI | Over | 0.5 | +185 | 33% | 1 | — | ✅ |
| Kyle Schwarber | RBI | Over | 0.5 | +148 | 38% | 0 | — | ❌ |
| Wade Meckler | H+R+RBI | Over | 1.5 | +124 | 42% | 0 | — | ❌ |
| Jo Adell | H+R+RBI | Over | 1.5 | -101 | 47% | 0 | — | ❌ |
| Otto Lopez | RBI | Over | 0.5 | +181 | 34% | 0 | — | ❌ |
| Michael Massey | H+R+RBI | Under | 1.5 | -131 | 53% | 5 | — | ❌ |
| Brett Sullivan | RBI | Over | 0.5 | +272 | 25% | 3 | — | ✅ |
| Xavier Edwards | RBI | Over | 0.5 | +194 | 32% | 0 | — | ❌ |
| Ketel Marte | H+R+RBI | Under | 1.5 | +106 | 46% | 1 | — | ✅ |
| Jo Adell | RBI | Over | 0.5 | +178 | 34% | 0 | — | ❌ |
| Salvador Perez | H+R+RBI | Over | 1.5 | -109 | 49% | 1 | — | ❌ |
| Randy Arozarena | RBI | Over | 0.5 | +234 | 28% | 1 | — | ✅ |
| Brandon Marsh | RBI | Over | 0.5 | +209 | 30% | 0 | — | ❌ |
| Michael Massey | Hits | Under | 0.5 | +144 | 38% | 3 | — | ❌ |
| Ty France | H+R+RBI | Under | 1.5 | -111 | 49% | 0 | — | ✅ |
| Jac Caglianone | RBI | Over | 0.5 | +143 | 38% | 0 | — | ❌ |
| Jacob Young | H+R+RBI | Over | 1.5 | +131 | 40% | 1 | — | ❌ |
| Jonah Heim | RBI | Over | 0.5 | +183 | 33% | 0 | — | ❌ |
| Gabriel Hughes | Ks (P) | Under | 3.5 | +129 | 41% | 2 | — | ✅ |
| Ceddanne Rafaela | RBI | Over | 0.5 | +199 | 31% | 0 | — | ❌ |
| Anthony Seigler | Hits | Under | 0.5 | +105 | 45% | 1 | — | ❌ |
| Nathan Church | H+R+RBI | Over | 1.5 | +112 | 44% | 0 | — | ❌ |
| Anthony Seigler | H+R+RBI | Over | 1.5 | +131 | 40% | 2 | — | ✅ |
| Heriberto Hernandez | RBI | Over | 0.5 | +157 | 36% | 1 | — | ✅ |
| Nathaniel Lowe | RBI | Over | 0.5 | +200 | 31% | 0 | — | ❌ |
| Connor Wong | H+R+RBI | Under | 0.5 | +126 | 41% | 6 | — | ❌ |
| JJ Bleday | Hits | Under | 0.5 | +122 | 42% | 0 | — | ✅ |
| Luis Torrens | H+R+RBI | Over | 1.5 | +122 | 42% | 4 | — | ✅ |
| Isaac Collins | H+R+RBI | Over | 1.5 | +112 | 44% | 0 | — | ❌ |
| Bo Bichette | H+R+RBI | Under | 1.5 | +118 | 42% | 3 | — | ❌ |
| Eugenio Suarez | RBI | Over | 0.5 | +181 | 33% | 0 | — | ❌ |
| Tim Tawa | RBI | Over | 0.5 | +238 | 27% | 1 | — | ✅ |
| Mickey Moniak | RBI | Over | 0.5 | +172 | 34% | 3 | — | ✅ |
| Eugenio Suarez | H+R+RBI | Over | 1.5 | +116 | 43% | 1 | — | ❌ |
| Royce Lewis | RBI | Over | 0.5 | +147 | 37% | 0 | — | ❌ |
| Javier Baez | RBI | Over | 0.5 | +254 | 26% | 0 | — | ❌ |
| Andy Pages | RBI | Over | 0.5 | +186 | 32% | 1 | — | ✅ |
| Adley Rutschman | Hits | Under | 0.5 | +140 | 38% | 0 | — | ✅ |
| Tim Tawa | Hits | Under | 0.5 | +126 | 41% | 0 | — | ✅ |
| Nico Hoerner | Hits | Under | 0.5 | +197 | 31% | 1 | — | ❌ |
| Ozzie Albies | Hits | Under | 0.5 | +147 | 37% | 0 | — | ✅ |
| Brendan Donovan | RBI | Over | 0.5 | +263 | 25% | 0 | — | ❌ |
| Cal Raleigh | RBI | Over | 0.5 | +213 | 29% | 1 | — | ✅ |
| Zack Gelof | Hits | Under | 0.5 | +172 | 34% | 2 | — | ❌ |
| Jonny Deluca | RBI | Over | 0.5 | +233 | 27% | 0 | — | ❌ |
| Daylen Lile | Hits | Under | 0.5 | +178 | 33% | 0 | — | ✅ |
| Fernando Tatis Jr. | RBI | Over | 0.5 | +184 | 32% | 0 | — | ❌ |
| Drew Gilbert | Hits | Under | 0.5 | +151 | 36% | 1 | — | ❌ |
| Heliot Ramos | RBI | Over | 0.5 | +276 | 24% | 0 | — | ❌ |
| Ernie Clement | RBI | Over | 0.5 | +237 | 27% | 1 | — | ✅ |
| Freddie Freeman | RBI | Over | 0.5 | +232 | 27% | 0 | — | ❌ |
| Ezequiel Tovar | RBI | Over | 0.5 | +279 | 24% | 0 | — | ❌ |
| Nick Loftin | RBI | Over | 0.5 | +239 | 27% | 0 | — | ❌ |
| Taylor Trammell | RBI | Over | 0.5 | +277 | 24% | 0 | — | ❌ |
| Luke Keaschall | RBI | Over | 0.5 | +215 | 28% | 0 | — | ❌ |
| Francisco Lindor | Hits | Over | 1.5 | +203 | 30% | 1 | — | ❌ |
| Salvador Perez | RBI | Over | 0.5 | +165 | 34% | 0 | — | ❌ |
| Shohei Ohtani | RBI | Over | 0.5 | +163 | 34% | 0 | — | ❌ |
| Mike Trout | RBI | Over | 0.5 | +184 | 31% | 0 | — | ❌ |
| Elly De La Cruz | RBI | Over | 0.5 | +172 | 33% | 0 | — | ❌ |
| Wade Meckler | RBI | Over | 0.5 | +296 | 22% | 0 | — | ❌ |
| Adley Rutschman | RBI | Over | 0.5 | +176 | 32% | 0 | — | ❌ |
| Spencer Torkelson | RBI | Over | 0.5 | +180 | 32% | 0 | — | ❌ |
| Luis Rengifo | RBI | Over | 0.5 | +232 | 26% | 1 | — | ✅ |
| Jacob Young | RBI | Over | 0.5 | +229 | 27% | 0 | — | ❌ |
| Jarren Duran | RBI | Over | 0.5 | +193 | 30% | 0 | — | ❌ |
| Drew Gilbert | RBI | Over | 0.5 | +242 | 26% | 1 | — | ✅ |
| Caleb Durbin | RBI | Over | 0.5 | +191 | 30% | 0 | — | ❌ |
| Geraldo Perdomo | RBI | Over | 0.5 | +227 | 26% | 0 | — | ❌ |
| Isaac Collins | RBI | Over | 0.5 | +240 | 25% | 0 | — | ❌ |
| Gary Sanchez | RBI | Over | 0.5 | +247 | 25% | 0 | — | ❌ |
| Evan Carter | RBI | Over | 0.5 | +240 | 25% | 0 | — | ❌ |
| Kyle Isbel | RBI | Over | 0.5 | +280 | 22% | 0 | — | ❌ |
| Jorbit Vivas | RBI | Over | 0.5 | +325 | 20% | 0 | — | ❌ |
| Matt McLain | RBI | Over | 0.5 | +288 | 22% | 0 | — | ❌ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Baltimore Orioles @ Tampa Bay Rays | **YRFI** | High | 66% | 50% | ❌ |
| Arizona Diamondbacks @ Atlanta Braves | **YRFI** | High | 72% | 49% | ❌ |
| Washington Nationals @ New York Mets | **YRFI** | High | 61% | 50% | ❌ |
| San Diego Padres @ Cleveland Guardians | **YRFI** | High | 56% | 43% | ❌ |
| Chicago White Sox @ Detroit Tigers | **YRFI** | High | 56% | 43% | ❌ |
| Colorado Rockies @ San Francisco Giants | **YRFI** | High | 66% | 50% | ✅ |
| Kansas City Royals @ Los Angeles Angels | **NRFI** | High | 57% | 47% | ✅ |
| Seattle Mariners @ Houston Astros | **YRFI** | High | 57% | 47% | ✅ |
| New York Yankees @ Toronto Blue Jays | **NRFI** | Medium | 66% | 61% | ✅ |
| Miami Marlins @ Cincinnati Reds | **NRFI** | Medium | 55% | 48% | ✅ |
| Philadelphia Phillies @ Minnesota Twins | **NRFI** | Medium | 51% | 46% | ❌ |
| Texas Rangers @ Athletics | **NRFI** | Low | 51% | 48% | ✅ |
| Boston Red Sox @ Pittsburgh Pirates | **NRFI** | Coin flip | 51% | 51% | ❌ |
| St. Louis Cardinals @ Chicago Cubs | **YRFI** | Coin flip | 51% | 52% | ✅ |
| Milwaukee Brewers @ Los Angeles Dodgers | **NRFI** | Coin flip | 51% | 52% | ✅ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Griffin Conine | Miami Marlins @ Cincinnati Reds | 32% | ❌ |
| 2 | Kyle Schwarber | Philadelphia Phillies @ Minnesota Twins | 28% | ❌ |
| 3 | Heriberto Hernández | Miami Marlins @ Cincinnati Reds | 28% | ✅ |
| 5 | Byron Buxton | Philadelphia Phillies @ Minnesota Twins | 26% | ❌ |
| 6 | Joc Pederson | Texas Rangers @ Athletics | 26% | ❌ |
| 8 | Max Muncy | Milwaukee Brewers @ Los Angeles Dodgers | 25% | ✅ |
| 9 | Shohei Ohtani | Milwaukee Brewers @ Los Angeles Dodgers | 25% | ❌ |
| 10 | Jac Caglianone | Kansas City Royals @ Los Angeles Angels | 22% | ❌ |

*2 homered · model expected 2.1*

> **CLV caveat.** Beating the close is evidence of skill only when the move came from the market re-evaluating information we also had. If a scratch or injury broke after we locked, we collect the CLV without having known anything — that is luck wearing the costume of skill. Read CLV in aggregate, never on a single bet.

> CLV is the signal that matters here, not W-L — per the sharp-bettor method, beating the closing line is what indicates a real edge. A small sample of wins with negative CLV is luck, not edge.

### Moneyline probability calibration (Model A, n=332)

Brier score: **0.2438** (0.25 = coin flip knowledge; lower is better)

| Model home-win band | n | Predicted avg | Actual home-win % |
|---|---|---|---|
| 0%–40% | 47 | 35% | 38% |
| 40%–45% | 52 | 43% | 46% |
| 45%–50% | 57 | 47% | 39% |
| 50%–55% | 46 | 52% | 41% |
| 55%–60% | 53 | 57% | 64% |
| 60%–65% | 38 | 62% | 58% |
| 65%+ | 39 | 69% | 67% |

> Calibrated = predicted ≈ actual per band. Systematic gaps mean the win probabilities themselves need retuning before any ML edge claim.

### Model A — segments (finding the winning slice)

- **by market:** NRFI 3-1 (+40%, CLV +2.0%)  ·  Moneyline 193-139 (+2%, CLV -10.3%)  ·  Total 83-80 (-1%, CLV -4.1%)  ·  Run Line 42-48 (-2%)  ·  F5 Total 6-14 (-47%, CLV -2.0%)
- **by side:** Under 58-54 (-0%)  ·  team 244-202 (-0%, CLV -7.4%)  ·  Over 25-26 (-2%, CLV -4.1%)
- **by fav_band:** unknown 20-14 (+12%)  ·  pickem 168-145 (+3%, CLV -3.8%)  ·  fav 93-67 (-5%, CLV -12.3%)  ·  dog 29-45 (-6%, CLV -1.9%)  ·  heavy fav 17-11 (-14%, CLV -11.6%)

### Model B — segments (finding the winning slice)

- **by market:** Total 64-49 (+9%)  ·  Moneyline 142-101 (+4%)  ·  Run Line 31-41 (-7%)
- **by side:** Over 13-7 (+24%)  ·  Under 51-42 (+6%)  ·  team 173-142 (+1%)
- **by fav_band:** pickem 129-98 (+9%)  ·  fav 68-40 (+4%)  ·  dog 27-40 (-5%)  ·  unknown 2-3 (-24%)  ·  heavy fav 11-10 (-26%)

## Model A — picks by date

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
