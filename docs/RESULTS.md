# Results

## Scoreboard

| Board | Record | Hit rate | Model predicted | Standing |
|---|---|---|---|---|
| **Locked bets** (ML/Total) | 360-312 | **53.6%** | — | -9.67u · CLV -3.17% |
| NRFI/YRFI forced calls | 103-102 | **50.2%** | 59.8% | 🔴 behind its own number · ⚠️ below 54% naive baseline |
| HR board (top 10 daily) | 22-128 | **14.7%** | 24.5% | 🔴 behind its own number |
| Player props (all tiers) | 3316-3667 | **47.5%** | 53.1% | 🔴 behind its own number · CLV +0.25% |
| &nbsp;&nbsp;↳ props · tier A (HR, pitcher K) | 153-126 | **54.8%** | 57.8% | 🟡 tracking its number |
| &nbsp;&nbsp;↳ props · tier B (hits, batter K) | 1130-1094 | **50.8%** | 57.1% | 🔴 behind its own number |
| &nbsp;&nbsp;↳ props · tier C (RBI, H+R+RBI) | 2020-2430 | **45.4%** | 50.7% | 🔴 behind its own number |

**Hit rate vs predicted is the whole test.** A board that hits at the rate it claims is trustworthy even when it loses; a board that hits below its own number is telling you it does not know what it claims to know.

---

**Model A** = current model (control). **Model B** = retired variant, history preserved. CLV measured from the real price vs close. Each unique bet counted once. Paper only — no real money.

**Model A: 360-312  ·  54% win  ·  -9.67u  ·  -1.4% ROI  ·  avg CLV -3.17%**
**Model B: 237-191  ·  55% win  ·  +14.16u  ·  +3.3% ROI  ·  avg CLV n/a (no closing lines yet)**

## Board calibration standings

These boards are calibration records, not bets. The question is not whether they won — it is whether a call at a stated confidence lands at that rate. A tier that hits BELOW its stated probability is a model telling you it does not know what it claims to know.

### NRFI/YRFI forced calls

| Confidence | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|
| High | 120 | 54 | 66 | 45% | 64% | -19% |
| Medium | 30 | 17 | 13 | 57% | 56% | +0% |
| Low | 21 | 12 | 9 | 57% | 54% | +4% |
| Coin flip | 34 | 20 | 14 | 59% | 53% | +6% |
| **All** | **205** | **103** | **102** | **50%** | **60%** | **-10%** |

YRFI share of calls: **147/205 (72%)** — hitting 48%.

**Naive baseline check.** First innings were scoreless in **53.7%** of these games, so always calling NRFI scores **53.7%**. The model scores **50.2%**.

> ⚠️ **The model is losing to a coin that always says the same thing.** Until it beats this line, its calls carry no information and should not be treated as analysis — a forced call is only worth making if it beats the majority class.

> ⚠️ **Confidence is inverted**: the High tier is hitting BELOW the Coin flip tier. Whatever the confidence metric is measuring, it is not the probability of being right. Calls at this tier should carry no weight until this reverses.

### HR board (top-10 daily)

- listed and graded: **150**
- homered: **22** · model expected **36.8**
- actual rate **14.7%** vs predicted **24.5%** (**-9.9%**)

### Prop divergence board

| Tier | Market | n | Hit | Miss | Hit% | Model said | Gap |
|---|---|---|---|---|---|---|---|
| A | Ks (P) | 279 | 153 | 126 | 55% | 58% | -3% |
| B | Hits | 2224 | 1130 | 1094 | 51% | 57% | -6% |
| C | H+R+RBI | 2225 | 1128 | 1097 | 51% | 57% | -6% |
| C | RBI | 2225 | 892 | 1333 | 40% | 45% | -5% |
| **All** | | **6983** | **3316** | **3667** | **47%** | **53%** | **-6%** |

Gate-clearing calls only: **40-32** (56% vs 60% predicted).

> **Sample-size reality check.** Distinguishing a real edge from noise needs hundreds of graded calls per tier. Gaps below are indicative, not verdicts — except where a tier is inverted against a lower tier, which is a structural signal rather than variance.

## Weak-link analysis

Every slice of the graded record with a bootstrap confidence interval. A segment only counts as a demonstrated loser when its whole interval sits below zero — otherwise it is a segment having a bad run, and cutting it would be fitting to noise.

### By grade

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| LEAN | 124-137 | -27.69u | -10.6% | -22.0% to +1.6% | ⚪ inconclusive |
| PLAY | 236-175 | +18.02u | +4.4% | -4.3% to +12.8% | ⚪ inconclusive |

### By market

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| F5 Total | 14-20 | -9.36u | -27.5% | -58.1% to +3.8% | ⚪ inconclusive |
| Total | 86-89 | -7.47u | -4.3% | -18.6% to +10.3% | ⚪ inconclusive |
| Run Line | 42-48 | -2.11u | -2.3% | -24.3% to +20.2% | ⚪ inconclusive |
| Moneyline | 212-150 | +9.13u | +2.5% | -6.5% to +11.8% | ⚪ inconclusive |

### By price band

| Segment | Record | Units | ROI | 95% CI | Verdict |
|---|---|---|---|---|---|
| fav -121 to -160 | 77-73 | -17.69u | -11.8% | -25.5% to +1.1% | ⚪ inconclusive |
| dog +120 or longer | 19-34 | -5.19u | -9.8% | -40.8% to +21.8% | ⚪ inconclusive |
| heavy fav past -160 | 71-41 | -3.93u | -3.5% | -17.2% to +9.9% | ⚪ inconclusive |
| pickem -120 to -100 | 132-116 | +3.48u | +1.4% | -10.5% to +12.4% | ⚪ inconclusive |
| dog +100 to +119 | 41-34 | +9.46u | +12.6% | -12.3% to +36.6% | ⚪ inconclusive |

### By model score — does the score rank bets correctly?

| Score band | n | Record | Units | ROI |
|---|---|---|---|---|
| 5.0–5.9 | 149 | 71-78 | -16.26u | -10.9% |
| 6.0–6.9 | 112 | 53-59 | -11.43u | -10.2% |
| 7.0–7.9 | 109 | 59-50 | +3.91u | +3.6% |
| 8.0–8.9 | 79 | 45-34 | +2.44u | +3.1% |
| 9.0–10.9 | 223 | 132-91 | +11.67u | +5.2% |

> Rank correlation between score band and ROI: **+0.90** (+1.00 = ROI rises perfectly with score).

> Below score 7.0: **-27.69u over 261 bets (-10.6%)**. At 7.0 and above: **+18.02u over 411 bets (+4.4%)**. The sign flips at exactly the PLAY threshold.

> ✅ The score ranks bets in the right order. That is stronger evidence than any single segment clearing a confidence interval — one slice can look good by luck, a clean gradient across bands is much harder to get by accident.

### Closing line value — the deeper test

Across **62** picks with a captured close, average CLV is **-3.17%** and **18/62 (29%)** beat the closing price.

> ⚠️ **Negative CLV outweighs a winning record.** The market is moving against these picks after they lock, which is what luck looks like from the inside — a model with real edge gets better prices than the close, not worse. Until this turns positive, treat any winning stretch as variance.

> One measurement caveat before over-reading it: picks lock at the BEST price across two books, and the close is captured from that same book. Some of the gap is simply the best-of-two price regressing, not the market disagreeing. The honest read is directional, not exact.

## Early vs late pull

| Pull | Rows | Avg CLV | Beat close |
|---|---|---|---|
| 8am (pre-move) | 1621 | **+0.37%** | 805/1621 |

## Daily ledger — every call, every result

Last 4 graded slates in full. Most recent first.

### 2026-08-24 — bets 3-2 (+0.41u) · props 207-216 · NRFI 4-4 · HR 0-10

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Philadelphia Phillies ML | — | -116 | 9.5 | -6.9% | ❌ -1.00u |
| F5 Total | F5 Over 4.5 | 4.5 | -146 | 9.5 | -3.2% | ❌ -1.00u |
| Moneyline | Chicago Cubs ML | — | -142 | 5.9 | -11.5% | ✅ +0.70u |
| F5 Total | F5 Over 4.5 | 4.5 | -108 | 5.3 | +8.9% | ✅ +0.93u |
| NRFI | NRFI | 0.5 | -128 | 5.2 | -3.6% | ✅ +0.78u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Ryan Feltner | Ks (P) | Under | 3.5 | +124 | 64% | 6 | +17.3% | ❌ |
| Dane Myers | Hits | Under | 0.5 | +181 | 56% | 0 | +5.2% | ✅ |
| Zack Wheeler | Ks (P) | Under | 7.5 | -142 | 76% | 4 | +2.2% | ✅ |
| Merrill Kelly | Ks (P) | Under | 3.5 | +124 | 57% | 4 | +3.7% | ❌ |
| Jonah Heim | Hits | Under | 0.5 | +153 | 55% | 1 | +3.3% | ❌ |
| Jorge Mateo | Hits | Under | 0.5 | +122 | 61% | 1 | +18.7% | ❌ |
| Jose Siri | Hits | Under | 0.5 | -104 | 69% | 0 | +1.9% | ✅ |
| Michael Conforto | Hits | Under | 0.5 | +125 | 59% | 3 | +4.2% | ❌ |
| Drew Rasmussen | Ks (P) | Over | 4.5 | -146 | 71% | 5 | +0.6% | ✅ |
| Braxton Ashcraft | Ks (P) | Over | 4.5 | -164 | 74% | 2 | — | ❌ |
| Oneil Cruz | Hits | Over | 0.5 | -140 | 73% | 0 | +2.0% | ❌ |
| Jorbit Vivas | Hits | Under | 0.5 | +124 | 56% | 3 | +4.2% | ❌ |
| Dane Myers | H+R+RBI | Under | 1.5 | -109 | 72% | 0 | +3.0% | ✅ |
| Jeffrey Springs | Ks (P) | Under | 3.5 | -116 | 62% | 3 | -8.3% | ✅ |
| Chase Burns | Ks (P) | Under | 6.5 | -110 | 60% | 5 | +2.5% | ✅ |
| Freddy Fermin | Hits | Under | 0.5 | -118 | 66% | 2 | -1.2% | ❌ |
| Brandon Marsh | Hits | Over | 0.5 | -136 | 70% | 0 | -0.3% | ❌ |
| Jose Ramirez | Hits | Under | 0.5 | +173 | 44% | 1 | +2.6% | ❌ |
| Taylor Ward | Hits | Over | 0.5 | -108 | 61% | 0 | +7.0% | ❌ |
| Jose Siri | H+R+RBI | Under | 0.5 | +117 | 59% | 0 | +1.9% | ✅ |
| Ranger Suarez | Ks (P) | Under | 5.5 | -158 | 68% | 4 | — | ✅ |
| Tyler Stephenson | Hits | Under | 0.5 | +166 | 44% | 2 | +4.3% | ❌ |
| Byron Buxton | H+R+RBI | Under | 2.5 | -102 | 63% | 7 | -2.4% | ❌ |
| Brayan Rocchio | Hits | Under | 0.5 | +149 | 46% | 0 | +2.0% | ✅ |
| Jorge Mateo | H+R+RBI | Under | 1.5 | -156 | 76% | 2 | — | ❌ |
| Jeff McNeil | Hits | Under | 1.5 | -212 | 78% | 3 | -1.2% | ❌ |
| Carlos Cortes | H+R+RBI | Under | 1.5 | -106 | 64% | 0 | +9.1% | ✅ |
| Moises Ballesteros | Hits | Under | 0.5 | +121 | 52% | 1 | +1.8% | ❌ |
| Framber Valdez | Ks (P) | Under | 4.5 | -151 | 66% | 0 | — | ✅ |
| Ildemaro Vargas | Hits | Under | 0.5 | +155 | 44% | 1 | +6.2% | ❌ |
| Robbie Ray | Ks (P) | Under | 5.5 | -104 | 55% | 5 | +4.1% | ✅ |
| Esteury Ruiz | H+R+RBI | Under | 1.5 | -177 | 77% | 0 | — | ✅ |
| Willi Castro | Hits | Over | 0.5 | -172 | 71% | 1 | +1.7% | ✅ |
| Tristan Peters | Hits | Over | 0.5 | -140 | 66% | 1 | +1.5% | ✅ |
| Bryan Reynolds | Hits | Over | 0.5 | -173 | 71% | 1 | -1.5% | ✅ |
| Oneil Cruz | H+R+RBI | Over | 1.5 | +115 | 56% | 0 | +0.0% | ❌ |
| Jonathan Aranda | RBI | Over | 0.5 | +244 | 35% | 2 | — | ✅ |
| Kevin Gausman | Ks (P) | Under | 5.5 | -162 | 67% | 6 | — | ❌ |
| Gabriel Moreno | RBI | Over | 0.5 | +195 | 41% | 0 | +0.0% | ❌ |
| Henry Bolte | Hits | Under | 1.5 | -227 | 78% | 3 | -1.1% | ❌ |
| Rafael Devers | Hits | Over | 0.5 | -154 | 68% | 2 | -3.8% | ✅ |
| Esteury Ruiz | Hits | Under | 0.5 | +105 | 55% | 0 | +7.4% | ✅ |
| Michael Conforto | H+R+RBI | Under | 1.5 | -134 | 68% | 7 | +2.8% | ❌ |
| Jose Ramirez | H+R+RBI | Under | 1.5 | -102 | 60% | 1 | +0.5% | ✅ |
| Alec Bohm | RBI | Over | 0.5 | +239 | 35% | 1 | -0.3% | ✅ |
| Byron Buxton | Hits | Under | 1.5 | -175 | 71% | 3 | -1.5% | ❌ |
| Randy Arozarena | Hits | Over | 0.5 | -149 | 67% | 0 | +2.1% | ❌ |
| Jeff McNeil | H+R+RBI | Under | 1.5 | +117 | 54% | 6 | -2.2% | ❌ |
| Luke Keaschall | Hits | Under | 1.5 | -216 | 76% | 2 | +0.0% | ❌ |
| Mickey Moniak | RBI | Over | 0.5 | +218 | 37% | 0 | — | ❌ |
| Henry Bolte | H+R+RBI | Under | 1.5 | +121 | 53% | 6 | — | ❌ |
| Byron Buxton | RBI | Under | 0.5 | -127 | 65% | 0 | -1.1% | ✅ |
| Eugenio Suarez | Hits | Under | 0.5 | +127 | 48% | 1 | +0.0% | ❌ |
| Tyler Stephenson | H+R+RBI | Under | 1.5 | -108 | 60% | 2 | +3.8% | ❌ |
| Royce Lewis | H+R+RBI | Under | 2.5 | -137 | 67% | 1 | +3.0% | ✅ |
| Ian Happ | Hits | Over | 0.5 | -195 | 72% | 2 | -1.2% | ✅ |
| Braden Montgomery | Hits | Over | 0.5 | -193 | 72% | 1 | +0.0% | ✅ |
| TJ Rumfield | Hits | Over | 0.5 | -228 | 76% | 1 | +1.6% | ✅ |
| Ildemaro Vargas | RBI | Over | 0.5 | +235 | 34% | 0 | -5.4% | ❌ |
| Chase Meidroth | Hits | Over | 0.5 | -181 | 70% | 0 | +0.0% | ❌ |
| Oneil Cruz | RBI | Over | 0.5 | +190 | 39% | 0 | +0.7% | ❌ |
| Moises Ballesteros | H+R+RBI | Under | 1.5 | -169 | 72% | 2 | +2.7% | ❌ |
| Jorbit Vivas | H+R+RBI | Under | 1.5 | -148 | 68% | 6 | +1.9% | ❌ |
| Jonah Heim | H+R+RBI | Under | 1.5 | -124 | 63% | 2 | +2.1% | ❌ |
| Weston Wilson | Hits | Under | 0.5 | -166 | 68% | 0 | -3.6% | ✅ |
| Josh Bell | Hits | Over | 1.5 | +195 | 37% | 1 | +1.4% | ❌ |
| Matt McLain | Hits | Under | 0.5 | +128 | 47% | 0 | +2.2% | ✅ |
| Nathaniel Lowe | H+R+RBI | Under | 1.5 | -121 | 62% | 1 | +3.9% | ✅ |
| Jake Burger | Hits | Over | 0.5 | -156 | 66% | 2 | -1.3% | ✅ |
| Seiya Suzuki | RBI | Over | 0.5 | +171 | 42% | 1 | -0.4% | ✅ |
| Luke Keaschall | H+R+RBI | Under | 2.5 | -152 | 68% | 4 | +0.0% | ❌ |
| Brandon Marsh | H+R+RBI | Over | 0.5 | -166 | 70% | 0 | -0.2% | ❌ |
| Kody Clemens | Hits | Over | 0.5 | -234 | 75% | 2 | +4.0% | ✅ |
| Lawrence Butler | H+R+RBI | Under | 1.5 | -116 | 60% | 2 | -4.6% | ❌ |
| Luis Arraez | Hits | Over | 0.5 | -238 | 76% | 1 | -1.0% | ✅ |
| Taylor Ward | H+R+RBI | Over | 0.5 | -143 | 66% | 1 | +8.1% | ✅ |
| Spencer Torkelson | Hits | Under | 0.5 | -103 | 54% | 1 | +0.9% | ❌ |
| Royce Lewis | RBI | Under | 0.5 | -146 | 66% | 0 | +4.9% | ✅ |
| Geraldo Perdomo | Hits | Over | 0.5 | -183 | 69% | 1 | +1.3% | ✅ |
| Joc Pederson | H+R+RBI | Under | 1.5 | -139 | 64% | 1 | +3.2% | ✅ |
| Jo Adell | Hits | Under | 0.5 | +156 | 42% | 1 | +2.0% | ❌ |
| Brandon Lowe | RBI | Over | 0.5 | +210 | 36% | 0 | -9.4% | ❌ |
| Ceddanne Rafaela | RBI | Over | 0.5 | +233 | 33% | 0 | -0.6% | ❌ |
| Jose Ramirez | RBI | Under | 0.5 | -211 | 75% | 0 | +1.3% | ✅ |
| Randy Arozarena | H+R+RBI | Over | 1.5 | +130 | 48% | 1 | +4.1% | ❌ |
| Jake Cronenworth | Hits | Under | 0.5 | +121 | 48% | 2 | -2.2% | ❌ |
| Lars Nootbaar | H+R+RBI | Under | 1.5 | -107 | 56% | 0 | +3.5% | ✅ |
| Brayan Rocchio | H+R+RBI | Under | 1.5 | -130 | 62% | 1 | +1.6% | ✅ |
| Jake McCarthy | Hits | Over | 0.5 | -238 | 74% | 1 | — | ✅ |
| JJ Bleday | Hits | Over | 0.5 | -153 | 64% | 0 | -2.1% | ❌ |
| Nolan Arenado | RBI | Over | 0.5 | +199 | 36% | 0 | -7.1% | ❌ |
| Sal Stewart | RBI | Over | 0.5 | +165 | 41% | 0 | -0.4% | ❌ |
| Dylan Crews | H+R+RBI | Under | 1.5 | -102 | 55% | 2 | +1.4% | ❌ |
| Josh Naylor | Hits | Over | 0.5 | -165 | 66% | 3 | +1.1% | ✅ |
| Ryan Jeffers | Hits | Under | 1.5 | -230 | 73% | 1 | -0.9% | ✅ |
| Carlos Cortes | RBI | Under | 0.5 | -208 | 73% | 0 | +6.9% | ✅ |
| Willi Castro | H+R+RBI | Over | 1.5 | +119 | 49% | 3 | — | ✅ |
| Colt Keith | H+R+RBI | Under | 1.5 | -171 | 68% | 0 | -2.5% | ✅ |
| Bryce Harper | H+R+RBI | Over | 1.5 | +118 | 50% | 2 | +0.0% | ✅ |
| Munetaka Murakami | Hits | Over | 0.5 | -177 | 67% | 1 | -1.0% | ✅ |
| Alex Bregman | Hits | Over | 0.5 | -245 | 74% | 1 | +0.0% | ✅ |
| Luis Rengifo | Hits | Over | 0.5 | -160 | 64% | 0 | — | ❌ |
| Heriberto Hernandez | Hits | Under | 0.5 | +136 | 44% | 2 | — | ❌ |
| Drew Gilbert | H+R+RBI | Under | 1.5 | -184 | 70% | 4 | — | ❌ |
| Brandon Lowe | H+R+RBI | Over | 1.5 | +122 | 48% | 0 | — | ❌ |
| Drew Romo | Hits | Under | 0.5 | -129 | 59% | 1 | +0.0% | ❌ |
| Gabriel Moreno | H+R+RBI | Over | 1.5 | -118 | 58% | 0 | +1.5% | ❌ |
| Ryan Vilade | H+R+RBI | Under | 1.5 | -133 | 61% | 2 | — | ❌ |
| Xander Bogaerts | Hits | Under | 0.5 | +107 | 50% | 0 | +0.0% | ✅ |
| Mickey Gasper | Hits | Over | 0.5 | -142 | 61% | 2 | +0.9% | ✅ |
| Cole Young | Hits | Over | 0.5 | -158 | 64% | 1 | +0.2% | ✅ |
| Freddy Fermin | H+R+RBI | Under | 0.5 | +104 | 52% | 3 | -1.9% | ❌ |
| Pedro Ramirez | H+R+RBI | Under | 1.5 | -115 | 57% | 4 | -0.4% | ❌ |
| J.T. Realmuto | Hits | Under | 0.5 | +104 | 51% | 1 | +2.0% | ❌ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +113 | 50% | 0 | +1.4% | ❌ |
| Alex Bregman | RBI | Over | 0.5 | +162 | 40% | 0 | +2.3% | ❌ |
| Jo Adell | H+R+RBI | Under | 1.5 | -116 | 57% | 2 | +0.0% | ❌ |
| George Klassen | Ks (P) | Under | 4.5 | -167 | 64% | 3 | -0.5% | ✅ |
| Fernando Tatis Jr. | RBI | Over | 0.5 | +206 | 35% | 0 | +5.2% | ❌ |
| Otto Lopez | H+R+RBI | Over | 1.5 | -118 | 57% | 4 | — | ✅ |
| Yandy Diaz | RBI | Over | 0.5 | +199 | 35% | 0 | +1.4% | ❌ |
| Connor Norby | Hits | Over | 0.5 | -123 | 57% | 1 | +4.2% | ✅ |
| Nathaniel Lowe | Hits | Under | 0.5 | +145 | 42% | 0 | +3.8% | ✅ |
| Heriberto Hernandez | RBI | Over | 0.5 | +234 | 32% | 0 | -15.4% | ❌ |
| Seiya Suzuki | Hits | Over | 0.5 | -248 | 74% | 1 | -0.9% | ✅ |
| Lars Nootbaar | Hits | Under | 0.5 | +165 | 39% | 0 | +6.8% | ✅ |
| Willi Castro | RBI | Over | 0.5 | +236 | 31% | 1 | — | ✅ |
| Kevin McGonigle | Hits | Over | 0.5 | -222 | 71% | 1 | -3.3% | ✅ |
| Logan Gilbert | Ks (P) | Under | 5.5 | +120 | 46% | 5 | — | ✅ |
| Jonny Deluca | H+R+RBI | Under | 1.5 | -130 | 59% | 2 | — | ❌ |
| Jake Burger | RBI | Over | 0.5 | +203 | 34% | 2 | -2.6% | ✅ |
| Alex Bregman | H+R+RBI | Over | 1.5 | -132 | 60% | 2 | +1.3% | ✅ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | +110 | 50% | 2 | -1.9% | ✅ |
| Rafael Devers | RBI | Over | 0.5 | +234 | 31% | 3 | -3.8% | ✅ |
| Denzer Guzman | Hits | Under | 0.5 | +102 | 51% | 0 | +4.4% | ✅ |
| Ezequiel Tovar | H+R+RBI | Over | 0.5 | -148 | 62% | 4 | +0.5% | ✅ |
| Julio Rodriguez | Hits | Over | 0.5 | -166 | 64% | 2 | +0.7% | ✅ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +143 | 43% | 0 | +2.1% | ❌ |
| Luis Rengifo | H+R+RBI | Over | 1.5 | +133 | 45% | 0 | — | ❌ |
| Tristan Peters | H+R+RBI | Over | 0.5 | -180 | 67% | 4 | — | ✅ |
| Weston Wilson | H+R+RBI | Under | 0.5 | -130 | 59% | 0 | -3.5% | ✅ |
| Adley Rutschman | RBI | Over | 0.5 | +198 | 35% | 0 | -16.1% | ❌ |
| Brandon Lowe | Hits | Over | 0.5 | -143 | 60% | 0 | -7.0% | ❌ |
| Xavier Edwards | Hits | Over | 0.5 | -198 | 68% | 1 | -1.4% | ✅ |
| Connor Norby | H+R+RBI | Over | 0.5 | -154 | 63% | 2 | +2.7% | ✅ |
| Brooks Lee | RBI | Over | 0.5 | +167 | 39% | 0 | +0.4% | ❌ |
| Ryan Jeffers | H+R+RBI | Under | 2.5 | -146 | 61% | 1 | -0.3% | ✅ |
| Mike Trout | Hits | Over | 0.5 | -190 | 67% | 1 | -2.5% | ✅ |
| Javier Sanoja | Hits | Over | 0.5 | -212 | 69% | 0 | -2.7% | ❌ |
| Eugenio Suarez | H+R+RBI | Under | 1.5 | -134 | 59% | 1 | +0.3% | ✅ |
| Parker Messick | Ks (P) | Under | 6.5 | +121 | 46% | 4 | -0.5% | ✅ |
| Javier Baez | H+R+RBI | Over | 0.5 | -161 | 64% | 1 | -1.5% | ✅ |
| Zack Gelof | Hits | Under | 0.5 | +150 | 41% | 2 | -6.7% | ❌ |
| Tyler Stephenson | RBI | Under | 0.5 | -220 | 71% | 0 | +3.9% | ✅ |
| Nathaniel Lowe | RBI | Under | 0.5 | -243 | 73% | 1 | +0.9% | ❌ |
| Kyle Schwarber | Hits | Over | 0.5 | -154 | 62% | 0 | -1.6% | ❌ |
| Carlos Cortes | Hits | Under | 0.5 | +158 | 39% | 0 | +11.7% | ✅ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | -137 | 59% | 2 | +0.0% | ✅ |
| Corey Seager | Hits | Over | 0.5 | -222 | 70% | 3 | -2.5% | ✅ |
| Vaughn Grissom | Hits | Under | 0.5 | +135 | 43% | 0 | -2.5% | ✅ |
| Rafael Devers | H+R+RBI | Over | 1.5 | +116 | 47% | 7 | -5.3% | ✅ |
| Colson Montgomery | RBI | Over | 0.5 | +183 | 36% | 0 | -2.1% | ❌ |
| Dominic Canzone | H+R+RBI | Under | 1.5 | -170 | 64% | 2 | -5.0% | ❌ |
| Dylan Crews | Hits | Under | 0.5 | +169 | 38% | 0 | -2.2% | ✅ |
| Sandy Alcantara | Ks (P) | Under | 4.5 | -108 | 52% | 6 | +8.9% | ❌ |
| Tim Tawa | Hits | Over | 0.5 | -172 | 64% | 1 | -0.2% | ✅ |
| Luke Keaschall | RBI | Under | 0.5 | -244 | 72% | 2 | -0.1% | ❌ |
| Willson Contreras | Hits | Under | 0.5 | +168 | 38% | 0 | +5.1% | ✅ |
| Lawrence Butler | Hits | Under | 0.5 | +144 | 42% | 1 | -9.3% | ❌ |
| Braden Montgomery | RBI | Over | 0.5 | +203 | 34% | 0 | -1.9% | ❌ |
| Brandon Nimmo | H+R+RBI | Under | 1.5 | -113 | 54% | 0 | +4.3% | ✅ |
| Matt McLain | H+R+RBI | Under | 1.5 | -147 | 61% | 0 | +2.4% | ✅ |
| Luis Arraez | H+R+RBI | Over | 1.5 | -105 | 52% | 1 | -1.4% | ❌ |
| Daylen Lile | H+R+RBI | Under | 1.5 | +125 | 45% | 10 | +9.8% | ❌ |
| Miguel Vargas | Hits | Over | 0.5 | -209 | 68% | 1 | -1.3% | ✅ |
| Nick Fortes | H+R+RBI | Under | 1.5 | -160 | 62% | 0 | — | ✅ |
| Brandon Nimmo | RBI | Under | 0.5 | -243 | 72% | 0 | +0.8% | ✅ |
| Elly De La Cruz | RBI | Over | 0.5 | +218 | 32% | 0 | +0.6% | ❌ |
| Jose Fernandez | H+R+RBI | Under | 1.5 | -149 | 60% | 1 | — | ✅ |
| Zach Neto | Hits | Over | 0.5 | -221 | 69% | 1 | -2.2% | ✅ |
| Dominic Canzone | Hits | Under | 0.5 | +117 | 46% | 1 | -4.0% | ❌ |
| Jarren Duran | RBI | Over | 0.5 | +224 | 31% | 0 | +1.2% | ❌ |
| Nick Gonzales | H+R+RBI | Under | 1.5 | -116 | 54% | 0 | +3.5% | ✅ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -158 | 62% | 3 | +0.0% | ❌ |
| Mickey Moniak | H+R+RBI | Over | 1.5 | +105 | 49% | 2 | — | ✅ |
| Nolan Arenado | H+R+RBI | Over | 1.5 | +101 | 50% | 0 | -4.7% | ❌ |
| Caleb Durbin | Hits | Under | 0.5 | +141 | 42% | 1 | +2.5% | ❌ |
| J.T. Realmuto | H+R+RBI | Over | 0.5 | -171 | 64% | 3 | -1.3% | ✅ |
| Drew Romo | H+R+RBI | Over | 0.5 | -131 | 57% | 1 | +0.0% | ✅ |
| Jung Hoo Lee | Hits | Over | 0.5 | -234 | 70% | 1 | -2.4% | ✅ |
| Jake Burger | H+R+RBI | Over | 1.5 | +119 | 46% | 5 | -1.8% | ✅ |
| Jacob Young | H+R+RBI | Under | 1.5 | -138 | 58% | 4 | +0.6% | ❌ |
| Kevin McGonigle | RBI | Over | 0.5 | +239 | 30% | 0 | -3.1% | ❌ |
| Bryce Harper | RBI | Over | 0.5 | +215 | 32% | 0 | +0.0% | ❌ |
| Jose Fernandez | Hits | Over | 0.5 | -173 | 64% | 1 | — | ✅ |
| Sal Stewart | Hits | Under | 1.5 | -242 | 71% | 1 | +1.1% | ✅ |
| Joc Pederson | Hits | Under | 0.5 | +117 | 46% | 0 | +1.9% | ✅ |
| Bryce Harper | Hits | Over | 0.5 | -156 | 61% | 2 | +0.0% | ✅ |
| Jonathan Aranda | Hits | Over | 0.5 | -199 | 66% | 1 | -13.7% | ✅ |
| Jung Hoo Lee | H+R+RBI | Under | 1.5 | -124 | 55% | 2 | +4.1% | ❌ |
| Andrew Benintendi | RBI | Over | 0.5 | +188 | 35% | 0 | +0.0% | ❌ |
| Heriberto Hernandez | H+R+RBI | Under | 1.5 | -142 | 59% | 2 | -18.9% | ❌ |
| Jake McCarthy | H+R+RBI | Over | 1.5 | -110 | 52% | 1 | — | ❌ |
| Miguel Vargas | H+R+RBI | Over | 1.5 | -115 | 53% | 1 | +0.0% | ❌ |
| Carson Kelly | RBI | Over | 0.5 | +215 | 32% | 1 | -1.9% | ✅ |
| Josh Bell | H+R+RBI | Under | 2.5 | -160 | 61% | 5 | -1.5% | ❌ |
| Brooks Lee | H+R+RBI | Under | 1.5 | +101 | 50% | 2 | -1.0% | ❌ |
| Caleb Durbin | H+R+RBI | Over | 1.5 | +116 | 46% | 1 | +0.5% | ❌ |
| Dylan Crews | RBI | Under | 0.5 | -235 | 70% | 1 | +0.6% | ❌ |
| Gavin Sheets | H+R+RBI | Over | 0.5 | -149 | 60% | 0 | +2.8% | ❌ |
| Corey Seager | RBI | Under | 0.5 | -238 | 70% | 3 | +2.7% | ❌ |
| Cal Raleigh | H+R+RBI | Over | 0.5 | -145 | 59% | 10 | -1.7% | ✅ |
| Mickey Gasper | H+R+RBI | Over | 1.5 | +130 | 43% | 3 | — | ✅ |
| Trea Turner | H+R+RBI | Over | 1.5 | +105 | 48% | 0 | -2.8% | ❌ |
| Jacob Young | Hits | Under | 0.5 | +137 | 42% | 2 | +3.0% | ❌ |
| Keibert Ruiz | Hits | Over | 0.5 | -234 | 70% | 2 | -1.9% | ✅ |
| Xander Bogaerts | H+R+RBI | Over | 0.5 | -179 | 64% | 0 | — | ❌ |
| Adley Rutschman | Hits | Over | 0.5 | -204 | 67% | 0 | -1.5% | ❌ |
| Alec Bohm | Hits | Over | 0.5 | -185 | 64% | 0 | +0.2% | ❌ |
| Ty France | H+R+RBI | Under | 1.5 | -138 | 57% | 1 | -1.2% | ✅ |
| Luis Arraez | RBI | Over | 0.5 | +239 | 29% | 0 | -3.4% | ❌ |
| Ryan Vilade | Hits | Over | 0.5 | -187 | 65% | 1 | — | ✅ |
| Ceddanne Rafaela | H+R+RBI | Over | 1.5 | -118 | 53% | 1 | -16.0% | ❌ |
| Braden Montgomery | H+R+RBI | Over | 1.5 | -102 | 50% | 2 | +0.0% | ✅ |
| Colson Montgomery | Hits | Over | 0.5 | -152 | 60% | 0 | -0.3% | ❌ |
| Corbin Carroll | H+R+RBI | Under | 1.5 | -105 | 50% | 0 | -1.9% | ✅ |
| Corey Seager | H+R+RBI | Under | 1.5 | -110 | 51% | 7 | +3.3% | ❌ |
| Ian Happ | H+R+RBI | Over | 1.5 | -119 | 53% | 4 | -2.0% | ✅ |
| Spencer Torkelson | H+R+RBI | Over | 0.5 | -173 | 62% | 1 | -1.8% | ✅ |
| Wyatt Langford | Hits | Over | 0.5 | -213 | 67% | 2 | -1.2% | ✅ |
| Colson Montgomery | H+R+RBI | Over | 1.5 | +112 | 46% | 0 | -1.9% | ❌ |
| JJ Bleday | RBI | Over | 0.5 | +221 | 30% | 0 | -5.6% | ❌ |
| Julio Rodriguez | H+R+RBI | Over | 1.5 | +126 | 43% | 7 | +1.4% | ✅ |
| Nico Hoerner | RBI | Over | 0.5 | +188 | 34% | 1 | +0.0% | ✅ |
| Nick Fortes | Hits | Over | 0.5 | -164 | 61% | 0 | — | ❌ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | -116 | 52% | 1 | -0.4% | ❌ |
| Michael Busch | H+R+RBI | Under | 1.5 | +106 | 47% | 1 | -1.0% | ✅ |
| Wilyer Abreu | H+R+RBI | Under | 1.5 | -112 | 51% | 2 | +19.2% | ❌ |
| Corbin Carroll | Hits | Under | 0.5 | +176 | 36% | 0 | -0.4% | ✅ |
| Ezequiel Duran | RBI | Over | 0.5 | +211 | 31% | 2 | -1.9% | ✅ |
| Willson Contreras | RBI | Over | 0.5 | +166 | 36% | 0 | -20.6% | ❌ |
| Sal Stewart | H+R+RBI | Under | 1.5 | +116 | 45% | 1 | +1.9% | ✅ |
| Vaughn Grissom | H+R+RBI | Over | 1.5 | +130 | 42% | 1 | +2.7% | ❌ |
| Nolan Arenado | Hits | Under | 0.5 | +136 | 42% | 0 | +3.1% | ✅ |
| Javier Sanoja | H+R+RBI | Under | 1.5 | -139 | 56% | 0 | +4.5% | ✅ |
| Miguel Vargas | RBI | Over | 0.5 | +169 | 36% | 0 | +0.0% | ❌ |
| Junior Caminero | H+R+RBI | Over | 1.5 | -139 | 56% | 2 | — | ✅ |
| Esmerlyn Valdez | H+R+RBI | Under | 1.5 | -139 | 56% | 3 | +1.8% | ❌ |
| Sam Antonacci | H+R+RBI | Under | 1.5 | -119 | 53% | 0 | +0.0% | ✅ |
| Ildemaro Vargas | H+R+RBI | Under | 1.5 | -133 | 55% | 1 | +4.3% | ✅ |
| Elly De La Cruz | Hits | Over | 0.5 | -245 | 70% | 1 | -1.1% | ✅ |
| Dillon Dingler | RBI | Over | 0.5 | +181 | 34% | 0 | -3.1% | ❌ |
| Manny Machado | H+R+RBI | Under | 1.5 | -143 | 57% | 0 | +0.0% | ✅ |
| Ezequiel Duran | H+R+RBI | Over | 1.5 | +107 | 47% | 5 | -2.4% | ✅ |
| Pedro Ramirez | Hits | Over | 0.5 | -214 | 67% | 2 | +0.0% | ✅ |
| Brooks Lee | Hits | Under | 0.5 | +188 | 34% | 1 | +3.2% | ❌ |
| Jackson Merrill | RBI | Over | 0.5 | +198 | 32% | 0 | +5.7% | ❌ |
| Alec Bohm | H+R+RBI | Over | 1.5 | +112 | 46% | 1 | -1.9% | ❌ |
| Denzer Guzman | H+R+RBI | Over | 0.5 | -165 | 60% | 0 | -1.6% | ❌ |
| Javier Baez | Hits | Under | 0.5 | +101 | 49% | 1 | +3.0% | ❌ |
| Zach McKinstry | H+R+RBI | Under | 0.5 | +127 | 42% | 0 | +5.6% | ✅ |
| TJ Rumfield | H+R+RBI | Over | 1.5 | -105 | 49% | 1 | +4.4% | ❌ |
| Michael Busch | RBI | Under | 0.5 | -207 | 65% | 0 | -1.0% | ✅ |
| Bryson Stott | H+R+RBI | Over | 1.5 | +134 | 41% | 1 | — | ❌ |
| Nick Gonzales | Hits | Over | 0.5 | -233 | 68% | 0 | -1.2% | ❌ |
| Tim Tawa | H+R+RBI | Under | 1.5 | -152 | 58% | 1 | +0.3% | ✅ |
| Trea Turner | Hits | Over | 0.5 | -205 | 66% | 0 | -1.5% | ❌ |
| Bryson Stott | Hits | Under | 0.5 | +110 | 46% | 1 | +1.9% | ❌ |
| TJ Rumfield | RBI | Over | 0.5 | +214 | 31% | 0 | +16.3% | ❌ |
| Kumar Rocker | Ks (P) | Under | 4.5 | +109 | 47% | 8 | +6.5% | ❌ |
| Donovan Walton | H+R+RBI | Under | 1.5 | -165 | 60% | 0 | -8.6% | ✅ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -110 | 50% | 2 | -6.9% | ✅ |
| Brandon Nimmo | Hits | Over | 0.5 | -242 | 69% | 0 | -3.7% | ❌ |
| Griffin Conine | RBI | Over | 0.5 | +240 | 28% | 0 | — | ❌ |
| Keibert Ruiz | H+R+RBI | Over | 1.5 | -116 | 52% | 3 | -2.5% | ✅ |
| Keibert Ruiz | RBI | Over | 0.5 | +187 | 33% | 0 | -4.3% | ❌ |
| Evan Carter | H+R+RBI | Over | 0.5 | -154 | 58% | 3 | -1.3% | ✅ |
| JJ Bleday | H+R+RBI | Over | 1.5 | +121 | 43% | 0 | -0.9% | ❌ |
| Pete Crow-Armstrong | H+R+RBI | Under | 2.5 | -148 | 57% | 0 | -0.3% | ✅ |
| Zach McKinstry | Hits | Under | 0.5 | +104 | 48% | 0 | +4.5% | ✅ |
| Griffin Conine | H+R+RBI | Under | 1.5 | -174 | 61% | 0 | — | ✅ |
| Andrew Benintendi | H+R+RBI | Under | 1.5 | -141 | 56% | 0 | +2.0% | ✅ |
| Xavier Edwards | H+R+RBI | Under | 1.5 | -140 | 56% | 2 | — | ❌ |
| Royce Lewis | Hits | Under | 1.5 | -231 | 68% | 1 | +0.0% | ✅ |
| Zach Neto | H+R+RBI | Over | 1.5 | -112 | 50% | 2 | -1.7% | ✅ |
| Adley Rutschman | H+R+RBI | Under | 1.5 | -129 | 54% | 0 | +5.1% | ✅ |
| Jackson Merrill | H+R+RBI | Under | 1.5 | -131 | 54% | 0 | -1.0% | ✅ |
| Fernando Tatis Jr. | H+R+RBI | Over | 1.5 | -130 | 54% | 0 | +2.9% | ❌ |
| Ryan Jeffers | RBI | Under | 0.5 | -190 | 62% | 0 | -2.7% | ✅ |
| Dillon Dingler | H+R+RBI | Under | 1.5 | -128 | 53% | 1 | +0.7% | ✅ |
| Javier Sanoja | RBI | Over | 0.5 | +229 | 29% | 0 | -13.4% | ❌ |
| Elly De La Cruz | H+R+RBI | Under | 1.5 | +101 | 47% | 1 | +2.0% | ✅ |
| Manny Machado | RBI | Over | 0.5 | +200 | 32% | 0 | +2.7% | ❌ |
| Zack Gelof | H+R+RBI | Over | 1.5 | -112 | 50% | 3 | +5.5% | ✅ |
| Griffin Conine | Hits | Over | 0.5 | -141 | 57% | 0 | — | ❌ |
| Kody Clemens | H+R+RBI | Over | 1.5 | -144 | 56% | 4 | — | ✅ |
| Daylen Lile | Hits | Under | 1.5 | -238 | 68% | 3 | — | ❌ |
| Willson Contreras | H+R+RBI | Over | 1.5 | -118 | 51% | 0 | -5.4% | ❌ |
| Tim Tawa | RBI | Over | 0.5 | +231 | 28% | 0 | +0.0% | ❌ |
| Kyle Schwarber | H+R+RBI | Over | 1.5 | +100 | 47% | 1 | +0.0% | ❌ |
| Donovan Walton | Hits | Over | 0.5 | -140 | 56% | 0 | +10.0% | ❌ |
| Josh Naylor | H+R+RBI | Over | 1.5 | +124 | 42% | 3 | +0.9% | ✅ |
| Ezequiel Tovar | Hits | Under | 0.5 | -107 | 50% | 2 | -0.9% | ❌ |
| Munetaka Murakami | RBI | Over | 0.5 | +158 | 36% | 0 | +0.0% | ❌ |
| Wyatt Langford | H+R+RBI | Under | 1.5 | -125 | 52% | 6 | +0.7% | ❌ |
| Jonathan Aranda | H+R+RBI | Under | 1.5 | -123 | 52% | 4 | — | ❌ |
| Brett Sullivan | Hits | Under | 0.5 | +103 | 47% | 0 | -5.6% | ✅ |
| Colt Keith | Hits | Under | 0.5 | +121 | 44% | 0 | -3.9% | ✅ |
| Mike Trout | H+R+RBI | Over | 1.5 | +108 | 45% | 1 | -1.9% | ❌ |
| Nico Hoerner | H+R+RBI | Under | 1.5 | +101 | 46% | 1 | +0.0% | ✅ |
| Yandy Diaz | H+R+RBI | Under | 1.5 | +115 | 43% | 2 | — | ❌ |
| Jacob Young | RBI | Over | 0.5 | +228 | 28% | 0 | -2.1% | ❌ |
| Geraldo Perdomo | H+R+RBI | Over | 1.5 | +101 | 46% | 1 | +2.0% | ❌ |
| Carson Kelly | H+R+RBI | Over | 1.5 | +105 | 45% | 3 | +2.0% | ✅ |
| Jarren Duran | H+R+RBI | Over | 1.5 | +112 | 44% | 3 | +0.9% | ✅ |
| Ty France | RBI | Over | 0.5 | +215 | 29% | 0 | +2.9% | ❌ |
| Cal Raleigh | RBI | Over | 0.5 | +216 | 29% | 4 | -7.3% | ✅ |
| Cole Young | H+R+RBI | Over | 1.5 | +127 | 41% | 3 | -2.2% | ✅ |
| Nico Hoerner | Hits | Over | 1.5 | +192 | 33% | 0 | +0.0% | ❌ |
| Julio Rodriguez | RBI | Over | 0.5 | +244 | 27% | 3 | +3.0% | ✅ |
| Brett Sullivan | H+R+RBI | Under | 0.5 | +124 | 41% | 0 | — | ✅ |
| Jarren Duran | Hits | Over | 0.5 | -170 | 60% | 2 | -2.3% | ✅ |
| Manny Machado | Hits | Under | 0.5 | +135 | 40% | 0 | +1.3% | ✅ |
| Andrew Benintendi | Hits | Over | 0.5 | -165 | 59% | 0 | -0.2% | ❌ |
| Wilyer Abreu | Hits | Under | 0.5 | +165 | 36% | 1 | +32.5% | ❌ |
| Drew Gilbert | Hits | Under | 0.5 | +106 | 46% | 2 | +2.0% | ❌ |
| Zach Neto | RBI | Over | 0.5 | +196 | 31% | 0 | -4.2% | ❌ |
| Junior Caminero | RBI | Over | 0.5 | +139 | 38% | 1 | — | ✅ |
| Kyle Schwarber | RBI | Over | 0.5 | +161 | 35% | 0 | +0.8% | ❌ |
| Daylen Lile | RBI | Over | 0.5 | +150 | 37% | 5 | +2.0% | ✅ |
| Wilyer Abreu | RBI | Over | 0.5 | +169 | 34% | 0 | -17.2% | ❌ |
| Gavin Sheets | Hits | Under | 0.5 | -109 | 49% | 0 | -1.3% | ✅ |
| Josh Bell | RBI | Over | 0.5 | +128 | 40% | 3 | +0.9% | ✅ |
| Eugenio Suarez | RBI | Over | 0.5 | +177 | 33% | 0 | +0.4% | ❌ |
| Kody Clemens | RBI | Over | 0.5 | +132 | 39% | 2 | +10.5% | ✅ |
| Ian Happ | RBI | Over | 0.5 | +164 | 34% | 1 | -1.9% | ✅ |
| Evan Carter | Hits | Over | 0.5 | -116 | 51% | 1 | -1.6% | ✅ |
| Bryan Reynolds | RBI | Over | 0.5 | +208 | 29% | 0 | -0.3% | ❌ |
| Jo Adell | RBI | Over | 0.5 | +152 | 36% | 1 | +2.0% | ✅ |
| Zebby Matthews | Ks (P) | Under | 4.5 | -138 | 56% | 7 | +2.9% | ❌ |
| Mickey Moniak | Hits | Under | 0.5 | +140 | 39% | 1 | — | ❌ |
| Jonah Heim | RBI | Over | 0.5 | +187 | 31% | 0 | -5.0% | ❌ |
| Jonny Deluca | Hits | Under | 0.5 | +145 | 38% | 2 | — | ❌ |
| Dominic Canzone | RBI | Over | 0.5 | +244 | 26% | 0 | +11.3% | ❌ |
| Pete Crow-Armstrong | Hits | Over | 1.5 | +171 | 34% | 0 | +2.3% | ❌ |
| Ty France | Hits | Under | 0.5 | +140 | 39% | 1 | -2.4% | ❌ |
| Sam Antonacci | Hits | Under | 0.5 | +153 | 37% | 0 | +0.0% | ✅ |
| Ezequiel Duran | Hits | Under | 0.5 | +136 | 40% | 2 | +2.2% | ❌ |
| Fernando Tatis Jr. | Hits | Over | 1.5 | +201 | 31% | 0 | +3.4% | ❌ |
| Spencer Torkelson | RBI | Over | 0.5 | +224 | 27% | 0 | -0.3% | ❌ |
| Cal Raleigh | Hits | Over | 0.5 | -106 | 48% | 3 | -3.8% | ✅ |
| Esmerlyn Valdez | Hits | Under | 0.5 | +117 | 43% | 1 | +1.9% | ❌ |
| Zack Gelof | RBI | Over | 0.5 | +181 | 31% | 1 | +8.1% | ✅ |
| Corbin Carroll | RBI | Over | 0.5 | +178 | 32% | 0 | +1.1% | ❌ |
| Jackson Merrill | Hits | Under | 0.5 | +144 | 38% | 0 | -2.8% | ✅ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +191 | 30% | 1 | -0.3% | ✅ |
| Lars Nootbaar | RBI | Over | 0.5 | +208 | 28% | 0 | -8.1% | ❌ |
| Carson Kelly | Hits | Under | 0.5 | +126 | 41% | 1 | -1.7% | ❌ |
| Yandy Diaz | Hits | Over | 1.5 | +171 | 34% | 1 | +90.1% | ❌ |
| Dillon Dingler | Hits | Under | 0.5 | +159 | 35% | 1 | -0.4% | ❌ |
| Cade Cavalli | Ks (P) | Over | 6.5 | -101 | 47% | 7 | +2.4% | ✅ |
| Jake McCarthy | RBI | Over | 0.5 | +275 | 34% | 0 | -6.2% | ❌ |
| Otto Lopez | RBI | Over | 0.5 | +294 | 30% | 1 | -0.2% | ✅ |
| Vaughn Grissom | RBI | Over | 0.5 | +300 | 30% | 0 | +2.3% | ❌ |
| Caleb Durbin | RBI | Over | 0.5 | +279 | 31% | 0 | +14.8% | ❌ |
| Randy Arozarena | RBI | Over | 0.5 | +303 | 29% | 0 | +3.6% | ❌ |
| Dane Myers | RBI | Under | 0.5 | -273 | 82% | 0 | +1.1% | ✅ |
| Mickey Gasper | RBI | Over | 0.5 | +259 | 31% | 1 | -1.6% | ✅ |
| Otto Lopez | Hits | Over | 0.5 | -256 | 80% | 2 | -14.4% | ✅ |
| Gabriel Moreno | Hits | Over | 0.5 | -252 | 80% | 0 | +1.0% | ❌ |
| Esteury Ruiz | RBI | Under | 0.5 | -379 | 88% | 0 | -0.5% | ✅ |
| Chase Meidroth | RBI | Over | 0.5 | +271 | 30% | 0 | +2.8% | ❌ |
| Jorge Mateo | RBI | Under | 0.5 | -322 | 84% | 0 | +4.8% | ✅ |
| Jose Siri | RBI | Under | 0.5 | -372 | 85% | 0 | +0.9% | ✅ |
| Colt Keith | RBI | Under | 0.5 | -351 | 82% | 0 | +6.1% | ✅ |
| Luis Rengifo | RBI | Over | 0.5 | +291 | 27% | 0 | — | ❌ |
| J.T. Realmuto | RBI | Over | 0.5 | +288 | 27% | 1 | -2.8% | ✅ |
| Lawrence Butler | RBI | Under | 0.5 | -251 | 74% | 1 | -5.7% | ❌ |
| Ceddanne Rafaela | Hits | Over | 0.5 | -252 | 74% | 1 | -12.1% | ✅ |
| Ezequiel Tovar | RBI | Over | 0.5 | +335 | 24% | 1 | +8.8% | ✅ |
| Moises Ballesteros | RBI | Under | 0.5 | -346 | 80% | 1 | +1.9% | ❌ |
| Weston Wilson | RBI | Under | 0.5 | -535 | 86% | 0 | +0.0% | ✅ |
| Junior Caminero | Hits | Over | 0.5 | -268 | 75% | 1 | -7.7% | ✅ |
| Michael Conforto | RBI | Under | 0.5 | -254 | 74% | 2 | +1.4% | ❌ |
| Donovan Walton | RBI | Under | 0.5 | -329 | 78% | 0 | -4.0% | ✅ |
| Jorbit Vivas | RBI | Under | 0.5 | -335 | 78% | 2 | +0.3% | ❌ |
| Nick Gonzales | RBI | Over | 0.5 | +265 | 28% | 0 | +3.1% | ❌ |
| Jose Fernandez | RBI | Under | 0.5 | -344 | 78% | 0 | — | ✅ |
| Joc Pederson | RBI | Under | 0.5 | -282 | 74% | 0 | +3.4% | ✅ |
| Michael Busch | Hits | Over | 0.5 | -252 | 72% | 0 | -0.3% | ❌ |
| Freddy Fermin | RBI | Under | 0.5 | -490 | 83% | 0 | -0.6% | ✅ |
| Brett Sullivan | RBI | Over | 0.5 | +270 | 27% | 0 | +5.7% | ❌ |
| Zach McKinstry | RBI | Under | 0.5 | -438 | 81% | 0 | +2.4% | ✅ |
| Jung Hoo Lee | RBI | Under | 0.5 | -306 | 75% | 1 | +2.7% | ❌ |
| Henry Bolte | RBI | Under | 0.5 | -290 | 74% | 0 | -2.8% | ✅ |
| Denzer Guzman | RBI | Over | 0.5 | +307 | 24% | 0 | -6.2% | ❌ |
| Bryson Stott | RBI | Over | 0.5 | +255 | 28% | 0 | -3.8% | ❌ |
| Xander Bogaerts | RBI | Over | 0.5 | +288 | 26% | 0 | +3.2% | ❌ |
| Tristan Peters | RBI | Over | 0.5 | +288 | 26% | 2 | +2.6% | ✅ |
| Ryan Vilade | RBI | Under | 0.5 | -283 | 73% | 0 | +3.9% | ✅ |
| Pedro Ramirez | RBI | Under | 0.5 | -271 | 72% | 1 | -0.2% | ❌ |
| Evan Carter | RBI | Under | 0.5 | -409 | 79% | 1 | +1.6% | ❌ |
| Trea Turner | RBI | Over | 0.5 | +272 | 26% | 0 | -0.3% | ❌ |
| Mike Trout | RBI | Under | 0.5 | -306 | 74% | 0 | +1.5% | ✅ |
| Connor Norby | RBI | Under | 0.5 | -404 | 79% | 1 | -0.7% | ❌ |
| Geraldo Perdomo | RBI | Under | 0.5 | -285 | 72% | 0 | +1.2% | ✅ |
| Matt McLain | RBI | Under | 0.5 | -313 | 74% | 0 | +0.8% | ✅ |
| Jeff McNeil | RBI | Under | 0.5 | -254 | 70% | 2 | -1.3% | ❌ |
| Nick Fortes | RBI | Under | 0.5 | -327 | 75% | 0 | — | ✅ |
| Wyatt Langford | RBI | Under | 0.5 | -279 | 72% | 2 | -0.6% | ❌ |
| Brandon Marsh | RBI | Over | 0.5 | +273 | 26% | 0 | -0.3% | ❌ |
| Brayan Rocchio | RBI | Under | 0.5 | -334 | 75% | 0 | +1.4% | ✅ |
| Jonny Deluca | RBI | Under | 0.5 | -312 | 74% | 0 | +2.0% | ✅ |
| Drew Romo | RBI | Over | 0.5 | +288 | 25% | 0 | -2.3% | ❌ |
| Xavier Edwards | RBI | Over | 0.5 | +251 | 27% | 1 | — | ✅ |
| Sam Antonacci | RBI | Over | 0.5 | +264 | 26% | 0 | -1.1% | ❌ |
| Taylor Ward | RBI | Over | 0.5 | +342 | 21% | 0 | +8.6% | ❌ |
| Cole Young | RBI | Over | 0.5 | +261 | 25% | 1 | -2.7% | ✅ |
| Josh Naylor | RBI | Over | 0.5 | +260 | 25% | 0 | +2.3% | ❌ |
| Gavin Sheets | RBI | Over | 0.5 | +281 | 24% | 0 | +1.1% | ❌ |
| Javier Baez | RBI | Over | 0.5 | +305 | 22% | 0 | -8.0% | ❌ |
| Drew Gilbert | RBI | Over | 0.5 | +340 | 20% | 0 | -5.4% | ❌ |
| Jake Cronenworth | RBI | Over | 0.5 | +276 | 23% | 1 | +1.1% | ✅ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Colorado Rockies @ Washington Nationals | **NRFI** | High | 66% | 53% | ✅ |
| Texas Rangers @ Chicago White Sox | **NRFI** | High | 57% | 47% | ❌ |
| Philadelphia Phillies @ Seattle Mariners | **YRFI** | High | 54% | 42% | ✅ |
| Tampa Bay Rays @ Detroit Tigers | **NRFI** | Coin flip | 54% | 55% | ❌ |
| Boston Red Sox @ Miami Marlins | **NRFI** | Coin flip | 59% | 57% | ✅ |
| Cleveland Guardians @ Los Angeles Angels | **NRFI** | Coin flip | 53% | 52% | ✅ |
| Chicago Cubs @ Arizona Diamondbacks | **YRFI** | Coin flip | 54% | 53% | ❌ |
| Cincinnati Reds @ San Francisco Giants | **NRFI** | Coin flip | 53% | 57% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Byron Buxton | Minnesota Twins @ Athletics | 28% | ❌ |
| 2 | Munetaka Murakami | Texas Rangers @ Chicago White Sox | 27% | ❌ |
| 3 | Pete Crow-Armstrong | Chicago Cubs @ Arizona Diamondbacks | 25% | ❌ |
| 4 | CJ Abrams | Colorado Rockies @ Washington Nationals | 24% | ❌ |
| 5 | Kody Clemens | Minnesota Twins @ Athletics | 22% | ❌ |
| 6 | Colson Montgomery | Texas Rangers @ Chicago White Sox | 22% | ❌ |
| 7 | Zack Gelof | Minnesota Twins @ Athletics | 22% | ❌ |
| 8 | Miguel Vargas | Texas Rangers @ Chicago White Sox | 22% | ❌ |
| 9 | Joc Pederson | Texas Rangers @ Chicago White Sox | 22% | ❌ |
| 10 | Kyle Schwarber | Philadelphia Phillies @ Seattle Mariners | 22% | ❌ |

*0 homered · model expected 2.4*

---

### 2026-08-23 — bets 10-5 (+2.60u) · props 280-327 · NRFI 8-7 · HR 1-9

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Tampa Bay Rays ML | — | -108 | 9.5 | — | ✅ +0.93u |
| Moneyline | Cleveland Guardians ML | — | -164 | 9.5 | — | ✅ +0.61u |
| Total | Under 11.5 | 11.5 | +100 | 9.5 | — | ✅ +1.00u |
| Moneyline | Boston Red Sox ML | — | -220 | 9.5 | — | ✅ +0.45u |
| Moneyline | Chicago Cubs ML | — | -108 | 9.5 | — | ✅ +0.93u |
| Moneyline | Arizona Diamondbacks ML | — | -126 | 9.5 | +73.6% | ✅ +0.79u |
| Total | Over 7.5 | 7.5 | +100 | 8.3 | — | ❌ -1.00u |
| Moneyline | Philadelphia Phillies ML | — | -220 | 7.4 | — | ✅ +0.45u |
| F5 Total | F5 Over 4.5 | 4.5 | -110 | 7.3 | — | ❌ -1.00u |
| Moneyline | Milwaukee Brewers ML | — | -132 | 5.7 | -8.3% | ❌ -1.00u |
| NRFI | NRFI | 0.5 | -125 | 5.5 | — | ❌ -1.00u |
| NRFI | NRFI | 0.5 | -128 | 5.3 | — | ✅ +0.78u |
| F5 Total | F5 Over 4.5 | 4.5 | -146 | 5.1 | — | ✅ +0.68u |
| NRFI | NRFI | 0.5 | -102 | 5.1 | — | ✅ +0.98u |
| F5 Total | F5 Over 4.5 | 4.5 | -146 | 5.1 | — | ❌ -1.00u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Lake Bachar | Ks (P) | Over | 2.5 | +137 | 96% | 1 | — | ❌ |
| Cal Quantrill | Ks (P) | Over | 3.5 | -137 | 83% | 6 | — | ✅ |
| Shane Drohan | Ks (P) | Over | 4.5 | +100 | 70% | 5 | +9.9% | ✅ |
| Cristian Javier | Ks (P) | Under | 4.5 | -122 | 74% | 8 | — | ❌ |
| Cristopher Sanchez | Ks (P) | Under | 6.5 | +110 | 61% | 7 | — | ❌ |
| Francisco Alvarez | Hits | Under | 0.5 | +145 | 58% | 0 | — | ✅ |
| Kyle Leahy | Ks (P) | Over | 3.5 | -132 | 72% | 0 | — | ❌ |
| Dane Myers | Hits | Under | 0.5 | +160 | 53% | 2 | — | ❌ |
| Myles Straw | Hits | Under | 0.5 | -112 | 73% | 2 | — | ❌ |
| Oneil Cruz | Hits | Over | 0.5 | -107 | 70% | 0 | — | ❌ |
| Otto Lopez | Hits | Over | 1.5 | +169 | 50% | 0 | — | ❌ |
| Jorbit Vivas | Hits | Under | 0.5 | +132 | 58% | 1 | — | ❌ |
| Francisco Lindor | Hits | Under | 0.5 | +180 | 46% | 2 | — | ❌ |
| Eli White | Hits | Under | 0.5 | +117 | 60% | 0 | — | ✅ |
| Mickey Moniak | Hits | Under | 0.5 | +155 | 50% | 0 | — | ✅ |
| Dylan Crews | Hits | Under | 0.5 | +195 | 43% | 2 | — | ❌ |
| Eugenio Suarez | Hits | Under | 0.5 | +127 | 56% | 1 | — | ❌ |
| Alec Burleson | RBI | Over | 0.5 | +233 | 43% | 0 | — | ❌ |
| Luis Arraez | Hits | Over | 1.5 | +191 | 43% | 0 | — | ❌ |
| Teoscar Hernandez | Hits | Under | 0.5 | +145 | 51% | 0 | — | ✅ |
| Jordan Walker | RBI | Over | 0.5 | +226 | 44% | 0 | — | ❌ |
| Hunter Feduccia | Hits | Under | 0.5 | -105 | 64% | 1 | — | ❌ |
| Tommy Edman | Hits | Under | 0.5 | +170 | 46% | 0 | — | ✅ |
| Jake Burger | Hits | Over | 0.5 | -156 | 75% | 0 | — | ❌ |
| Willson Contreras | Hits | Under | 0.5 | +192 | 42% | 0 | — | ✅ |
| Gleyber Torres | Hits | Under | 0.5 | +168 | 45% | 1 | — | ❌ |
| Myles Straw | H+R+RBI | Under | 0.5 | +111 | 64% | 3 | — | ❌ |
| Luis Robert Jr. | Hits | Under | 0.5 | +149 | 49% | 1 | — | ❌ |
| Jake Bennett | Ks (P) | Under | 4.5 | +100 | 57% | 6 | — | ❌ |
| Tim Tawa | Hits | Under | 0.5 | +143 | 50% | 2 | — | ❌ |
| Brett Baty | Hits | Under | 0.5 | -104 | 61% | 0 | — | ✅ |
| Brandon Marsh | Hits | Over | 0.5 | -179 | 77% | 0 | — | ❌ |
| Caleb Durbin | Hits | Under | 0.5 | +182 | 42% | 0 | — | ✅ |
| Tomoyuki Sugano | Ks (P) | Over | 2.5 | -105 | 58% | 2 | — | ❌ |
| Josh Naylor | Hits | Over | 0.5 | -156 | 73% | 2 | — | ✅ |
| Vaughn Grissom | Hits | Under | 0.5 | +151 | 47% | 1 | — | ❌ |
| Oneil Cruz | H+R+RBI | Over | 0.5 | -144 | 77% | 0 | — | ❌ |
| Isaac Paredes | Hits | Over | 0.5 | -225 | 82% | 1 | — | ✅ |
| Justin Crawford | Hits | Over | 0.5 | -137 | 68% | 0 | — | ❌ |
| Jordan Walker | H+R+RBI | Over | 1.5 | +110 | 62% | 0 | — | ❌ |
| Eli White | H+R+RBI | Under | 1.5 | -150 | 77% | 0 | — | ✅ |
| Weston Wilson | Hits | Under | 0.5 | -119 | 64% | 1 | — | ❌ |
| Hao-Yu Lee | H+R+RBI | Under | 1.5 | -125 | 71% | 5 | — | ❌ |
| Francisco Alvarez | H+R+RBI | Under | 1.5 | -124 | 71% | 0 | — | ✅ |
| Hao-Yu Lee | Hits | Under | 0.5 | +148 | 47% | 2 | — | ❌ |
| Mookie Betts | Hits | Under | 0.5 | +194 | 40% | 1 | — | ❌ |
| Dane Myers | H+R+RBI | Under | 1.5 | -127 | 71% | 3 | — | ❌ |
| Bryce Miller | Ks (P) | Under | 4.5 | +121 | 50% | 5 | — | ❌ |
| Jordan Walker | Hits | Over | 0.5 | -204 | 77% | 0 | — | ❌ |
| Hunter Feduccia | H+R+RBI | Under | 1.5 | -170 | 78% | 2 | — | ❌ |
| Moises Ballesteros | Hits | Under | 0.5 | +133 | 49% | 2 | — | ❌ |
| Christian Vazquez | Hits | Over | 0.5 | -121 | 63% | 0 | — | ❌ |
| Xander Bogaerts | Hits | Under | 0.5 | +139 | 48% | 1 | — | ❌ |
| Austin Riley | Hits | Over | 0.5 | -137 | 66% | 2 | -0.3% | ✅ |
| Brandon Nimmo | Hits | Over | 0.5 | -239 | 80% | 0 | — | ❌ |
| Cole Carrigg | Hits | Under | 1.5 | -225 | 79% | 0 | — | ✅ |
| Chase DeLauter | H+R+RBI | Under | 2.5 | -108 | 63% | 7 | — | ❌ |
| Brice Turang | Hits | Over | 0.5 | -180 | 73% | 1 | +1.0% | ✅ |
| Bailey Ober | Ks (P) | Under | 3.5 | -115 | 58% | 3 | — | ✅ |
| Yandy Diaz | Hits | Over | 1.5 | +177 | 41% | 0 | — | ❌ |
| Ezequiel Tovar | Hits | Under | 0.5 | +131 | 49% | 1 | — | ❌ |
| Trent Grisham | Hits | Under | 0.5 | +122 | 51% | 0 | — | ✅ |
| Nolan McLean | Ks (P) | Over | 6.5 | +121 | 49% | 6 | — | ❌ |
| Alec Burleson | H+R+RBI | Over | 1.5 | +121 | 55% | 0 | — | ❌ |
| Brandon Lowe | H+R+RBI | Over | 0.5 | -138 | 70% | 1 | — | ✅ |
| Brooks Lee | Hits | Over | 0.5 | -175 | 72% | 1 | — | ✅ |
| Shohei Ohtani | H+R+RBI | Under | 2.5 | -133 | 69% | 1 | — | ✅ |
| Mookie Betts | H+R+RBI | Under | 1.5 | +108 | 58% | 1 | — | ✅ |
| Corbin Carroll | Hits | Over | 0.5 | -220 | 77% | 2 | — | ✅ |
| Christian Yelich | Hits | Over | 0.5 | -136 | 65% | 2 | +3.0% | ✅ |
| Nathaniel Lowe | H+R+RBI | Under | 2.5 | -135 | 69% | 3 | — | ❌ |
| David Hamilton | Hits | Over | 0.5 | -116 | 60% | 0 | -5.5% | ❌ |
| JJ Wetherholt | H+R+RBI | Over | 1.5 | +135 | 51% | 1 | — | ❌ |
| Tommy Edman | H+R+RBI | Under | 1.5 | -109 | 62% | 1 | — | ✅ |
| Cole Young | Hits | Over | 0.5 | -130 | 63% | 0 | — | ❌ |
| Esteury Ruiz | H+R+RBI | Under | 1.5 | -148 | 71% | 0 | — | ✅ |
| Gleyber Torres | H+R+RBI | Under | 1.5 | -102 | 60% | 3 | — | ❌ |
| Bryan Reynolds | Hits | Over | 0.5 | -153 | 67% | 0 | — | ❌ |
| Kyle Tucker | Hits | Under | 0.5 | +144 | 45% | 1 | — | ❌ |
| Nathaniel Lowe | Hits | Under | 1.5 | -209 | 75% | 1 | — | ✅ |
| Tyrone Taylor | H+R+RBI | Under | 0.5 | +130 | 51% | 2 | — | ❌ |
| Bryce Eldridge | Hits | Over | 0.5 | -168 | 69% | 2 | — | ✅ |
| Rafael Devers | RBI | Over | 0.5 | +244 | 34% | 0 | — | ❌ |
| Jonathan Aranda | Hits | Over | 0.5 | -233 | 77% | 0 | — | ❌ |
| Freddie Freeman | H+R+RBI | Under | 1.5 | +117 | 54% | 3 | — | ❌ |
| Moises Ballesteros | H+R+RBI | Under | 1.5 | -150 | 70% | 3 | — | ❌ |
| Drake Baldwin | RBI | Over | 0.5 | +249 | 33% | 0 | +10.1% | ❌ |
| Donovan Walton | Hits | Over | 0.5 | -118 | 60% | 1 | — | ✅ |
| Brandon Lowe | RBI | Over | 0.5 | +248 | 33% | 0 | — | ❌ |
| Jake Bauers | RBI | Over | 0.5 | +217 | 37% | 1 | +1.3% | ✅ |
| Tim Tawa | H+R+RBI | Under | 1.5 | -129 | 65% | 3 | — | ❌ |
| A.J. Ewing | H+R+RBI | Under | 1.5 | -125 | 64% | 1 | — | ✅ |
| Ian Happ | Hits | Over | 0.5 | -142 | 64% | 2 | — | ✅ |
| Brice Turang | H+R+RBI | Over | 1.5 | +108 | 56% | 2 | +1.0% | ✅ |
| Jackson Holliday | Hits | Under | 0.5 | +155 | 43% | 0 | — | ✅ |
| Spencer Jones | Hits | Under | 0.5 | +115 | 51% | 2 | — | ❌ |
| Michael Harris II | Hits | Over | 0.5 | -192 | 72% | 1 | +10.2% | ✅ |
| Heriberto Hernandez | Hits | Under | 0.5 | +183 | 39% | 1 | — | ❌ |
| Garrett Mitchell | Hits | Over | 0.5 | -123 | 60% | 0 | -6.3% | ❌ |
| Jake Bauers | H+R+RBI | Over | 1.5 | +119 | 53% | 2 | +0.5% | ✅ |
| Liam Hicks | RBI | Over | 0.5 | +204 | 38% | 0 | — | ❌ |
| Francisco Lindor | H+R+RBI | Under | 1.5 | -110 | 60% | 2 | — | ❌ |
| Weston Wilson | H+R+RBI | Under | 0.5 | +109 | 55% | 1 | — | ❌ |
| Ildemaro Vargas | Hits | Under | 1.5 | -247 | 78% | 2 | — | ❌ |
| Jo Adell | H+R+RBI | Under | 2.5 | -129 | 65% | 4 | — | ❌ |
| Adley Rutschman | H+R+RBI | Under | 1.5 | -102 | 58% | 0 | — | ✅ |
| Seiya Suzuki | RBI | Over | 0.5 | +213 | 36% | 0 | — | ❌ |
| Chase Meidroth | Hits | Over | 0.5 | -150 | 65% | 0 | — | ❌ |
| Yusei Kikuchi | Ks (P) | Over | 4.5 | -130 | 60% | 4 | — | ❌ |
| Pete Alonso | Hits | Over | 0.5 | -245 | 77% | 0 | — | ❌ |
| Teoscar Hernandez | H+R+RBI | Under | 1.5 | -124 | 63% | 0 | — | ✅ |
| Christian Yelich | H+R+RBI | Over | 0.5 | -183 | 74% | 3 | — | ✅ |
| A.J. Ewing | Hits | Under | 0.5 | +152 | 43% | 1 | — | ❌ |
| Kyle Tucker | H+R+RBI | Under | 1.5 | -122 | 62% | 2 | — | ❌ |
| Donovan Walton | H+R+RBI | Over | 0.5 | -152 | 68% | 2 | — | ✅ |
| Pedro Pages | Hits | Under | 0.5 | -147 | 64% | 0 | — | ✅ |
| Travis Bazzana | Hits | Over | 1.5 | +194 | 37% | 0 | — | ❌ |
| Willson Contreras | H+R+RBI | Under | 1.5 | +117 | 52% | 0 | — | ✅ |
| Jeremy Pena | Hits | Under | 1.5 | -216 | 74% | 2 | — | ❌ |
| Fernando Tatis Jr. | H+R+RBI | Under | 2.5 | -129 | 64% | 10 | — | ❌ |
| Alex Bregman | RBI | Over | 0.5 | +224 | 35% | 2 | — | ✅ |
| Ivan Herrera | Hits | Over | 0.5 | -175 | 69% | 0 | — | ❌ |
| Ozzie Albies | Hits | Over | 0.5 | -199 | 72% | 2 | +2.7% | ✅ |
| Jo Adell | Hits | Under | 1.5 | -219 | 74% | 2 | — | ❌ |
| Sal Stewart | RBI | Over | 0.5 | +166 | 42% | 1 | — | ✅ |
| Jake Bauers | Hits | Over | 0.5 | -140 | 63% | 1 | +2.3% | ✅ |
| Ivan Herrera | H+R+RBI | Over | 1.5 | +121 | 51% | 0 | — | ❌ |
| Vaughn Grissom | RBI | Over | 0.5 | +250 | 32% | 0 | — | ❌ |
| Andruw Monasterio | H+R+RBI | Under | 1.5 | -134 | 64% | 1 | — | ✅ |
| Jake Burger | H+R+RBI | Over | 1.5 | +112 | 53% | 0 | — | ❌ |
| Randy Arozarena | Hits | Over | 0.5 | -195 | 71% | 1 | — | ✅ |
| Chase DeLauter | Hits | Under | 1.5 | -159 | 66% | 3 | — | ❌ |
| Nolan Arenado | Hits | Under | 0.5 | +155 | 42% | 0 | — | ✅ |
| Christian Walker | Hits | Over | 0.5 | -207 | 72% | 1 | — | ✅ |
| Coby Mayo | Hits | Under | 0.5 | +102 | 53% | 0 | — | ✅ |
| Jacob Young | Hits | Under | 0.5 | +144 | 44% | 0 | — | ✅ |
| Cole Carrigg | H+R+RBI | Under | 1.5 | +119 | 51% | 0 | — | ✅ |
| Garrett Mitchell | H+R+RBI | Over | 0.5 | -169 | 70% | 0 | -6.6% | ❌ |
| Ceddanne Rafaela | H+R+RBI | Under | 1.5 | +113 | 52% | 5 | — | ❌ |
| Ildemaro Vargas | H+R+RBI | Under | 1.5 | +116 | 51% | 5 | — | ❌ |
| George Springer | H+R+RBI | Under | 1.5 | -123 | 61% | 2 | — | ❌ |
| Austin Hedges | Hits | Over | 0.5 | -175 | 68% | 2 | — | ✅ |
| Mitch Bratt | Ks (P) | Under | 3.5 | +120 | 47% | 3 | — | ✅ |
| Jose Soriano | Ks (P) | Over | 5.5 | +105 | 51% | 7 | — | ✅ |
| Justin Foscue | H+R+RBI | Under | 1.5 | -146 | 66% | 0 | — | ✅ |
| Colton Cowser | Hits | Under | 0.5 | -118 | 57% | 2 | — | ❌ |
| Braden Montgomery | Hits | Over | 0.5 | -175 | 68% | 0 | — | ❌ |
| Francisco Alvarez | RBI | Under | 0.5 | -250 | 79% | 0 | — | ✅ |
| Luis Robert Jr. | H+R+RBI | Under | 1.5 | -126 | 61% | 1 | — | ✅ |
| Jorbit Vivas | H+R+RBI | Under | 1.5 | -173 | 70% | 2 | — | ❌ |
| Jeremy Pena | RBI | Over | 0.5 | +191 | 38% | 0 | — | ❌ |
| Austin Riley | H+R+RBI | Over | 0.5 | -173 | 70% | 2 | +0.4% | ✅ |
| Ezequiel Tovar | H+R+RBI | Under | 1.5 | -136 | 63% | 1 | — | ✅ |
| Austin Hedges | H+R+RBI | Under | 1.5 | -126 | 61% | 2 | — | ❌ |
| Zack Gelof | H+R+RBI | Over | 1.5 | +108 | 53% | 1 | — | ❌ |
| Andrew Benintendi | Hits | Under | 0.5 | +123 | 47% | 1 | — | ❌ |
| Brooks Lee | RBI | Over | 0.5 | +218 | 34% | 1 | — | ✅ |
| Freddie Freeman | RBI | Under | 0.5 | -197 | 72% | 0 | — | ✅ |
| Ben Rice | RBI | Over | 0.5 | +207 | 36% | 2 | — | ✅ |
| Esmerlyn Valdez | H+R+RBI | Over | 0.5 | -159 | 67% | 0 | — | ❌ |
| TJ Rumfield | H+R+RBI | Under | 1.5 | +102 | 54% | 0 | — | ✅ |
| JJ Wetherholt | Hits | Over | 0.5 | -164 | 66% | 1 | — | ✅ |
| Alex Bregman | Hits | Over | 0.5 | -187 | 69% | 0 | — | ❌ |
| Spencer Jones | H+R+RBI | Under | 1.5 | -164 | 68% | 5 | — | ❌ |
| Sal Stewart | Hits | Over | 0.5 | -246 | 75% | 2 | — | ✅ |
| Brandon Lowe | Hits | Over | 0.5 | -111 | 55% | 1 | — | ✅ |
| Cole Young | H+R+RBI | Over | 0.5 | -169 | 68% | 0 | — | ❌ |
| Brayan Rocchio | H+R+RBI | Under | 1.5 | +113 | 51% | 2 | — | ❌ |
| Ceddanne Rafaela | Hits | Under | 1.5 | -248 | 75% | 3 | — | ❌ |
| Adley Rutschman | Hits | Under | 0.5 | +166 | 40% | 0 | — | ✅ |
| Jared Young | H+R+RBI | Under | 1.5 | -158 | 66% | 2 | — | ❌ |
| Jackson Holliday | H+R+RBI | Under | 1.5 | -125 | 60% | 0 | — | ✅ |
| Janson Junk | Ks (P) | Under | 3.5 | -148 | 62% | 2 | — | ✅ |
| Mauricio Dubon | Hits | Over | 0.5 | -181 | 68% | 1 | -4.2% | ✅ |
| Keibert Ruiz | H+R+RBI | Over | 1.5 | +120 | 49% | 2 | — | ✅ |
| Ronald Acuna Jr. | RBI | Over | 0.5 | +248 | 31% | 0 | +4.5% | ❌ |
| Liam Hicks | H+R+RBI | Over | 1.5 | -108 | 56% | 1 | — | ❌ |
| Dylan Crews | H+R+RBI | Under | 1.5 | -123 | 59% | 3 | — | ❌ |
| Caleb Durbin | H+R+RBI | Under | 1.5 | -107 | 56% | 0 | — | ✅ |
| Jose Trevino | H+R+RBI | Under | 1.5 | -158 | 66% | 0 | — | ✅ |
| Brandon Marsh | H+R+RBI | Over | 1.5 | +103 | 53% | 0 | — | ❌ |
| Cal Raleigh | Hits | Under | 0.5 | -102 | 53% | 1 | — | ❌ |
| Max Muncy | RBI | Under | 0.5 | -195 | 71% | 1 | — | ❌ |
| Eugenio Suarez | H+R+RBI | Under | 1.5 | -134 | 62% | 3 | — | ❌ |
| Manny Machado | H+R+RBI | Under | 1.5 | +101 | 53% | 1 | — | ✅ |
| Cam Smith | Hits | Under | 0.5 | +146 | 42% | 0 | — | ✅ |
| Shohei Ohtani | Hits | Under | 1.5 | -247 | 74% | 0 | — | ✅ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | +134 | 46% | 0 | — | ❌ |
| Dylan Beavers | Hits | Over | 0.5 | -140 | 61% | 0 | — | ❌ |
| Samuel Basallo | Hits | Under | 0.5 | +148 | 42% | 0 | — | ✅ |
| Andruw Monasterio | Hits | Under | 0.5 | +130 | 45% | 1 | — | ❌ |
| Brooks Lee | H+R+RBI | Over | 1.5 | +115 | 50% | 3 | — | ✅ |
| Shohei Ohtani | RBI | Under | 0.5 | -163 | 66% | 0 | — | ✅ |
| Jackson Chourio | Hits | Over | 0.5 | -226 | 72% | 2 | +4.6% | ✅ |
| Munetaka Murakami | Hits | Over | 0.5 | -151 | 63% | 0 | — | ❌ |
| Dylan Beavers | H+R+RBI | Over | 0.5 | -169 | 67% | 0 | — | ❌ |
| Matt Olson | Hits | Over | 0.5 | -192 | 68% | 0 | +3.6% | ❌ |
| Gavin Sheets | H+R+RBI | Under | 1.5 | -146 | 63% | 0 | — | ✅ |
| Wilyer Abreu | Hits | Over | 0.5 | -239 | 73% | 0 | — | ❌ |
| Spencer Torkelson | H+R+RBI | Under | 1.5 | -135 | 61% | 1 | — | ✅ |
| Matt Olson | H+R+RBI | Over | 1.5 | +102 | 53% | 0 | +7.2% | ❌ |
| Alex Bregman | H+R+RBI | Over | 1.5 | +105 | 52% | 4 | — | ✅ |
| Javier Baez | H+R+RBI | Under | 1.5 | -150 | 64% | 2 | — | ❌ |
| Josh Naylor | H+R+RBI | Over | 1.5 | +125 | 47% | 2 | — | ✅ |
| Vladimir Guerrero Jr. | H+R+RBI | Under | 1.5 | -113 | 56% | 0 | — | ✅ |
| Heriberto Hernandez | H+R+RBI | Under | 1.5 | +102 | 52% | 2 | — | ❌ |
| Christian Vazquez | H+R+RBI | Over | 0.5 | -166 | 66% | 0 | — | ❌ |
| Byron Buxton | RBI | Under | 0.5 | -184 | 69% | 0 | — | ✅ |
| Geraldo Perdomo | RBI | Under | 0.5 | -224 | 73% | 0 | — | ✅ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +137 | 45% | 0 | — | ❌ |
| Gabriel Moreno | RBI | Over | 0.5 | +170 | 39% | 1 | — | ✅ |
| Nathaniel Lowe | RBI | Under | 0.5 | -161 | 65% | 1 | — | ❌ |
| Michael Busch | Hits | Over | 0.5 | -173 | 66% | 1 | — | ✅ |
| Carlos Cortes | Hits | Over | 0.5 | -164 | 64% | 1 | — | ✅ |
| Alec Burleson | Hits | Over | 0.5 | -177 | 66% | 0 | — | ❌ |
| David Hamilton | H+R+RBI | Over | 0.5 | -153 | 64% | 0 | -5.0% | ❌ |
| Jake Burger | RBI | Over | 0.5 | +182 | 37% | 0 | — | ❌ |
| Manny Machado | Hits | Under | 0.5 | +175 | 38% | 1 | — | ❌ |
| Cal Raleigh | H+R+RBI | Under | 1.5 | -169 | 66% | 1 | — | ✅ |
| Max Muncy | H+R+RBI | Under | 1.5 | -118 | 57% | 3 | — | ❌ |
| J.T. Realmuto | RBI | Over | 0.5 | +227 | 32% | 0 | — | ❌ |
| Matt Olson | RBI | Over | 0.5 | +200 | 35% | 0 | +11.5% | ❌ |
| Xander Bogaerts | H+R+RBI | Under | 1.5 | -135 | 60% | 3 | — | ❌ |
| Geraldo Perdomo | Hits | Over | 0.5 | -212 | 70% | 1 | — | ✅ |
| Chase DeLauter | RBI | Under | 0.5 | -153 | 64% | 2 | — | ❌ |
| Yordan Alvarez | RBI | Over | 0.5 | +138 | 44% | 0 | — | ❌ |
| Daulton Varsho | RBI | Under | 0.5 | -246 | 75% | 0 | — | ✅ |
| Zach Neto | RBI | Over | 0.5 | +217 | 33% | 1 | — | ✅ |
| Josh Bell | Hits | Over | 0.5 | -202 | 69% | 0 | — | ❌ |
| Luis Garcia Jr. | Hits | Under | 0.5 | +169 | 38% | 0 | — | ✅ |
| Luis Arraez | H+R+RBI | Over | 1.5 | -136 | 60% | 0 | — | ❌ |
| Jake McCarthy | H+R+RBI | Under | 1.5 | +127 | 46% | 1 | — | ✅ |
| Seiya Suzuki | Hits | Over | 0.5 | -179 | 66% | 2 | — | ✅ |
| Foster Griffin | Ks (P) | Over | 4.5 | -147 | 60% | 4 | — | ❌ |
| Andrew Abbott | Ks (P) | Over | 3.5 | +126 | 45% | 6 | — | ✅ |
| Kody Clemens | Hits | Over | 0.5 | -190 | 67% | 0 | — | ❌ |
| Bryce Harper | H+R+RBI | Over | 1.5 | -123 | 57% | 0 | — | ❌ |
| Spencer Torkelson | Hits | Under | 0.5 | +122 | 46% | 0 | — | ✅ |
| Zack Gelof | RBI | Over | 0.5 | +215 | 33% | 0 | — | ❌ |
| Isaac Paredes | H+R+RBI | Over | 1.5 | -128 | 58% | 5 | — | ✅ |
| Kyle Tucker | RBI | Under | 0.5 | -245 | 74% | 0 | — | ✅ |
| Jazz Chisholm Jr. | Hits | Under | 0.5 | +109 | 49% | 2 | — | ❌ |
| Pete Alonso | H+R+RBI | Over | 1.5 | -128 | 58% | 0 | — | ❌ |
| Liam Hicks | Hits | Over | 0.5 | -211 | 69% | 1 | — | ✅ |
| Tristan Peters | Hits | Over | 0.5 | -129 | 58% | 2 | — | ✅ |
| Michael Harris II | RBI | Over | 0.5 | +222 | 32% | 1 | +9.2% | ✅ |
| Yandy Diaz | H+R+RBI | Over | 1.5 | -145 | 61% | 0 | — | ❌ |
| Drake Baldwin | H+R+RBI | Over | 1.5 | +107 | 50% | 2 | +1.5% | ✅ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | +104 | 51% | 5 | — | ✅ |
| Jake McCarthy | RBI | Over | 0.5 | +204 | 34% | 0 | — | ❌ |
| Jose Altuve | RBI | Under | 0.5 | -197 | 69% | 3 | — | ❌ |
| Keibert Ruiz | RBI | Over | 0.5 | +221 | 32% | 0 | — | ❌ |
| Andrew Benintendi | H+R+RBI | Under | 1.5 | -151 | 62% | 2 | — | ❌ |
| TJ Rumfield | RBI | Under | 0.5 | -203 | 69% | 0 | — | ✅ |
| Luis Garcia Jr. | RBI | Over | 0.5 | +201 | 34% | 0 | — | ❌ |
| Keibert Ruiz | Hits | Over | 0.5 | -192 | 67% | 1 | — | ✅ |
| William Contreras | Hits | Over | 0.5 | -218 | 70% | 2 | +2.5% | ✅ |
| Brett Baty | H+R+RBI | Under | 0.5 | +126 | 46% | 0 | — | ✅ |
| Braden Montgomery | RBI | Over | 0.5 | +234 | 31% | 0 | — | ❌ |
| Ronald Acuna Jr. | Hits | Under | 0.5 | +141 | 42% | 1 | -17.5% | ❌ |
| Luke Keaschall | H+R+RBI | Under | 1.5 | -115 | 55% | 1 | — | ✅ |
| Coby Mayo | H+R+RBI | Over | 0.5 | -165 | 64% | 0 | — | ❌ |
| Griffin Conine | H+R+RBI | Under | 1.5 | -112 | 54% | 2 | — | ❌ |
| Fernando Tatis Jr. | RBI | Under | 0.5 | -175 | 65% | 4 | — | ❌ |
| George Springer | RBI | Under | 0.5 | -246 | 73% | 0 | — | ✅ |
| George Springer | Hits | Under | 0.5 | +144 | 42% | 1 | — | ❌ |
| Elias Diaz | Hits | Over | 0.5 | -137 | 59% | 1 | — | ✅ |
| Bryson Stott | RBI | Over | 0.5 | +204 | 34% | 0 | — | ❌ |
| Taylor Trammell | H+R+RBI | Under | 1.5 | -179 | 66% | 1 | — | ✅ |
| Christian Walker | RBI | Over | 0.5 | +159 | 40% | 0 | — | ❌ |
| Marcus Semien | H+R+RBI | Under | 1.5 | -156 | 62% | 0 | — | ✅ |
| Lane Thomas | Hits | Over | 0.5 | -142 | 60% | 2 | +2.2% | ✅ |
| Willson Contreras | RBI | Under | 0.5 | -174 | 65% | 0 | — | ✅ |
| Sam Antonacci | Hits | Under | 0.5 | +135 | 43% | 1 | — | ❌ |
| Ezequiel Duran | Hits | Over | 0.5 | -189 | 66% | 1 | — | ✅ |
| Otto Lopez | H+R+RBI | Over | 1.5 | -165 | 64% | 2 | — | ✅ |
| Geraldo Perdomo | H+R+RBI | Under | 1.5 | -111 | 54% | 1 | — | ✅ |
| Mauricio Dubon | H+R+RBI | Over | 1.5 | +125 | 45% | 3 | -1.8% | ✅ |
| Pete Alonso | RBI | Over | 0.5 | +156 | 40% | 0 | — | ❌ |
| Nick Gonzales | Hits | Over | 0.5 | -177 | 65% | 0 | — | ❌ |
| Ezequiel Duran | H+R+RBI | Over | 1.5 | +100 | 51% | 3 | — | ✅ |
| Sal Stewart | H+R+RBI | Over | 1.5 | -130 | 58% | 4 | — | ✅ |
| Austin Riley | RBI | Over | 0.5 | +245 | 30% | 0 | +2.4% | ❌ |
| Ezequiel Duran | RBI | Over | 0.5 | +209 | 33% | 1 | — | ✅ |
| Randy Arozarena | H+R+RBI | Over | 1.5 | +101 | 51% | 3 | — | ✅ |
| Luis Rengifo | Hits | Over | 0.5 | -200 | 68% | 1 | — | ✅ |
| Marcus Semien | Hits | Over | 0.5 | -161 | 62% | 0 | — | ❌ |
| Dominic Canzone | H+R+RBI | Under | 1.5 | -164 | 63% | 1 | — | ✅ |
| Corey Seager | H+R+RBI | Under | 1.5 | +104 | 50% | 3 | — | ❌ |
| Michael Harris II | H+R+RBI | Over | 1.5 | +105 | 50% | 3 | +14.3% | ✅ |
| Isaac Paredes | RBI | Over | 0.5 | +159 | 39% | 3 | — | ✅ |
| Byron Buxton | H+R+RBI | Under | 1.5 | +105 | 50% | 1 | — | ✅ |
| Brandon Nimmo | RBI | Under | 0.5 | -224 | 70% | 1 | — | ❌ |
| Carson Benge | Hits | Over | 0.5 | -191 | 66% | 2 | — | ✅ |
| Kevin McGonigle | H+R+RBI | Under | 1.5 | -119 | 55% | 6 | — | ❌ |
| JJ Bleday | RBI | Over | 0.5 | +221 | 32% | 0 | — | ❌ |
| Jackson Chourio | H+R+RBI | Over | 1.5 | -118 | 55% | 2 | +5.5% | ✅ |
| Kevin McGonigle | Hits | Under | 0.5 | +160 | 39% | 2 | — | ❌ |
| Junior Caminero | H+R+RBI | Under | 2.5 | -153 | 61% | 3 | — | ❌ |
| Mickey Moniak | H+R+RBI | Under | 1.5 | -120 | 55% | 0 | — | ✅ |
| Manny Machado | RBI | Under | 0.5 | -186 | 66% | 0 | — | ✅ |
| Jonathan Aranda | RBI | Over | 0.5 | +171 | 37% | 0 | — | ❌ |
| Fernando Tatis Jr. | Hits | Under | 1.5 | -197 | 67% | 4 | — | ❌ |
| Bo Bichette | H+R+RBI | Under | 1.5 | -111 | 53% | 0 | — | ✅ |
| Jackson Merrill | H+R+RBI | Under | 1.5 | -101 | 51% | 3 | — | ❌ |
| Travis Bazzana | RBI | Under | 0.5 | -194 | 67% | 0 | — | ✅ |
| Willi Castro | H+R+RBI | Under | 1.5 | +104 | 50% | 1 | — | ✅ |
| Mickey Moniak | RBI | Over | 0.5 | +167 | 38% | 0 | — | ❌ |
| Carson Kelly | Hits | Under | 0.5 | +108 | 48% | 1 | — | ❌ |
| Joey Ortiz | H+R+RBI | Under | 1.5 | -152 | 61% | 0 | +0.8% | ✅ |
| Trent Grisham | H+R+RBI | Under | 1.5 | -134 | 58% | 0 | — | ✅ |
| Alejandro Kirk | H+R+RBI | Under | 1.5 | -126 | 56% | 2 | — | ❌ |
| Richie Palacios | Hits | Over | 0.5 | -157 | 61% | 0 | — | ❌ |
| Yandy Diaz | RBI | Over | 0.5 | +167 | 38% | 0 | — | ❌ |
| Julio Rodriguez | H+R+RBI | Under | 1.5 | -128 | 57% | 0 | — | ✅ |
| Jonathan Aranda | H+R+RBI | Over | 1.5 | -123 | 56% | 0 | — | ❌ |
| Pete Crow-Armstrong | Hits | Over | 0.5 | -220 | 69% | 2 | — | ✅ |
| Esmerlyn Valdez | Hits | Over | 0.5 | -116 | 54% | 0 | — | ❌ |
| Christian Walker | H+R+RBI | Over | 1.5 | -119 | 55% | 1 | — | ❌ |
| Mike Trout | H+R+RBI | Under | 1.5 | -121 | 55% | 1 | — | ✅ |
| Cam Smith | H+R+RBI | Under | 1.5 | -116 | 54% | 1 | — | ✅ |
| Lawrence Butler | H+R+RBI | Under | 1.5 | -140 | 58% | 3 | — | ❌ |
| Elly De La Cruz | H+R+RBI | Over | 1.5 | -139 | 58% | 2 | — | ✅ |
| Jose Caballero | H+R+RBI | Over | 0.5 | -163 | 62% | 0 | — | ❌ |
| Griffin Conine | RBI | Under | 0.5 | -201 | 67% | 0 | — | ✅ |
| Jake Cronenworth | Hits | Under | 0.5 | +124 | 45% | 1 | — | ❌ |
| Heriberto Hernandez | RBI | Over | 0.5 | +181 | 36% | 1 | — | ✅ |
| Sam Antonacci | H+R+RBI | Under | 1.5 | -139 | 58% | 1 | — | ✅ |
| Royce Lewis | RBI | Under | 0.5 | -222 | 69% | 0 | — | ✅ |
| Samuel Basallo | H+R+RBI | Under | 1.5 | -128 | 56% | 0 | — | ✅ |
| Royce Lewis | H+R+RBI | Under | 1.5 | -119 | 54% | 0 | — | ✅ |
| Trea Turner | H+R+RBI | Over | 1.5 | -132 | 57% | 0 | — | ❌ |
| Willi Castro | RBI | Under | 0.5 | -215 | 68% | 0 | — | ✅ |
| Ernie Clement | H+R+RBI | Under | 1.5 | -150 | 60% | 0 | — | ✅ |
| Shota Imanaga | Ks (P) | Over | 5.5 | -121 | 55% | 4 | — | ❌ |
| Bryce Harper | RBI | Over | 0.5 | +168 | 37% | 0 | — | ❌ |
| Ozzie Albies | H+R+RBI | Over | 1.5 | +101 | 50% | 3 | +3.9% | ✅ |
| Ronald Acuna Jr. | H+R+RBI | Under | 1.5 | -131 | 56% | 1 | -13.6% | ✅ |
| Ty France | H+R+RBI | Under | 1.5 | -114 | 53% | 0 | — | ✅ |
| Nico Hoerner | Hits | Over | 0.5 | -211 | 68% | 1 | — | ✅ |
| Travis Bazzana | H+R+RBI | Under | 1.5 | +116 | 46% | 0 | — | ✅ |
| Jo Adell | RBI | Under | 0.5 | -129 | 56% | 2 | — | ❌ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -143 | 59% | 1 | — | ✅ |
| Kyle Schwarber | Hits | Over | 0.5 | -218 | 68% | 0 | — | ❌ |
| Carlos Cortes | H+R+RBI | Under | 1.5 | -153 | 60% | 1 | — | ✅ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +174 | 36% | 3 | — | ✅ |
| Xavier Edwards | H+R+RBI | Under | 1.5 | +102 | 49% | 3 | — | ❌ |
| Bryson Stott | H+R+RBI | Over | 1.5 | -101 | 50% | 0 | — | ❌ |
| Lane Thomas | H+R+RBI | Under | 1.5 | -178 | 64% | 2 | -1.2% | ❌ |
| Royce Lewis | Hits | Over | 0.5 | -198 | 66% | 0 | — | ❌ |
| Daulton Varsho | H+R+RBI | Under | 1.5 | -118 | 54% | 1 | — | ✅ |
| Garrett Mitchell | RBI | Over | 0.5 | +235 | 30% | 0 | -10.9% | ❌ |
| Jacob Young | H+R+RBI | Under | 1.5 | -155 | 60% | 0 | — | ✅ |
| William Contreras | RBI | Over | 0.5 | +190 | 34% | 0 | -1.7% | ❌ |
| Jeremy Pena | H+R+RBI | Under | 2.5 | -169 | 62% | 4 | — | ❌ |
| Rafael Devers | Hits | Under | 0.5 | +137 | 42% | 0 | — | ✅ |
| Cole Carrigg | RBI | Under | 0.5 | -221 | 68% | 0 | — | ✅ |
| Colson Montgomery | RBI | Over | 0.5 | +197 | 33% | 0 | — | ❌ |
| Munetaka Murakami | RBI | Over | 0.5 | +194 | 34% | 0 | — | ❌ |
| Ty France | RBI | Under | 0.5 | -224 | 68% | 0 | — | ✅ |
| Ildemaro Vargas | RBI | Over | 0.5 | +201 | 33% | 2 | — | ✅ |
| Corbin Carroll | H+R+RBI | Over | 1.5 | -127 | 55% | 4 | — | ✅ |
| Xavier Edwards | RBI | Under | 0.5 | -250 | 70% | 2 | — | ❌ |
| Kazuma Okamoto | RBI | Under | 0.5 | -242 | 70% | 0 | — | ✅ |
| Nick Martinez | Ks (P) | Under | 3.5 | +104 | 49% | 4 | — | ❌ |
| Jared Young | Hits | Under | 0.5 | +117 | 46% | 1 | — | ❌ |
| Jackson Merrill | RBI | Under | 0.5 | -202 | 66% | 1 | — | ❌ |
| Elias Diaz | H+R+RBI | Under | 0.5 | +127 | 43% | 4 | — | ❌ |
| Carson Kelly | H+R+RBI | Under | 1.5 | -179 | 63% | 3 | — | ❌ |
| Vaughn Grissom | H+R+RBI | Under | 1.5 | -147 | 58% | 2 | — | ❌ |
| Brayan Rocchio | RBI | Under | 0.5 | -232 | 68% | 1 | — | ❌ |
| Austin Wells | Hits | Over | 0.5 | -104 | 50% | 1 | — | ✅ |
| Zack Gelof | Hits | Over | 0.5 | -174 | 63% | 0 | — | ❌ |
| Drake Baldwin | Hits | Over | 0.5 | -200 | 66% | 1 | -0.7% | ✅ |
| Brandon Nimmo | H+R+RBI | Over | 1.5 | -124 | 54% | 1 | — | ❌ |
| Trent Grisham | RBI | Over | 0.5 | +217 | 31% | 0 | — | ❌ |
| Bryce Eldridge | H+R+RBI | Over | 1.5 | +116 | 45% | 3 | — | ✅ |
| Jose Trevino | Hits | Under | 0.5 | +126 | 44% | 0 | — | ✅ |
| Yordan Alvarez | H+R+RBI | Under | 2.5 | -148 | 58% | 2 | — | ✅ |
| Carson Benge | H+R+RBI | Under | 1.5 | -131 | 55% | 3 | — | ❌ |
| Kazuma Okamoto | H+R+RBI | Under | 1.5 | -139 | 57% | 1 | — | ✅ |
| Kazuma Okamoto | Hits | Over | 0.5 | -167 | 62% | 1 | — | ✅ |
| Daulton Varsho | Hits | Over | 0.5 | -195 | 65% | 1 | — | ✅ |
| Jackson Chourio | RBI | Over | 0.5 | +199 | 33% | 0 | +1.4% | ❌ |
| Josh Bell | RBI | Over | 0.5 | +168 | 36% | 0 | — | ❌ |
| Josh Lowe | H+R+RBI | Under | 0.5 | +120 | 44% | 1 | — | ❌ |
| Daylen Lile | RBI | Over | 0.5 | +182 | 34% | 0 | — | ❌ |
| Carlos Cortes | RBI | Over | 0.5 | +231 | 29% | 0 | — | ❌ |
| Evan Carter | Hits | Under | 0.5 | -123 | 54% | 0 | — | ✅ |
| Tristan Peters | H+R+RBI | Over | 0.5 | -161 | 60% | 4 | — | ✅ |
| Pete Crow-Armstrong | H+R+RBI | Over | 1.5 | -122 | 53% | 7 | — | ✅ |
| Otto Lopez | RBI | Over | 0.5 | +186 | 34% | 1 | — | ✅ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | +104 | 48% | 0 | — | ❌ |
| Jung Hoo Lee | Hits | Over | 0.5 | -245 | 70% | 0 | — | ❌ |
| Wilyer Abreu | RBI | Under | 0.5 | -228 | 68% | 0 | — | ✅ |
| Wilyer Abreu | H+R+RBI | Under | 1.5 | +102 | 48% | 0 | — | ✅ |
| Braden Montgomery | H+R+RBI | Over | 1.5 | +114 | 45% | 0 | — | ❌ |
| Pedro Pages | H+R+RBI | Under | 0.5 | -124 | 54% | 0 | — | ✅ |
| Dominic Canzone | Hits | Under | 0.5 | +106 | 48% | 1 | — | ❌ |
| JJ Bleday | H+R+RBI | Under | 1.5 | -149 | 58% | 0 | — | ✅ |
| Luis Garcia Jr. | H+R+RBI | Under | 1.5 | -119 | 53% | 0 | — | ✅ |
| Colton Cowser | H+R+RBI | Over | 0.5 | -138 | 56% | 4 | — | ✅ |
| Evan Carter | H+R+RBI | Over | 0.5 | -153 | 58% | 0 | — | ❌ |
| J.T. Realmuto | H+R+RBI | Over | 1.5 | +116 | 45% | 0 | — | ❌ |
| Ian Happ | H+R+RBI | Over | 1.5 | +122 | 44% | 9 | — | ✅ |
| Justin Crawford | H+R+RBI | Over | 1.5 | +131 | 42% | 1 | — | ❌ |
| Henry Bolte | Hits | Over | 0.5 | -211 | 66% | 3 | — | ✅ |
| Corey Seager | RBI | Under | 0.5 | -241 | 68% | 0 | — | ✅ |
| Josh Lowe | Hits | Under | 0.5 | -105 | 50% | 0 | — | ✅ |
| Michael Busch | RBI | Over | 0.5 | +214 | 31% | 0 | — | ❌ |
| Taylor Trammell | Hits | Over | 0.5 | -121 | 53% | 1 | — | ✅ |
| Kyle Schwarber | H+R+RBI | Under | 1.5 | +110 | 46% | 0 | — | ✅ |
| Brandon Marsh | RBI | Over | 0.5 | +207 | 31% | 0 | — | ❌ |
| Denzer Guzman | H+R+RBI | Under | 1.5 | -177 | 61% | 0 | — | ✅ |
| Corey Seager | Hits | Over | 0.5 | -248 | 70% | 2 | — | ✅ |
| William Contreras | H+R+RBI | Over | 1.5 | -114 | 51% | 2 | +2.0% | ✅ |
| Luis Rengifo | H+R+RBI | Over | 1.5 | +103 | 47% | 3 | — | ✅ |
| Richie Palacios | RBI | Over | 0.5 | +235 | 29% | 0 | — | ❌ |
| Miguel Vargas | H+R+RBI | Under | 1.5 | -119 | 52% | 2 | — | ❌ |
| Josh Bell | H+R+RBI | Over | 1.5 | -111 | 50% | 0 | — | ❌ |
| Jose Altuve | H+R+RBI | Under | 1.5 | +111 | 45% | 5 | — | ❌ |
| Nolan Arenado | H+R+RBI | Under | 1.5 | -114 | 51% | 0 | — | ✅ |
| Ben Rice | H+R+RBI | Over | 1.5 | -107 | 49% | 4 | — | ✅ |
| Wyatt Langford | H+R+RBI | Under | 1.5 | -112 | 50% | 2 | — | ❌ |
| Bryce Harper | Hits | Over | 0.5 | -230 | 68% | 0 | — | ❌ |
| Ty France | Hits | Over | 0.5 | -210 | 66% | 0 | — | ❌ |
| Henry Bolte | H+R+RBI | Under | 1.5 | -123 | 53% | 4 | — | ❌ |
| TJ Rumfield | Hits | Over | 0.5 | -245 | 69% | 0 | — | ❌ |
| Joey Ortiz | Hits | Over | 0.5 | -183 | 63% | 0 | -1.0% | ❌ |
| Daylen Lile | H+R+RBI | Over | 1.5 | -115 | 51% | 2 | — | ✅ |
| Javier Sanoja | H+R+RBI | Under | 1.5 | -104 | 49% | 1 | — | ✅ |
| Jung Hoo Lee | H+R+RBI | Over | 1.5 | +105 | 46% | 0 | — | ❌ |
| Ben Rice | Hits | Over | 0.5 | -203 | 65% | 2 | — | ✅ |
| Cedric Mullins | H+R+RBI | Under | 1.5 | -155 | 58% | 0 | — | ✅ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +236 | 28% | 0 | — | ❌ |
| Matt McLain | H+R+RBI | Under | 1.5 | -158 | 58% | 0 | — | ✅ |
| Vladimir Guerrero Jr. | Hits | Over | 0.5 | -226 | 67% | 0 | — | ❌ |
| Nick Gonzales | H+R+RBI | Over | 1.5 | +124 | 42% | 0 | — | ❌ |
| Mike Trout | Hits | Under | 0.5 | +157 | 38% | 1 | — | ❌ |
| Ernie Clement | Hits | Over | 0.5 | -198 | 64% | 0 | — | ❌ |
| Kody Clemens | H+R+RBI | Under | 1.5 | -118 | 51% | 0 | — | ✅ |
| Michael Busch | H+R+RBI | Over | 1.5 | +110 | 45% | 4 | — | ✅ |
| Gunnar Henderson | H+R+RBI | Over | 1.5 | -106 | 49% | 0 | — | ❌ |
| Nico Hoerner | H+R+RBI | Over | 1.5 | +104 | 46% | 1 | — | ❌ |
| Willy Adames | Hits | Over | 0.5 | -177 | 62% | 1 | — | ✅ |
| Zach Neto | H+R+RBI | Over | 1.5 | -107 | 49% | 4 | — | ✅ |
| Luis Arraez | RBI | Over | 0.5 | +178 | 34% | 0 | — | ❌ |
| Gavin Sheets | Hits | Under | 0.5 | +110 | 46% | 0 | — | ✅ |
| Miguel Vargas | RBI | Over | 0.5 | +187 | 33% | 0 | — | ❌ |
| Jazz Chisholm Jr. | RBI | Over | 0.5 | +249 | 27% | 2 | — | ✅ |
| Denzer Guzman | Hits | Under | 0.5 | +117 | 44% | 0 | — | ✅ |
| Leody Taveras | H+R+RBI | Over | 1.5 | +128 | 41% | 0 | — | ❌ |
| Gabriel Moreno | H+R+RBI | Under | 1.5 | +107 | 45% | 1 | — | ✅ |
| Jose Caballero | Hits | Over | 0.5 | -116 | 52% | 0 | — | ❌ |
| Rafael Devers | H+R+RBI | Over | 1.5 | +108 | 45% | 1 | — | ❌ |
| Nolan Arenado | RBI | Over | 0.5 | +164 | 36% | 0 | — | ❌ |
| Kody Clemens | RBI | Over | 0.5 | +165 | 35% | 0 | — | ❌ |
| Colson Montgomery | H+R+RBI | Over | 1.5 | +126 | 42% | 0 | — | ❌ |
| Willy Adames | H+R+RBI | Over | 1.5 | +110 | 45% | 2 | — | ✅ |
| Bryce Eldridge | RBI | Over | 0.5 | +229 | 28% | 1 | — | ✅ |
| Austin Wells | H+R+RBI | Under | 0.5 | +103 | 46% | 2 | — | ❌ |
| Julio Rodriguez | Hits | Under | 0.5 | +150 | 38% | 0 | — | ✅ |
| Joey Ortiz | RBI | Over | 0.5 | +248 | 27% | 0 | +1.5% | ❌ |
| Elly De La Cruz | RBI | Over | 0.5 | +180 | 33% | 0 | — | ❌ |
| Lawrence Butler | Hits | Over | 0.5 | -175 | 61% | 1 | — | ✅ |
| Javier Baez | Hits | Over | 0.5 | -171 | 60% | 1 | — | ✅ |
| Jacob Young | RBI | Over | 0.5 | +243 | 27% | 0 | — | ❌ |
| Josh Naylor | RBI | Over | 0.5 | +249 | 26% | 0 | — | ❌ |
| Walker Buehler | Ks (P) | Under | 3.5 | +111 | 46% | 4 | — | ❌ |
| Samuel Basallo | RBI | Over | 0.5 | +177 | 33% | 0 | — | ❌ |
| Ozzie Albies | RBI | Over | 0.5 | +203 | 30% | 0 | +7.5% | ❌ |
| Cedric Mullins | Hits | Under | 0.5 | +110 | 45% | 0 | — | ✅ |
| Yordan Alvarez | Hits | Over | 1.5 | +176 | 34% | 1 | — | ❌ |
| J.T. Realmuto | Hits | Under | 0.5 | +117 | 44% | 0 | — | ✅ |
| Miguel Vargas | Hits | Under | 0.5 | +156 | 37% | 1 | — | ❌ |
| Justin Foscue | Hits | Over | 0.5 | -150 | 57% | 0 | — | ❌ |
| Colson Montgomery | Hits | Over | 0.5 | -139 | 55% | 0 | — | ❌ |
| Richie Palacios | H+R+RBI | Over | 1.5 | +121 | 42% | 0 | — | ❌ |
| Tyler Mahle | Ks (P) | Over | 5.5 | +121 | 44% | 4 | -3.5% | ❌ |
| Bo Bichette | Hits | Under | 0.5 | +187 | 33% | 0 | — | ✅ |
| Jazz Chisholm Jr. | H+R+RBI | Over | 1.5 | +128 | 40% | 6 | — | ✅ |
| Alejandro Kirk | Hits | Under | 0.5 | +152 | 38% | 1 | — | ❌ |
| Esteury Ruiz | Hits | Over | 0.5 | -144 | 56% | 0 | — | ❌ |
| Bryson Stott | Hits | Under | 0.5 | +147 | 38% | 0 | — | ✅ |
| Junior Caminero | RBI | Over | 0.5 | +127 | 40% | 1 | — | ✅ |
| Max Muncy | Hits | Under | 0.5 | +131 | 41% | 1 | — | ❌ |
| Kyle Schwarber | RBI | Over | 0.5 | +130 | 40% | 0 | — | ❌ |
| Matt McLain | Hits | Under | 0.5 | +117 | 44% | 0 | — | ✅ |
| JJ Bleday | Hits | Under | 0.5 | +125 | 42% | 0 | — | ✅ |
| Henry Bolte | RBI | Over | 0.5 | +240 | 27% | 0 | — | ❌ |
| Trea Turner | RBI | Over | 0.5 | +192 | 31% | 0 | — | ❌ |
| Griffin Conine | Hits | Under | 0.5 | +160 | 36% | 1 | — | ❌ |
| Alejandro Kirk | RBI | Over | 0.5 | +199 | 30% | 1 | — | ✅ |
| Coby Mayo | RBI | Over | 0.5 | +206 | 29% | 0 | — | ❌ |
| Cam Smith | RBI | Over | 0.5 | +179 | 32% | 0 | — | ❌ |
| Bo Bichette | RBI | Over | 0.5 | +199 | 30% | 0 | — | ❌ |
| Randy Arozarena | RBI | Over | 0.5 | +200 | 30% | 1 | — | ✅ |
| Luis Rengifo | RBI | Over | 0.5 | +228 | 27% | 2 | — | ✅ |
| Jackson Merrill | Hits | Under | 0.5 | +170 | 35% | 1 | — | ❌ |
| Javier Sanoja | RBI | Over | 0.5 | +165 | 34% | 0 | — | ❌ |
| Cal Raleigh | RBI | Over | 0.5 | +190 | 31% | 0 | — | ❌ |
| Matt McLain | RBI | Over | 0.5 | +237 | 27% | 0 | — | ❌ |
| Zach Neto | Hits | Under | 0.5 | +152 | 37% | 2 | — | ❌ |
| Eugenio Suarez | RBI | Over | 0.5 | +171 | 33% | 2 | — | ✅ |
| Gleyber Torres | RBI | Over | 0.5 | +213 | 28% | 1 | — | ✅ |
| Adley Rutschman | RBI | Over | 0.5 | +169 | 33% | 0 | — | ❌ |
| Carlos Rodon | Ks (P) | Under | 5.5 | -148 | 57% | 1 | — | ✅ |
| Junior Caminero | Hits | Over | 1.5 | +184 | 33% | 1 | — | ❌ |
| Shane Baz | Ks (P) | Under | 4.5 | -138 | 55% | 0 | — | ✅ |
| Luke Keaschall | Hits | Under | 0.5 | +147 | 37% | 1 | — | ❌ |
| Andrew Benintendi | RBI | Over | 0.5 | +188 | 30% | 1 | — | ✅ |
| Lawrence Butler | RBI | Over | 0.5 | +224 | 27% | 1 | — | ✅ |
| Leody Taveras | Hits | Under | 0.5 | +121 | 42% | 0 | — | ✅ |
| Willy Adames | RBI | Over | 0.5 | +194 | 30% | 0 | — | ❌ |
| Dominic Canzone | RBI | Over | 0.5 | +211 | 28% | 0 | — | ❌ |
| Gunnar Henderson | RBI | Over | 0.5 | +202 | 29% | 0 | — | ❌ |
| Gunnar Henderson | Hits | Under | 0.5 | +159 | 35% | 0 | — | ✅ |
| Luke Keaschall | RBI | Over | 0.5 | +244 | 25% | 0 | — | ❌ |
| Byron Buxton | Hits | Under | 0.5 | +170 | 34% | 1 | — | ❌ |
| Jake McCarthy | Hits | Over | 1.5 | +154 | 36% | 1 | — | ❌ |
| Wyatt Langford | Hits | Under | 0.5 | +163 | 34% | 2 | — | ❌ |
| Daylen Lile | Hits | Under | 0.5 | +203 | 30% | 1 | — | ❌ |
| Brice Turang | RBI | Over | 0.5 | +271 | 37% | 0 | +0.5% | ❌ |
| Oneil Cruz | RBI | Over | 0.5 | +259 | 37% | 0 | — | ❌ |
| JJ Wetherholt | RBI | Over | 0.5 | +349 | 29% | 0 | — | ❌ |
| Ivan Herrera | RBI | Over | 0.5 | +292 | 30% | 0 | — | ❌ |
| Mauricio Dubon | RBI | Over | 0.5 | +292 | 30% | 1 | +4.5% | ✅ |
| Christian Yelich | RBI | Over | 0.5 | +256 | 32% | 0 | +6.9% | ❌ |
| Eli White | RBI | Under | 0.5 | -307 | 85% | 0 | — | ✅ |
| Esteury Ruiz | RBI | Under | 0.5 | -320 | 85% | 0 | — | ✅ |
| Jose Caballero | RBI | Over | 0.5 | +314 | 27% | 0 | — | ❌ |
| Cole Young | RBI | Over | 0.5 | +307 | 27% | 0 | — | ❌ |
| Dylan Beavers | RBI | Over | 0.5 | +274 | 30% | 0 | — | ❌ |
| Dane Myers | RBI | Under | 0.5 | -299 | 82% | 0 | — | ✅ |
| Hunter Feduccia | RBI | Under | 0.5 | -396 | 87% | 1 | — | ❌ |
| Chase Meidroth | RBI | Over | 0.5 | +302 | 27% | 0 | — | ❌ |
| Hao-Yu Lee | RBI | Under | 0.5 | -280 | 80% | 1 | — | ❌ |
| Elly De La Cruz | Hits | Over | 0.5 | -262 | 78% | 1 | — | ✅ |
| Javier Sanoja | Hits | Over | 0.5 | -261 | 77% | 1 | — | ✅ |
| Tommy Edman | RBI | Under | 0.5 | -257 | 76% | 0 | — | ✅ |
| Weston Wilson | RBI | Under | 0.5 | -402 | 85% | 0 | — | ✅ |
| Myles Straw | RBI | Under | 0.5 | -509 | 88% | 0 | — | ✅ |
| Teoscar Hernandez | RBI | Under | 0.5 | -252 | 76% | 0 | — | ✅ |
| Nico Hoerner | RBI | Over | 0.5 | +258 | 30% | 0 | — | ❌ |
| Jose Altuve | Hits | Over | 0.5 | -257 | 76% | 1 | — | ✅ |
| Xavier Edwards | Hits | Over | 0.5 | -252 | 75% | 1 | — | ✅ |
| Nick Gonzales | RBI | Over | 0.5 | +306 | 26% | 0 | — | ❌ |
| Moises Ballesteros | RBI | Under | 0.5 | -309 | 78% | 0 | — | ✅ |
| Austin Wells | RBI | Under | 0.5 | -389 | 82% | 1 | — | ❌ |
| Brayan Rocchio | Hits | Over | 0.5 | -271 | 75% | 0 | — | ❌ |
| Vladimir Guerrero Jr. | RBI | Under | 0.5 | -278 | 76% | 0 | — | ✅ |
| Austin Hedges | RBI | Under | 0.5 | -258 | 74% | 0 | — | ✅ |
| Tyrone Taylor | RBI | Under | 0.5 | -348 | 80% | 0 | — | ✅ |
| Gavin Sheets | RBI | Under | 0.5 | -266 | 74% | 0 | — | ✅ |
| Trea Turner | Hits | Over | 0.5 | -257 | 73% | 0 | — | ❌ |
| Elias Diaz | RBI | Under | 0.5 | -347 | 79% | 2 | — | ❌ |
| Josh Lowe | RBI | Under | 0.5 | -367 | 80% | 1 | — | ❌ |
| Ezequiel Tovar | RBI | Under | 0.5 | -300 | 76% | 0 | — | ✅ |
| Gabriel Moreno | Hits | Over | 0.5 | -278 | 74% | 0 | — | ❌ |
| Jung Hoo Lee | RBI | Over | 0.5 | +274 | 27% | 0 | — | ❌ |
| A.J. Ewing | RBI | Under | 0.5 | -367 | 79% | 0 | — | ✅ |
| Jared Young | RBI | Under | 0.5 | -334 | 78% | 1 | — | ❌ |
| Jorbit Vivas | RBI | Under | 0.5 | -389 | 80% | 1 | — | ❌ |
| Willi Castro | Hits | Over | 0.5 | -260 | 72% | 1 | — | ✅ |
| Xander Bogaerts | RBI | Under | 0.5 | -271 | 73% | 1 | — | ❌ |
| Spencer Torkelson | RBI | Under | 0.5 | -270 | 73% | 0 | — | ✅ |
| Justin Foscue | RBI | Under | 0.5 | -343 | 77% | 0 | — | ✅ |
| Dylan Crews | RBI | Under | 0.5 | -268 | 73% | 1 | — | ❌ |
| Luis Robert Jr. | RBI | Under | 0.5 | -268 | 72% | 0 | — | ✅ |
| Spencer Jones | RBI | Under | 0.5 | -314 | 76% | 1 | — | ❌ |
| Javier Baez | RBI | Under | 0.5 | -358 | 78% | 0 | — | ✅ |
| Leody Taveras | RBI | Over | 0.5 | +274 | 27% | 0 | — | ❌ |
| Mike Trout | RBI | Under | 0.5 | -262 | 72% | 0 | — | ✅ |
| Ernie Clement | RBI | Under | 0.5 | -352 | 77% | 0 | — | ✅ |
| Bryan Reynolds | RBI | Over | 0.5 | +264 | 27% | 0 | — | ❌ |
| Julio Rodriguez | RBI | Under | 0.5 | -262 | 72% | 0 | — | ✅ |
| Andruw Monasterio | RBI | Under | 0.5 | -286 | 73% | 0 | — | ✅ |
| Christian Vazquez | RBI | Over | 0.5 | +273 | 26% | 0 | — | ❌ |
| Tim Tawa | RBI | Under | 0.5 | -281 | 73% | 0 | — | ✅ |
| Francisco Lindor | RBI | Under | 0.5 | -276 | 72% | 0 | — | ✅ |
| Mookie Betts | RBI | Under | 0.5 | -262 | 71% | 0 | — | ✅ |
| Freddie Freeman | Hits | Under | 1.5 | -257 | 71% | 2 | — | ❌ |
| Carson Benge | RBI | Under | 0.5 | -285 | 73% | 0 | — | ✅ |
| Denzer Guzman | RBI | Over | 0.5 | +270 | 26% | 0 | — | ❌ |
| Pedro Pages | RBI | Under | 0.5 | -650 | 85% | 0 | — | ✅ |
| Jake Cronenworth | RBI | Under | 0.5 | -335 | 75% | 0 | — | ✅ |
| Cedric Mullins | RBI | Under | 0.5 | -284 | 72% | 0 | — | ✅ |
| Kevin McGonigle | RBI | Under | 0.5 | -279 | 72% | 3 | — | ❌ |
| Colton Cowser | RBI | Under | 0.5 | -405 | 78% | 1 | — | ❌ |
| Taylor Trammell | RBI | Under | 0.5 | -354 | 76% | 0 | — | ✅ |
| Jose Trevino | RBI | Under | 0.5 | -386 | 77% | 0 | — | ✅ |
| Marcus Semien | RBI | Under | 0.5 | -336 | 75% | 0 | — | ✅ |
| Caleb Durbin | RBI | Under | 0.5 | -262 | 70% | 0 | — | ✅ |
| Corbin Carroll | RBI | Under | 0.5 | -257 | 70% | 1 | — | ❌ |
| Ian Happ | RBI | Under | 0.5 | -310 | 73% | 5 | — | ❌ |
| Evan Carter | RBI | Over | 0.5 | +317 | 23% | 0 | — | ❌ |
| Wyatt Langford | RBI | Under | 0.5 | -254 | 69% | 0 | — | ✅ |
| Ceddanne Rafaela | RBI | Under | 0.5 | -266 | 70% | 2 | — | ❌ |
| Sam Antonacci | RBI | Over | 0.5 | +308 | 23% | 0 | — | ❌ |
| Donovan Walton | RBI | Over | 0.5 | +306 | 24% | 0 | — | ❌ |
| Jackson Holliday | RBI | Over | 0.5 | +266 | 26% | 0 | — | ❌ |
| Carson Kelly | RBI | Over | 0.5 | +258 | 26% | 1 | — | ✅ |
| Justin Crawford | RBI | Over | 0.5 | +291 | 24% | 0 | — | ❌ |
| David Hamilton | RBI | Over | 0.5 | +302 | 23% | 0 | -5.4% | ❌ |
| Lane Thomas | RBI | Over | 0.5 | +251 | 25% | 0 | +2.3% | ❌ |
| Brett Baty | RBI | Over | 0.5 | +265 | 23% | 0 | — | ❌ |
| Tristan Peters | RBI | Over | 0.5 | +285 | 22% | 1 | — | ✅ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Tampa Bay Rays @ Baltimore Orioles | **NRFI** | High | 64% | 52% | ✅ |
| St. Louis Cardinals @ Philadelphia Phillies | **YRFI** | High | 63% | 45% | ✅ |
| Toronto Blue Jays @ New York Yankees | **NRFI** | High | 67% | 53% | ✅ |
| Washington Nationals @ Miami Marlins | **NRFI** | High | 68% | 52% | ❌ |
| Los Angeles Angels @ Texas Rangers | **NRFI** | High | 66% | 48% | ✅ |
| Chicago Cubs @ Seattle Mariners | **YRFI** | High | 68% | 48% | ✅ |
| Minnesota Twins @ San Diego Padres | **YRFI** | High | 71% | 52% | ❌ |
| Atlanta Braves @ Milwaukee Brewers | **YRFI** | High | 53% | 45% | ❌ |
| Athletics @ Houston Astros | **NRFI** | Medium | 55% | 47% | ❌ |
| Cleveland Guardians @ Colorado Rockies | **YRFI** | Medium | 63% | 56% | ✅ |
| New York Mets @ Chicago White Sox | **YRFI** | Low | 51% | 47% | ❌ |
| Pittsburgh Pirates @ Los Angeles Dodgers | **YRFI** | Low | 50% | 47% | ✅ |
| Cincinnati Reds @ Arizona Diamondbacks | **NRFI** | Low | 54% | 50% | ✅ |
| Detroit Tigers @ Kansas City Royals | **NRFI** | Coin flip | 50% | 52% | ❌ |
| San Francisco Giants @ Boston Red Sox | **NRFI** | Coin flip | 57% | 55% | ❌ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Max Muncy | Pittsburgh Pirates @ Los Angeles Dodgers | 28% | ❌ |
| 2 | Shohei Ohtani | Pittsburgh Pirates @ Los Angeles Dodgers | 27% | ❌ |
| 3 | Mickey Moniak | Cleveland Guardians @ Colorado Rockies | 25% | ❌ |
| 4 | Munetaka Murakami | New York Mets @ Chicago White Sox | 24% | ❌ |
| 5 | Kyle Schwarber | St. Louis Cardinals @ Philadelphia Phillies | 23% | ❌ |
| 6 | Ben Rice | Toronto Blue Jays @ New York Yankees | 23% | ❌ |
| 7 | Zack Gelof | Athletics @ Houston Astros | 22% | ❌ |
| 8 | Mookie Betts | Pittsburgh Pirates @ Los Angeles Dodgers | 21% | ❌ |
| 9 | Luis García Jr. | Toronto Blue Jays @ New York Yankees | 21% | ❌ |
| 10 | Pete Crow-Armstrong | Chicago Cubs @ Seattle Mariners | 21% | ✅ |

*1 homered · model expected 2.3*

### 2026-08-22 — bets 9-11 (-5.11u) · props 341-331 · NRFI 9-6 · HR 2-8

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Tampa Bay Rays ML | — | -130 | 9.5 | -8.1% | ❌ -1.00u |
| Moneyline | Los Angeles Dodgers ML | — | -255 | 9.5 | +3.5% | ✅ +0.39u |
| Moneyline | Chicago Cubs ML | — | +102 | 9.5 | +6.7% | ❌ -1.00u |
| Moneyline | Boston Red Sox ML | — | -217 | 9.5 | -2.0% | ✅ +0.46u |
| Moneyline | Arizona Diamondbacks ML | — | -163 | 9.5 | -7.0% | ❌ -1.00u |
| Total | Under 11.0 | 11.0 | -105 | 8.7 | +4.0% | ✅ +0.95u |
| Total | Over 7.5 | 7.5 | -115 | 8.2 | — | ❌ -1.00u |
| Moneyline | Miami Marlins ML | — | -186 | 8.1 | -4.7% | ✅ +0.54u |
| Total | Over 7.5 | 7.5 | -112 | 8.1 | +0.0% | ❌ -1.00u |
| F5 Total | F5 Over 3.5 | 3.5 | -152 | 7.9 | — | ✅ +0.66u |
| F5 Total | F5 Over 3.5 | 3.5 | -154 | 7.5 | +0.0% | ✅ +0.65u |
| Moneyline | San Diego Padres ML | — | -164 | 6.5 | -7.8% | ✅ +0.61u |
| Moneyline | Houston Astros ML | — | -246 | 6.1 | -1.3% | ❌ -1.00u |
| F5 Total | F5 Over 4.5 | 4.5 | -138 | 6.1 | — | ✅ +0.72u |
| NRFI | NRFI | 0.5 | -104 | 5.9 | -0.9% | ❌ -1.00u |
| F5 Total | F5 Over 4.5 | 4.5 | -104 | 5.5 | — | ❌ -1.00u |
| NRFI | NRFI | 0.5 | -128 | 5.3 | — | ❌ -1.00u |
| Total | Under 9.5 | 9.5 | -112 | 5.2 | — | ❌ -1.00u |
| NRFI | NRFI | 0.5 | -192 | 5.1 | -13.5% | ❌ -1.00u |
| Moneyline | Kansas City Royals ML | — | -110 | 5.0 | -2.7% | ✅ +0.91u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Drew Anderson | Ks (P) | Over | 4.5 | +118 | 84% | 4 | -1.4% | ❌ |
| David Peterson | Ks (P) | Over | 4.5 | +109 | 66% | 8 | +0.0% | ✅ |
| Alec Burleson | Hits | Over | 1.5 | +191 | 49% | 1 | — | ❌ |
| Patrick Sandoval | Ks (P) | Under | 5.5 | +114 | 59% | 6 | +14.5% | ❌ |
| Gabriel Hughes | Ks (P) | Over | 3.5 | +125 | 55% | 2 | -0.4% | ❌ |
| Brett Sullivan | Hits | Under | 0.5 | +132 | 59% | 0 | +1.8% | ✅ |
| Myles Straw | Hits | Under | 0.5 | -102 | 68% | 1 | — | ❌ |
| Dylan Cease | Ks (P) | Over | 8.5 | -125 | 67% | 8 | — | ❌ |
| Ke'Bryan Hayes | Hits | Under | 0.5 | -115 | 70% | 0 | +1.6% | ✅ |
| Ryan Johnson | Ks (P) | Under | 3.5 | +122 | 54% | 3 | +11.0% | ✅ |
| Dylan Crews | Hits | Under | 0.5 | +149 | 51% | 1 | — | ❌ |
| Oneil Cruz | Hits | Over | 0.5 | -134 | 73% | 1 | +1.6% | ✅ |
| Esteury Ruiz | Hits | Under | 0.5 | +120 | 58% | 0 | — | ✅ |
| Samuel Basallo | Hits | Under | 0.5 | +117 | 58% | 1 | — | ❌ |
| Jonah Heim | Hits | Under | 0.5 | +101 | 62% | 0 | +2.0% | ✅ |
| Nick Loftin | Hits | Under | 0.5 | +135 | 53% | 1 | +4.4% | ❌ |
| Casey Mize | Ks (P) | Under | 4.5 | -104 | 59% | 0 | +4.9% | ✅ |
| Josh Naylor | Hits | Over | 0.5 | -184 | 80% | 0 | +0.0% | ❌ |
| Hunter Brown | Ks (P) | Under | 6.5 | -150 | 69% | 4 | — | ✅ |
| Taylor Ward | Hits | Over | 0.5 | -154 | 74% | 0 | +2.2% | ❌ |
| Michael Soroka | Ks (P) | Under | 5.5 | +118 | 52% | 3 | -0.9% | ✅ |
| Eury Perez | Ks (P) | Under | 6.5 | -132 | 64% | 4 | — | ✅ |
| Rafael Devers | RBI | Over | 0.5 | +244 | 38% | 0 | -3.1% | ❌ |
| Isaac Paredes | Hits | Over | 0.5 | -205 | 80% | 0 | +2.1% | ❌ |
| Dane Myers | Hits | Under | 0.5 | +102 | 58% | 0 | -2.4% | ✅ |
| Esteury Ruiz | H+R+RBI | Under | 1.5 | -152 | 78% | 0 | — | ✅ |
| Seiya Suzuki | Hits | Over | 0.5 | -184 | 76% | 1 | -2.8% | ✅ |
| Mike Trout | Hits | Over | 0.5 | -169 | 74% | 2 | +7.5% | ✅ |
| Myles Straw | H+R+RBI | Under | 0.5 | +122 | 58% | 1 | — | ❌ |
| Heriberto Hernandez | Hits | Under | 0.5 | +147 | 47% | 1 | — | ❌ |
| Bryce Eldridge | Hits | Over | 0.5 | -181 | 75% | 1 | -1.4% | ✅ |
| Dean Kremer | Ks (P) | Over | 4.5 | +106 | 54% | 5 | -0.5% | ✅ |
| Oneil Cruz | H+R+RBI | Over | 0.5 | -164 | 78% | 4 | -0.2% | ✅ |
| Mickey Moniak | Hits | Under | 0.5 | +192 | 40% | 1 | -0.7% | ❌ |
| Jacob Young | Hits | Under | 0.5 | +123 | 52% | 0 | — | ✅ |
| Salvador Perez | Hits | Under | 0.5 | +180 | 41% | 1 | +2.2% | ❌ |
| Pete Crow-Armstrong | Hits | Over | 0.5 | -191 | 76% | 1 | -1.3% | ✅ |
| Jose Ramirez | Hits | Under | 1.5 | -195 | 76% | 1 | -2.0% | ✅ |
| Jorbit Vivas | Hits | Under | 0.5 | -136 | 66% | 0 | — | ✅ |
| Sal Stewart | RBI | Over | 0.5 | +200 | 42% | 1 | -2.3% | ✅ |
| Brooks Lee | Hits | Over | 0.5 | -142 | 67% | 3 | +0.0% | ✅ |
| Zach Neto | Hits | Over | 0.5 | -199 | 76% | 3 | +0.0% | ✅ |
| Drew Romo | Hits | Under | 0.5 | -126 | 64% | 1 | -1.4% | ❌ |
| Vaughn Grissom | RBI | Over | 0.5 | +240 | 36% | 1 | -4.5% | ✅ |
| Max Muncy | Hits | Under | 0.5 | +117 | 52% | 1 | -2.2% | ❌ |
| Jackson Holliday | Hits | Under | 0.5 | +144 | 47% | 1 | +1.7% | ❌ |
| Michael Soroka | Ks (P) | Under | 6.5 | -162 | 67% | 3 | — | ✅ |
| Caleb Durbin | Hits | Under | 0.5 | +170 | 42% | 2 | +1.9% | ❌ |
| Jakob Marsee | Hits | Under | 0.5 | +145 | 46% | 2 | — | ❌ |
| Vinnie Pasquantino | Hits | Over | 0.5 | -197 | 75% | 0 | +0.2% | ❌ |
| Jake Cronenworth | Hits | Under | 0.5 | +138 | 48% | 2 | +0.0% | ❌ |
| Cole Young | Hits | Over | 0.5 | -165 | 70% | 0 | -6.9% | ❌ |
| Brice Turang | RBI | Over | 0.5 | +248 | 35% | 0 | — | ❌ |
| Nico Hoerner | Hits | Over | 0.5 | -205 | 75% | 1 | +0.5% | ✅ |
| Ildemaro Vargas | Hits | Under | 0.5 | +157 | 44% | 0 | -3.4% | ✅ |
| Zach Neto | RBI | Over | 0.5 | +217 | 38% | 0 | +1.3% | ❌ |
| Jose Ramirez | H+R+RBI | Under | 2.5 | -131 | 68% | 2 | +0.3% | ✅ |
| Esmerlyn Valdez | H+R+RBI | Over | 0.5 | -133 | 68% | 3 | +2.2% | ✅ |
| Alex Bregman | Hits | Over | 0.5 | -181 | 72% | 1 | -2.0% | ✅ |
| Spencer Torkelson | Hits | Under | 0.5 | +127 | 49% | 0 | +1.8% | ✅ |
| Jose Altuve | Hits | Over | 0.5 | -205 | 75% | 0 | +1.9% | ❌ |
| Carson Benge | Hits | Over | 0.5 | -213 | 76% | 3 | +4.1% | ✅ |
| Max Muncy | H+R+RBI | Under | 1.5 | -132 | 67% | 1 | -1.3% | ✅ |
| Bryan Reynolds | Hits | Over | 0.5 | -165 | 69% | 1 | -2.6% | ✅ |
| Jared Young | Hits | Over | 0.5 | -159 | 68% | 2 | +0.0% | ✅ |
| Xander Bogaerts | Hits | Under | 0.5 | +124 | 49% | 1 | +1.8% | ❌ |
| Braden Montgomery | Hits | Over | 0.5 | -174 | 70% | 1 | +0.0% | ✅ |
| Danny Jansen | Hits | Under | 0.5 | -107 | 57% | 0 | +3.1% | ✅ |
| Luis Rengifo | Hits | Over | 0.5 | -155 | 67% | 0 | +6.8% | ❌ |
| Marcus Semien | Hits | Over | 0.5 | -131 | 62% | 2 | +1.6% | ✅ |
| Zach Neto | H+R+RBI | Over | 1.5 | -102 | 59% | 5 | +2.4% | ✅ |
| Derek Hill | Hits | Under | 0.5 | -112 | 58% | 1 | +5.2% | ❌ |
| Alec Burleson | RBI | Over | 0.5 | +153 | 46% | 1 | -27.7% | ✅ |
| Alex Bregman | RBI | Over | 0.5 | +224 | 36% | 1 | -4.1% | ✅ |
| Alec Burleson | H+R+RBI | Over | 1.5 | -137 | 67% | 2 | — | ✅ |
| Jose Siri | Hits | Under | 0.5 | -108 | 57% | 0 | -6.5% | ✅ |
| Joey Ortiz | Hits | Under | 0.5 | +129 | 48% | 1 | — | ❌ |
| Jung Hoo Lee | Hits | Over | 0.5 | -228 | 76% | 1 | -1.2% | ✅ |
| Nick Loftin | H+R+RBI | Under | 1.5 | -143 | 68% | 1 | +3.0% | ✅ |
| Gleyber Torres | Hits | Over | 0.5 | -237 | 77% | 0 | -1.2% | ❌ |
| Seiya Suzuki | RBI | Over | 0.5 | +198 | 38% | 0 | -7.5% | ❌ |
| Colt Keith | H+R+RBI | Under | 1.5 | -121 | 63% | 0 | +4.6% | ✅ |
| Josh Naylor | H+R+RBI | Over | 1.5 | +110 | 54% | 0 | -1.9% | ❌ |
| Jonathan Aranda | Hits | Over | 1.5 | +198 | 36% | 0 | +6.0% | ❌ |
| Cole Carrigg | H+R+RBI | Under | 1.5 | +114 | 53% | 0 | +9.1% | ✅ |
| Teoscar Hernandez | Hits | Under | 0.5 | +136 | 46% | 1 | -1.3% | ❌ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | -102 | 57% | 1 | -4.8% | ❌ |
| Henry Davis | Hits | Under | 0.5 | -147 | 64% | 0 | +3.1% | ✅ |
| Jordan Walker | H+R+RBI | Over | 1.5 | -137 | 66% | 0 | — | ❌ |
| Brett Sullivan | H+R+RBI | Under | 1.5 | -137 | 66% | 0 | +0.9% | ✅ |
| Salvador Perez | H+R+RBI | Under | 1.5 | -107 | 59% | 3 | +3.5% | ❌ |
| Gabriel Moreno | RBI | Over | 0.5 | +172 | 42% | 0 | +4.2% | ❌ |
| Tristan Peters | Hits | Over | 0.5 | -126 | 60% | 1 | +0.3% | ✅ |
| Munetaka Murakami | Hits | Over | 0.5 | -148 | 64% | 1 | +2.1% | ✅ |
| Liam Hicks | RBI | Over | 0.5 | +203 | 37% | 1 | -1.9% | ✅ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | +137 | 48% | 2 | — | ✅ |
| Brice Turang | Hits | Under | 0.5 | +146 | 44% | 0 | — | ✅ |
| Brooks Lee | H+R+RBI | Over | 0.5 | -168 | 71% | 6 | +0.2% | ✅ |
| Chase DeLauter | H+R+RBI | Under | 2.5 | -127 | 63% | 1 | +1.4% | ✅ |
| Leody Taveras | Hits | Under | 0.5 | +106 | 52% | 0 | +0.0% | ✅ |
| Joey Ortiz | H+R+RBI | Under | 1.5 | -152 | 68% | 2 | — | ❌ |
| Alex Bregman | H+R+RBI | Over | 1.5 | +106 | 54% | 3 | -4.6% | ✅ |
| Michael Harris II | Hits | Over | 0.5 | -177 | 69% | 2 | — | ✅ |
| Connor Norby | H+R+RBI | Under | 1.5 | -140 | 65% | 3 | — | ❌ |
| Christian Walker | Hits | Over | 0.5 | -174 | 68% | 1 | +2.4% | ✅ |
| Jakob Marsee | H+R+RBI | Under | 1.5 | -118 | 60% | 4 | — | ❌ |
| Tyler O'Neill | H+R+RBI | Under | 1.5 | -165 | 70% | 0 | -0.9% | ✅ |
| Kevin McGonigle | Hits | Over | 0.5 | -249 | 76% | 0 | +1.0% | ❌ |
| Martin Perez | Ks (P) | Over | 3.5 | -107 | 54% | 2 | — | ❌ |
| Kazuma Okamoto | Hits | Over | 0.5 | -159 | 66% | 1 | — | ✅ |
| Nathaniel Lowe | H+R+RBI | Under | 2.5 | -162 | 69% | 1 | — | ✅ |
| Vaughn Grissom | H+R+RBI | Over | 1.5 | +115 | 52% | 2 | +1.9% | ✅ |
| Jose Ramirez | RBI | Under | 0.5 | -154 | 68% | 0 | +1.5% | ✅ |
| Derek Hill | H+R+RBI | Under | 0.5 | +118 | 51% | 2 | +6.3% | ❌ |
| Ke'Bryan Hayes | H+R+RBI | Under | 0.5 | +107 | 54% | 0 | +2.0% | ✅ |
| Randy Arozarena | Hits | Over | 0.5 | -232 | 74% | 3 | -0.1% | ✅ |
| Dylan Crews | H+R+RBI | Under | 1.5 | -152 | 67% | 2 | — | ❌ |
| Eugenio Suarez | Hits | Over | 0.5 | -147 | 63% | 0 | -0.8% | ❌ |
| Jo Adell | H+R+RBI | Under | 2.5 | -148 | 66% | 7 | -2.0% | ❌ |
| Mike Trout | H+R+RBI | Over | 1.5 | +106 | 54% | 4 | +6.5% | ✅ |
| Esmerlyn Valdez | Hits | Over | 0.5 | -103 | 54% | 2 | +2.8% | ✅ |
| Pete Crow-Armstrong | H+R+RBI | Over | 1.5 | -111 | 58% | 1 | -4.0% | ❌ |
| Jackson Holliday | H+R+RBI | Under | 1.5 | -141 | 65% | 2 | +0.3% | ❌ |
| Brandon Young | Ks (P) | Under | 3.5 | +108 | 50% | 3 | +3.0% | ✅ |
| Carlos Cortes | H+R+RBI | Under | 1.5 | -182 | 71% | 1 | — | ✅ |
| Carter Jensen | H+R+RBI | Under | 1.5 | -116 | 59% | 0 | +3.5% | ✅ |
| Trent Grisham | Hits | Under | 0.5 | -101 | 53% | 0 | — | ✅ |
| Joc Pederson | H+R+RBI | Under | 1.5 | -119 | 60% | 0 | +0.0% | ✅ |
| Ryan Jeffers | Hits | Under | 0.5 | +143 | 44% | 2 | +0.0% | ❌ |
| Michael Busch | Hits | Over | 0.5 | -171 | 67% | 1 | -5.7% | ✅ |
| Jordan Walker | RBI | Over | 0.5 | +134 | 47% | 0 | -34.1% | ❌ |
| Andrew Vaughn | H+R+RBI | Under | 1.5 | -124 | 61% | 1 | — | ✅ |
| Tyler O'Neill | Hits | Under | 0.5 | +116 | 49% | 0 | +2.4% | ✅ |
| Travis Bazzana | Hits | Over | 1.5 | +186 | 37% | 1 | — | ❌ |
| Trevor Larnach | Hits | Over | 0.5 | -119 | 57% | 0 | +0.0% | ❌ |
| Trevor Larnach | H+R+RBI | Over | 0.5 | -149 | 66% | 0 | -1.4% | ❌ |
| Nick Gonzales | Hits | Over | 0.5 | -176 | 68% | 0 | +1.8% | ❌ |
| Willy Adames | Hits | Over | 0.5 | -162 | 65% | 2 | -1.4% | ✅ |
| Austin Riley | H+R+RBI | Over | 0.5 | -134 | 62% | 0 | — | ❌ |
| Mauricio Dubon | Hits | Over | 0.5 | -168 | 66% | 2 | — | ✅ |
| Zach McKinstry | H+R+RBI | Under | 1.5 | -142 | 64% | 0 | -1.5% | ✅ |
| Shohei Ohtani | Hits | Over | 0.5 | -229 | 74% | 0 | +2.3% | ❌ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +187 | 38% | 0 | -4.0% | ❌ |
| Josh Bell | Hits | Over | 0.5 | -169 | 66% | 0 | -2.0% | ❌ |
| Dane Myers | H+R+RBI | Under | 0.5 | +125 | 48% | 0 | -5.1% | ✅ |
| Jeff McNeil | Hits | Under | 0.5 | +142 | 44% | 2 | +2.1% | ❌ |
| Heriberto Hernandez | H+R+RBI | Under | 1.5 | -119 | 59% | 3 | — | ❌ |
| JJ Wetherholt | Hits | Over | 0.5 | -223 | 73% | 2 | -16.8% | ✅ |
| Marcus Semien | H+R+RBI | Over | 0.5 | -164 | 68% | 3 | +1.6% | ✅ |
| Nico Hoerner | RBI | Over | 0.5 | +247 | 31% | 0 | +1.5% | ❌ |
| Taylor Ward | H+R+RBI | Over | 1.5 | +118 | 50% | 0 | +3.3% | ❌ |
| Chase Meidroth | Hits | Over | 0.5 | -173 | 67% | 2 | +1.0% | ✅ |
| Ildemaro Vargas | RBI | Over | 0.5 | +211 | 35% | 0 | +2.0% | ❌ |
| Luke Keaschall | Hits | Under | 0.5 | +157 | 41% | 2 | +0.0% | ❌ |
| Brett Baty | H+R+RBI | Over | 0.5 | -165 | 68% | 1 | +0.0% | ✅ |
| Josh Lowe | Hits | Over | 0.5 | -140 | 61% | 0 | — | ❌ |
| Max Muncy | RBI | Under | 0.5 | -240 | 76% | 0 | -3.3% | ✅ |
| Willy Adames | RBI | Over | 0.5 | +231 | 33% | 1 | -2.6% | ✅ |
| Matt McLain | Hits | Under | 0.5 | -105 | 54% | 1 | +0.0% | ❌ |
| Rafael Devers | H+R+RBI | Over | 1.5 | +110 | 52% | 0 | -2.3% | ❌ |
| Cole Young | H+R+RBI | Over | 1.5 | +122 | 49% | 0 | — | ❌ |
| Alejandro Kirk | RBI | Over | 0.5 | +216 | 34% | 0 | — | ❌ |
| Royce Lewis | Hits | Over | 0.5 | -154 | 64% | 0 | +0.0% | ❌ |
| Edmundo Sosa | H+R+RBI | Under | 1.5 | -137 | 63% | 5 | — | ❌ |
| Griffin Conine | H+R+RBI | Under | 1.5 | -113 | 57% | 1 | — | ✅ |
| Luis Arraez | Hits | Over | 1.5 | +167 | 39% | 1 | — | ❌ |
| Jake Cronenworth | H+R+RBI | Under | 1.5 | -135 | 62% | 6 | -2.3% | ❌ |
| Jung Hoo Lee | H+R+RBI | Over | 1.5 | +103 | 53% | 1 | +0.0% | ❌ |
| Lars Nootbaar | H+R+RBI | Under | 1.5 | -108 | 56% | 3 | -7.4% | ❌ |
| Cedric Mullins | Hits | Under | 0.5 | +127 | 46% | 1 | +7.1% | ❌ |
| Jo Adell | Hits | Under | 1.5 | -244 | 74% | 2 | -1.5% | ❌ |
| Austin Wells | Hits | Over | 0.5 | +132 | 45% | 1 | — | ✅ |
| Josh Bell | RBI | Over | 0.5 | +213 | 34% | 0 | -2.2% | ❌ |
| Nolan Arenado | RBI | Over | 0.5 | +191 | 37% | 1 | +12.8% | ✅ |
| Luis Campusano | Hits | Over | 0.5 | -185 | 68% | 1 | — | ✅ |
| Liam Hicks | H+R+RBI | Over | 1.5 | -105 | 55% | 3 | +0.0% | ✅ |
| Mike Yastrzemski | Hits | Over | 0.5 | +113 | 49% | 0 | — | ❌ |
| Cam Smith | Hits | Under | 0.5 | +131 | 45% | 0 | +0.0% | ✅ |
| Bryan Torres | H+R+RBI | Under | 1.5 | -173 | 68% | 0 | — | ✅ |
| Fernando Tatis Jr. | H+R+RBI | Under | 2.5 | -156 | 65% | 4 | +2.4% | ❌ |
| Willy Adames | H+R+RBI | Over | 1.5 | +118 | 49% | 4 | -3.5% | ✅ |
| Jacob Young | H+R+RBI | Under | 1.5 | -173 | 68% | 0 | — | ✅ |
| Bryce Eldridge | H+R+RBI | Over | 1.5 | +107 | 52% | 1 | -1.9% | ❌ |
| Zach McKinstry | Hits | Under | 0.5 | +141 | 43% | 0 | -1.6% | ✅ |
| Eugenio Suarez | RBI | Over | 0.5 | +227 | 33% | 0 | -4.4% | ❌ |
| Kyle Schwarber | Hits | Over | 0.5 | -171 | 66% | 2 | — | ✅ |
| Jake McCarthy | Hits | Under | 1.5 | -197 | 69% | 2 | +4.7% | ❌ |
| Bryce Eldridge | RBI | Over | 0.5 | +224 | 33% | 0 | -2.1% | ❌ |
| Jake McCarthy | H+R+RBI | Under | 2.5 | -167 | 67% | 2 | — | ✅ |
| Carlos Cortes | Hits | Under | 0.5 | +109 | 50% | 1 | +1.5% | ❌ |
| Ozzie Albies | H+R+RBI | Over | 0.5 | -160 | 66% | 2 | — | ✅ |
| Nico Hoerner | H+R+RBI | Over | 1.5 | +105 | 52% | 2 | +1.0% | ✅ |
| Griffin Conine | RBI | Under | 0.5 | -193 | 70% | 0 | — | ✅ |
| Brandon Nimmo | H+R+RBI | Under | 1.5 | +103 | 52% | 0 | +0.0% | ✅ |
| Austin Riley | Hits | Over | 0.5 | -114 | 55% | 0 | — | ❌ |
| Jake Burger | Hits | Over | 0.5 | -177 | 66% | 0 | -0.2% | ❌ |
| Drake Baldwin | Hits | Over | 0.5 | -180 | 67% | 0 | — | ❌ |
| Andruw Monasterio | H+R+RBI | Under | 1.5 | -139 | 62% | 1 | +0.0% | ✅ |
| Richie Palacios | Hits | Over | 0.5 | -147 | 62% | 0 | +0.0% | ❌ |
| Lars Nootbaar | RBI | Under | 0.5 | -219 | 73% | 1 | +6.5% | ❌ |
| Ben Rice | Hits | Over | 0.5 | -148 | 62% | 0 | — | ❌ |
| Michael Wacha | Ks (P) | Over | 4.5 | +122 | 46% | 6 | -0.9% | ✅ |
| Mickey Moniak | H+R+RBI | Under | 1.5 | +109 | 51% | 3 | +0.0% | ❌ |
| Zack Gelof | H+R+RBI | Over | 0.5 | -180 | 68% | 1 | -1.2% | ✅ |
| Ivan Herrera | Hits | Over | 0.5 | -233 | 72% | 0 | -22.0% | ❌ |
| Rhett Lowder | Ks (P) | Over | 3.5 | -113 | 54% | 1 | -0.8% | ❌ |
| Isaac Paredes | H+R+RBI | Over | 1.5 | -113 | 56% | 0 | +3.2% | ❌ |
| Brandon Nimmo | RBI | Under | 0.5 | -200 | 70% | 0 | +0.5% | ✅ |
| Tanner Bibee | Ks (P) | Under | 4.5 | -113 | 54% | 6 | +4.7% | ❌ |
| Matt Olson | Hits | Over | 0.5 | -153 | 62% | 1 | — | ✅ |
| Ian Happ | H+R+RBI | Over | 0.5 | -174 | 67% | 0 | — | ❌ |
| Connor Norby | Hits | Under | 0.5 | +129 | 45% | 1 | — | ❌ |
| Javier Sanoja | H+R+RBI | Under | 1.5 | -128 | 59% | 0 | — | ✅ |
| Geraldo Perdomo | Hits | Over | 0.5 | -222 | 71% | 0 | -0.6% | ❌ |
| Gleyber Torres | RBI | Over | 0.5 | +227 | 32% | 0 | +3.8% | ❌ |
| Ben Rice | RBI | Over | 0.5 | +216 | 33% | 0 | — | ❌ |
| Wyatt Langford | Hits | Over | 0.5 | -217 | 71% | 0 | +0.0% | ❌ |
| Luis Robert Jr. | Hits | Under | 0.5 | +124 | 46% | 2 | -1.8% | ❌ |
| Xavier Edwards | H+R+RBI | Under | 1.5 | +106 | 51% | 1 | — | ✅ |
| Samuel Basallo | H+R+RBI | Under | 1.5 | -171 | 66% | 4 | — | ❌ |
| Josh Lowe | H+R+RBI | Over | 0.5 | -165 | 65% | 0 | — | ❌ |
| Luke Keaschall | H+R+RBI | Under | 1.5 | -129 | 59% | 5 | +1.7% | ❌ |
| Francisco Lindor | Hits | Over | 0.5 | -219 | 70% | 0 | +0.0% | ❌ |
| Xavier Edwards | RBI | Under | 0.5 | -228 | 72% | 0 | — | ✅ |
| Gabriel Moreno | H+R+RBI | Over | 1.5 | -136 | 60% | 1 | +3.6% | ❌ |
| Nick Gonzales | H+R+RBI | Over | 1.5 | +133 | 45% | 0 | +4.5% | ❌ |
| Bryson Stott | RBI | Over | 0.5 | +220 | 32% | 0 | — | ❌ |
| Mauricio Dubon | H+R+RBI | Over | 0.5 | -190 | 68% | 2 | — | ✅ |
| Corbin Carroll | H+R+RBI | Under | 1.5 | +109 | 50% | 2 | -3.7% | ❌ |
| Wilyer Abreu | H+R+RBI | Under | 1.5 | +112 | 49% | 1 | -0.9% | ✅ |
| Kazuma Okamoto | H+R+RBI | Over | 1.5 | +118 | 48% | 2 | — | ✅ |
| Braden Montgomery | RBI | Over | 0.5 | +234 | 31% | 2 | +2.1% | ✅ |
| Jorbit Vivas | H+R+RBI | Under | 0.5 | -103 | 53% | 0 | — | ✅ |
| Nathan Church | RBI | Over | 0.5 | +244 | 30% | 0 | -34.5% | ❌ |
| Evan Carter | H+R+RBI | Under | 1.5 | -160 | 64% | 0 | +1.4% | ✅ |
| Cal Raleigh | RBI | Over | 0.5 | +199 | 35% | 0 | +2.4% | ❌ |
| Tarik Skubal | Ks (P) | Under | 8.5 | -132 | 58% | 11 | +0.0% | ❌ |
| Ryan Vilade | H+R+RBI | Under | 1.5 | -155 | 63% | 0 | — | ✅ |
| Gavin Sheets | H+R+RBI | Under | 1.5 | -165 | 64% | 0 | +2.4% | ✅ |
| Lars Nootbaar | Hits | Under | 0.5 | +161 | 39% | 2 | -8.1% | ❌ |
| Yainer Diaz | Hits | Over | 0.5 | -203 | 68% | 1 | +2.8% | ✅ |
| Jeff McNeil | H+R+RBI | Under | 1.5 | -160 | 64% | 3 | -0.2% | ❌ |
| Bo Bichette | RBI | Over | 0.5 | +196 | 35% | 1 | +4.6% | ✅ |
| Colson Montgomery | Hits | Over | 0.5 | -132 | 58% | 0 | +0.3% | ❌ |
| Luis Rengifo | H+R+RBI | Over | 1.5 | +122 | 46% | 0 | +8.3% | ❌ |
| Bryan Torres | Hits | Under | 0.5 | +109 | 49% | 0 | — | ✅ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +122 | 46% | 3 | +2.3% | ✅ |
| Elly De La Cruz | RBI | Over | 0.5 | +217 | 32% | 1 | -5.1% | ✅ |
| Jose Caballero | H+R+RBI | Over | 0.5 | -132 | 59% | 0 | — | ❌ |
| Bobby Witt Jr. | H+R+RBI | Under | 1.5 | +120 | 47% | 1 | +6.3% | ✅ |
| Pete Alonso | RBI | Over | 0.5 | +179 | 37% | 0 | +7.7% | ❌ |
| Xander Bogaerts | H+R+RBI | Under | 1.5 | -149 | 62% | 1 | +0.0% | ✅ |
| Donovan Walton | Hits | Under | 0.5 | -121 | 56% | 1 | +2.2% | ❌ |
| Jazz Chisholm Jr. | H+R+RBI | Over | 0.5 | -155 | 62% | 2 | — | ✅ |
| Isaac Paredes | RBI | Over | 0.5 | +173 | 38% | 0 | +4.6% | ❌ |
| Geraldo Perdomo | H+R+RBI | Under | 1.5 | -102 | 52% | 0 | +3.7% | ✅ |
| Teoscar Hernandez | H+R+RBI | Under | 1.5 | -130 | 58% | 2 | -0.3% | ❌ |
| Yainer Diaz | H+R+RBI | Under | 1.5 | -118 | 56% | 2 | -1.2% | ❌ |
| Ty France | H+R+RBI | Under | 1.5 | -115 | 55% | 2 | +1.6% | ❌ |
| A.J. Ewing | Hits | Over | 0.5 | -213 | 69% | 1 | +0.0% | ✅ |
| Corey Seager | H+R+RBI | Under | 1.5 | +100 | 51% | 0 | +0.0% | ✅ |
| Randy Arozarena | H+R+RBI | Over | 1.5 | -115 | 55% | 8 | +0.0% | ✅ |
| Spencer Torkelson | H+R+RBI | Under | 1.5 | -137 | 59% | 0 | -0.6% | ✅ |
| Owen Caissie | H+R+RBI | Under | 1.5 | -152 | 62% | 2 | — | ❌ |
| Manny Machado | H+R+RBI | Under | 1.5 | -115 | 55% | 1 | +0.0% | ✅ |
| Josh Bell | H+R+RBI | Over | 1.5 | +115 | 48% | 0 | -2.3% | ❌ |
| Willi Castro | H+R+RBI | Under | 1.5 | +101 | 51% | 2 | +7.1% | ❌ |
| Vaughn Grissom | Hits | Over | 0.5 | -187 | 66% | 1 | +2.5% | ✅ |
| Mookie Betts | H+R+RBI | Under | 1.5 | -104 | 52% | 1 | -2.4% | ✅ |
| Chase DeLauter | Hits | Under | 1.5 | -180 | 65% | 0 | +0.0% | ✅ |
| Ernie Clement | Hits | Over | 0.5 | -212 | 69% | 2 | — | ✅ |
| Jeremy Pena | RBI | Over | 0.5 | +189 | 35% | 1 | +0.7% | ✅ |
| Shane McClanahan | Ks (P) | Over | 4.5 | -102 | 51% | 5 | +1.0% | ✅ |
| Kyle Karros | Hits | Under | 0.5 | +143 | 42% | 0 | -10.7% | ✅ |
| Lawrence Butler | H+R+RBI | Under | 0.5 | +131 | 44% | 4 | +1.8% | ❌ |
| Jonah Heim | H+R+RBI | Under | 0.5 | +128 | 45% | 1 | +2.2% | ❌ |
| Michael Massey | H+R+RBI | Under | 1.5 | -135 | 58% | 0 | +3.6% | ✅ |
| Kyle Karros | H+R+RBI | Under | 1.5 | -129 | 57% | 0 | -8.2% | ✅ |
| Bryson Stott | H+R+RBI | Over | 1.5 | +110 | 48% | 0 | — | ❌ |
| Andrew Vaughn | Hits | Over | 0.5 | -190 | 66% | 1 | — | ✅ |
| Byron Buxton | RBI | Under | 0.5 | -223 | 70% | 0 | +1.5% | ✅ |
| Jared Jones | Ks (P) | Under | 4.5 | -104 | 51% | 5 | -9.2% | ❌ |
| Moises Ballesteros | H+R+RBI | Under | 1.5 | -168 | 64% | 3 | -6.9% | ❌ |
| Kyle Isbel | H+R+RBI | Under | 1.5 | -171 | 64% | 3 | — | ❌ |
| Adley Rutschman | RBI | Over | 0.5 | +183 | 36% | 0 | -0.3% | ❌ |
| Samuel Basallo | RBI | Over | 0.5 | +250 | 29% | 2 | — | ✅ |
| Carter Jensen | Hits | Under | 0.5 | +150 | 40% | 0 | +4.2% | ✅ |
| Yordan Alvarez | H+R+RBI | Under | 2.5 | -149 | 61% | 0 | -0.3% | ✅ |
| Corbin Carroll | Hits | Under | 0.5 | +184 | 36% | 2 | -2.1% | ❌ |
| Tyrone Taylor | H+R+RBI | Over | 0.5 | -136 | 58% | 3 | +8.8% | ✅ |
| Kody Clemens | Hits | Over | 0.5 | -169 | 63% | 2 | -1.6% | ✅ |
| Kyle Schwarber | RBI | Over | 0.5 | +171 | 37% | 2 | -22.6% | ✅ |
| Joe Mack | H+R+RBI | Under | 1.5 | -152 | 61% | 1 | — | ✅ |
| Mike Yastrzemski | H+R+RBI | Over | 0.5 | -108 | 53% | 0 | — | ❌ |
| JJ Wetherholt | H+R+RBI | Over | 1.5 | -125 | 56% | 4 | — | ✅ |
| Matt Olson | H+R+RBI | Over | 1.5 | +115 | 47% | 1 | — | ❌ |
| Sam Antonacci | Hits | Under | 0.5 | +148 | 41% | 1 | -2.8% | ❌ |
| Tim Tawa | Hits | Over | 0.5 | -174 | 64% | 2 | +7.3% | ✅ |
| Coby Mayo | H+R+RBI | Under | 1.5 | -155 | 61% | 2 | -0.5% | ❌ |
| Lawrence Butler | Hits | Under | 0.5 | -107 | 52% | 2 | +0.0% | ❌ |
| Liam Hicks | Hits | Over | 0.5 | -215 | 69% | 1 | -1.1% | ✅ |
| Fernando Tatis Jr. | Hits | Under | 1.5 | -219 | 69% | 2 | -0.4% | ❌ |
| Nathaniel Lowe | RBI | Under | 0.5 | -182 | 65% | 0 | +1.0% | ✅ |
| Travis Bazzana | H+R+RBI | Under | 1.5 | +121 | 46% | 1 | +6.8% | ✅ |
| William Contreras | H+R+RBI | Under | 1.5 | -107 | 52% | 4 | — | ❌ |
| Brady House | Hits | Under | 0.5 | +109 | 48% | 0 | — | ✅ |
| Luis Robert Jr. | RBI | Over | 0.5 | +237 | 30% | 3 | +3.7% | ✅ |
| Jake Burger | RBI | Over | 0.5 | +172 | 37% | 0 | -3.2% | ❌ |
| Caleb Durbin | H+R+RBI | Under | 1.5 | -112 | 53% | 3 | -0.4% | ❌ |
| Luis Campusano | H+R+RBI | Under | 1.5 | -136 | 58% | 2 | — | ❌ |
| Cam Smith | H+R+RBI | Under | 1.5 | -131 | 57% | 0 | +0.0% | ✅ |
| A.J. Ewing | H+R+RBI | Under | 1.5 | -121 | 55% | 2 | +0.0% | ❌ |
| Bobby Witt Jr. | RBI | Under | 0.5 | -229 | 70% | 0 | +3.2% | ✅ |
| Matt McLain | H+R+RBI | Over | 0.5 | -164 | 62% | 4 | -0.7% | ✅ |
| Tristan Peters | H+R+RBI | Over | 0.5 | -159 | 62% | 3 | +0.0% | ✅ |
| Cedric Mullins | H+R+RBI | Under | 1.5 | -139 | 58% | 1 | +5.3% | ✅ |
| Travis Bazzana | RBI | Under | 0.5 | -194 | 66% | 0 | +4.2% | ✅ |
| Alejandro Kirk | Hits | Over | 0.5 | -204 | 67% | 1 | — | ✅ |
| Spencer Jones | H+R+RBI | Over | 0.5 | -119 | 55% | 0 | — | ❌ |
| Ben Rice | H+R+RBI | Over | 1.5 | +119 | 46% | 1 | — | ❌ |
| Sam Antonacci | H+R+RBI | Under | 1.5 | -125 | 56% | 2 | +0.0% | ❌ |
| Heliot Ramos | Hits | Over | 0.5 | -158 | 61% | 0 | — | ❌ |
| Tim Tawa | H+R+RBI | Under | 1.5 | -141 | 59% | 5 | -7.5% | ❌ |
| Trent Grisham | RBI | Over | 0.5 | +247 | 29% | 0 | — | ❌ |
| Jose Altuve | RBI | Under | 0.5 | -234 | 70% | 0 | -0.9% | ✅ |
| Bo Bichette | H+R+RBI | Over | 1.5 | -119 | 55% | 4 | +1.5% | ✅ |
| Cal Raleigh | H+R+RBI | Under | 1.5 | -161 | 62% | 1 | +2.1% | ✅ |
| Yandy Diaz | Hits | Over | 1.5 | +153 | 40% | 2 | +5.9% | ✅ |
| Ronald Acuna Jr. | H+R+RBI | Under | 1.5 | -139 | 58% | 0 | — | ✅ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -126 | 56% | 0 | +3.4% | ❌ |
| Mookie Betts | RBI | Under | 0.5 | -210 | 68% | 0 | +1.3% | ✅ |
| Tommy Edman | H+R+RBI | Under | 1.5 | -126 | 56% | 0 | -2.2% | ✅ |
| Chase DeLauter | RBI | Under | 0.5 | -171 | 63% | 0 | +2.5% | ✅ |
| TJ Rumfield | H+R+RBI | Under | 1.5 | -101 | 50% | 0 | -3.4% | ✅ |
| Brett Baty | Hits | Over | 0.5 | -138 | 58% | 1 | -1.2% | ✅ |
| Colson Montgomery | RBI | Over | 0.5 | +186 | 35% | 0 | +2.5% | ❌ |
| Willi Castro | RBI | Under | 0.5 | -212 | 68% | 0 | +4.6% | ✅ |
| Gleyber Torres | H+R+RBI | Over | 1.5 | -120 | 54% | 0 | -1.5% | ❌ |
| Jonathan Aranda | RBI | Over | 0.5 | +168 | 37% | 0 | -1.5% | ❌ |
| Vinnie Pasquantino | H+R+RBI | Over | 1.5 | -104 | 51% | 0 | -0.5% | ❌ |
| Jake McCarthy | RBI | Over | 0.5 | +190 | 34% | 0 | -7.3% | ❌ |
| Cal Raleigh | Hits | Under | 0.5 | +101 | 50% | 1 | +2.0% | ❌ |
| Henry Bolte | H+R+RBI | Under | 1.5 | -165 | 62% | 0 | -2.6% | ✅ |
| Mickey Gasper | H+R+RBI | Under | 1.5 | -139 | 58% | 1 | +1.5% | ✅ |
| Edmundo Sosa | Hits | Under | 0.5 | +138 | 42% | 2 | — | ❌ |
| Sal Stewart | H+R+RBI | Over | 1.5 | -118 | 54% | 6 | -3.6% | ✅ |
| Austin Wells | H+R+RBI | Over | 0.5 | +100 | 50% | 2 | — | ✅ |
| Ezequiel Duran | RBI | Over | 0.5 | +203 | 33% | 0 | +0.3% | ❌ |
| Josh Naylor | RBI | Over | 0.5 | +228 | 30% | 0 | -2.7% | ❌ |
| Jose Altuve | H+R+RBI | Over | 1.5 | -114 | 53% | 0 | +3.2% | ❌ |
| Ildemaro Vargas | H+R+RBI | Under | 1.5 | -123 | 55% | 1 | -0.4% | ✅ |
| Adley Rutschman | H+R+RBI | Under | 1.5 | -112 | 52% | 0 | +0.4% | ✅ |
| Tyrone Taylor | Hits | Over | 0.5 | -112 | 52% | 1 | +9.4% | ✅ |
| Michael Busch | RBI | Over | 0.5 | +216 | 31% | 1 | -5.7% | ✅ |
| Carson Benge | RBI | Under | 0.5 | -225 | 69% | 2 | -3.2% | ❌ |
| Jazz Chisholm Jr. | Hits | Under | 0.5 | -119 | 54% | 2 | — | ❌ |
| Rafael Devers | Hits | Over | 0.5 | -183 | 64% | 0 | -1.4% | ❌ |
| Jake Bauers | H+R+RBI | Over | 1.5 | +105 | 48% | 4 | — | ✅ |
| Jeremy Pena | H+R+RBI | Under | 1.5 | +116 | 46% | 2 | -1.4% | ❌ |
| Kyle Tucker | Hits | Over | 0.5 | -152 | 60% | 1 | -2.2% | ✅ |
| Dillon Dingler | H+R+RBI | Under | 1.5 | +107 | 48% | 1 | +3.0% | ✅ |
| Michael Busch | H+R+RBI | Over | 1.5 | +113 | 46% | 3 | -6.6% | ✅ |
| Jake Mangum | H+R+RBI | Over | 0.5 | -181 | 64% | 0 | +1.0% | ❌ |
| Wilyer Abreu | Hits | Under | 0.5 | +195 | 34% | 0 | +1.4% | ✅ |
| Ivan Herrera | H+R+RBI | Over | 1.5 | -126 | 55% | 0 | — | ❌ |
| Christian Walker | H+R+RBI | Over | 1.5 | -105 | 51% | 2 | +3.1% | ✅ |
| Otto Lopez | H+R+RBI | Under | 1.5 | +113 | 46% | 3 | — | ❌ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | -101 | 50% | 1 | +3.3% | ❌ |
| Jarren Duran | H+R+RBI | Under | 1.5 | -123 | 55% | 0 | +0.4% | ✅ |
| Carson Benge | H+R+RBI | Over | 1.5 | -116 | 53% | 7 | +7.0% | ✅ |
| Corey Seager | RBI | Under | 0.5 | -225 | 68% | 0 | +0.1% | ✅ |
| Freddie Freeman | RBI | Under | 0.5 | -236 | 69% | 0 | +1.9% | ✅ |
| Wilyer Abreu | RBI | Under | 0.5 | -194 | 65% | 1 | -1.1% | ❌ |
| Nolan Arenado | H+R+RBI | Over | 1.5 | -105 | 50% | 5 | +5.3% | ✅ |
| Corbin Carroll | RBI | Under | 0.5 | -225 | 68% | 0 | -2.1% | ✅ |
| Julio Rodriguez | Hits | Over | 0.5 | -225 | 68% | 0 | -1.0% | ❌ |
| Francisco Alvarez | Hits | Over | 0.5 | -147 | 59% | 1 | +0.0% | ✅ |
| Braden Montgomery | H+R+RBI | Over | 1.5 | +110 | 47% | 4 | +1.9% | ✅ |
| Danny Jansen | H+R+RBI | Under | 0.5 | +128 | 43% | 0 | +2.7% | ✅ |
| George Springer | H+R+RBI | Under | 1.5 | -140 | 57% | 4 | — | ❌ |
| Andrew Painter | Ks (P) | Under | 3.5 | +122 | 45% | 8 | — | ❌ |
| Drake Baldwin | H+R+RBI | Over | 1.5 | +106 | 48% | 1 | — | ❌ |
| Henry Bolte | Hits | Under | 0.5 | +127 | 44% | 0 | -5.4% | ✅ |
| Nathan Church | Hits | Over | 0.5 | -172 | 62% | 2 | -26.4% | ✅ |
| Richie Palacios | H+R+RBI | Over | 1.5 | +135 | 42% | 0 | +4.0% | ❌ |
| Colson Montgomery | H+R+RBI | Over | 1.5 | +123 | 44% | 0 | +1.8% | ❌ |
| Freddie Freeman | H+R+RBI | Under | 1.5 | +103 | 48% | 1 | -1.0% | ✅ |
| Ty France | RBI | Under | 0.5 | -246 | 70% | 1 | +1.6% | ❌ |
| Willi Castro | Hits | Over | 0.5 | -242 | 70% | 1 | -3.4% | ✅ |
| Jackson Chourio | RBI | Under | 0.5 | -243 | 69% | 0 | — | ✅ |
| Heriberto Hernandez | RBI | Under | 0.5 | -227 | 68% | 1 | — | ❌ |
| Ivan Herrera | RBI | Over | 0.5 | +198 | 33% | 0 | -22.6% | ❌ |
| Adley Rutschman | Hits | Over | 0.5 | -214 | 67% | 0 | -1.1% | ❌ |
| Elly De La Cruz | Hits | Under | 0.5 | +168 | 37% | 4 | +1.9% | ❌ |
| Ceddanne Rafaela | H+R+RBI | Under | 1.5 | +112 | 46% | 1 | +0.5% | ✅ |
| JJ Bleday | H+R+RBI | Under | 1.5 | -146 | 58% | 9 | +1.4% | ❌ |
| Daulton Varsho | H+R+RBI | Under | 1.5 | -147 | 58% | 4 | +0.3% | ❌ |
| Eugenio Suarez | H+R+RBI | Over | 1.5 | +131 | 42% | 0 | — | ❌ |
| Ezequiel Duran | H+R+RBI | Over | 1.5 | -103 | 50% | 0 | +0.0% | ❌ |
| Salvador Perez | RBI | Under | 0.5 | -234 | 68% | 1 | +2.1% | ❌ |
| Bobby Witt Jr. | Hits | Under | 1.5 | -244 | 70% | 1 | +1.7% | ✅ |
| Nolan Arenado | Hits | Under | 0.5 | +143 | 40% | 1 | -6.5% | ❌ |
| Miguel Vargas | Hits | Over | 0.5 | -186 | 64% | 1 | +1.1% | ✅ |
| Mickey Moniak | RBI | Under | 0.5 | -177 | 62% | 1 | +3.3% | ❌ |
| Kazuma Okamoto | RBI | Over | 0.5 | +189 | 34% | 0 | — | ❌ |
| Jake Irvin | Ks (P) | Under | 4.5 | -122 | 54% | 4 | — | ✅ |
| Luis Arraez | RBI | Under | 0.5 | -224 | 67% | 0 | +12.5% | ✅ |
| TJ Rumfield | RBI | Under | 0.5 | -243 | 69% | 0 | -1.8% | ✅ |
| Yandy Diaz | H+R+RBI | Over | 1.5 | -164 | 60% | 3 | — | ✅ |
| J.T. Realmuto | H+R+RBI | Under | 1.5 | -138 | 56% | 4 | -23.4% | ❌ |
| Kyle Tucker | H+R+RBI | Under | 1.5 | -148 | 58% | 4 | +2.4% | ❌ |
| Wyatt Langford | RBI | Under | 0.5 | -248 | 69% | 0 | +0.2% | ✅ |
| Byron Buxton | H+R+RBI | Under | 1.5 | -115 | 52% | 0 | +0.0% | ✅ |
| Manny Machado | RBI | Under | 0.5 | -220 | 67% | 0 | +0.1% | ✅ |
| Andrew Benintendi | H+R+RBI | Under | 1.5 | -161 | 60% | 2 | -1.7% | ❌ |
| Gavin Sheets | Hits | Under | 0.5 | +106 | 48% | 0 | +2.5% | ✅ |
| Alejandro Kirk | H+R+RBI | Over | 1.5 | -102 | 49% | 2 | — | ✅ |
| Michael Harris II | H+R+RBI | Over | 1.5 | +115 | 45% | 3 | — | ✅ |
| Junior Caminero | RBI | Over | 0.5 | +144 | 40% | 1 | +12.4% | ✅ |
| Jose Siri | H+R+RBI | Under | 0.5 | +110 | 46% | 0 | — | ✅ |
| Caleb Durbin | RBI | Over | 0.5 | +199 | 32% | 0 | +0.3% | ❌ |
| Jonathan Aranda | H+R+RBI | Over | 1.5 | -134 | 56% | 0 | +3.9% | ❌ |
| Christian Walker | RBI | Over | 0.5 | +159 | 37% | 0 | +2.4% | ❌ |
| Alec Bohm | H+R+RBI | Under | 1.5 | +105 | 47% | 5 | — | ❌ |
| Fernando Tatis Jr. | RBI | Under | 0.5 | -216 | 66% | 1 | +1.1% | ❌ |
| Ryan Jeffers | RBI | Over | 0.5 | +202 | 32% | 0 | -0.3% | ❌ |
| Jake Burger | H+R+RBI | Over | 1.5 | +100 | 48% | 0 | -2.0% | ❌ |
| Daulton Varsho | Hits | Over | 0.5 | -163 | 61% | 2 | +1.6% | ✅ |
| Francisco Alvarez | H+R+RBI | Under | 1.5 | -159 | 59% | 1 | -0.5% | ✅ |
| Francisco Lindor | RBI | Under | 0.5 | -223 | 67% | 0 | +0.0% | ✅ |
| Daylen Lile | Hits | Over | 0.5 | -180 | 63% | 0 | — | ❌ |
| Dominic Canzone | RBI | Over | 0.5 | +205 | 32% | 1 | -2.2% | ✅ |
| Randy Arozarena | RBI | Over | 0.5 | +205 | 32% | 3 | -3.8% | ✅ |
| Heliot Ramos | H+R+RBI | Under | 1.5 | -179 | 62% | 0 | — | ✅ |
| Brice Turang | H+R+RBI | Under | 1.5 | -129 | 54% | 0 | — | ✅ |
| Henry Davis | H+R+RBI | Over | 0.5 | -103 | 49% | 0 | -1.9% | ❌ |
| Shohei Ohtani | RBI | Under | 0.5 | -183 | 62% | 0 | -1.0% | ✅ |
| Jake Bauers | Hits | Over | 0.5 | -155 | 59% | 1 | — | ✅ |
| Jac Caglianone | H+R+RBI | Under | 1.5 | -105 | 49% | 2 | +1.8% | ❌ |
| Willson Contreras | Hits | Under | 0.5 | +166 | 37% | 1 | +3.1% | ❌ |
| Royce Lewis | H+R+RBI | Over | 1.5 | +123 | 43% | 0 | +2.3% | ❌ |
| J.T. Realmuto | Hits | Under | 0.5 | +129 | 43% | 2 | — | ❌ |
| Yordan Alvarez | RBI | Over | 0.5 | +128 | 42% | 0 | +0.4% | ❌ |
| Yandy Diaz | RBI | Over | 0.5 | +157 | 37% | 0 | -7.9% | ❌ |
| Alec Bohm | RBI | Over | 0.5 | +148 | 39% | 1 | — | ✅ |
| Trent Grisham | H+R+RBI | Under | 1.5 | -172 | 61% | 0 | — | ✅ |
| Jackson Merrill | H+R+RBI | Under | 1.5 | -126 | 53% | 5 | +0.0% | ❌ |
| William Contreras | Hits | Over | 0.5 | -233 | 68% | 2 | — | ✅ |
| Jose Caballero | Hits | Over | 0.5 | +103 | 48% | 0 | — | ❌ |
| Miguel Vargas | RBI | Under | 0.5 | -219 | 66% | 0 | +0.0% | ✅ |
| Luis Garcia Jr. | Hits | Under | 0.5 | +127 | 43% | 1 | — | ❌ |
| Kody Clemens | RBI | Over | 0.5 | +191 | 33% | 1 | -4.3% | ✅ |
| Michael Massey | Hits | Under | 0.5 | +150 | 39% | 0 | +4.2% | ✅ |
| Miguel Vargas | H+R+RBI | Over | 1.5 | -109 | 50% | 1 | +0.0% | ❌ |
| Luis Garcia Jr. | RBI | Over | 0.5 | +211 | 31% | 2 | — | ✅ |
| Wyatt Langford | H+R+RBI | Over | 1.5 | -119 | 52% | 0 | +0.0% | ❌ |
| Tyler Stephenson | H+R+RBI | Under | 1.5 | -171 | 60% | 5 | — | ❌ |
| Jo Adell | RBI | Under | 0.5 | -154 | 58% | 3 | -1.8% | ❌ |
| Ozzie Albies | Hits | Over | 0.5 | -136 | 56% | 2 | — | ✅ |
| Andruw Monasterio | Hits | Under | 0.5 | +123 | 44% | 0 | +1.8% | ✅ |
| Kyle Schwarber | H+R+RBI | Over | 1.5 | -116 | 51% | 6 | — | ✅ |
| Javier Sanoja | Hits | Under | 0.5 | +151 | 39% | 0 | — | ✅ |
| Joe Mack | Hits | Over | 0.5 | -143 | 57% | 1 | — | ✅ |
| Bryce Harper | H+R+RBI | Over | 1.5 | -123 | 52% | 5 | -13.7% | ✅ |
| Ian Happ | Hits | Over | 0.5 | -129 | 55% | 0 | — | ❌ |
| Pete Alonso | H+R+RBI | Over | 1.5 | -112 | 50% | 2 | +4.8% | ✅ |
| Kody Clemens | H+R+RBI | Over | 1.5 | +111 | 45% | 3 | -0.5% | ✅ |
| Manny Machado | Hits | Under | 0.5 | +152 | 38% | 0 | +0.0% | ✅ |
| Jared Young | H+R+RBI | Over | 1.5 | +115 | 44% | 4 | +1.4% | ✅ |
| Mike Trout | RBI | Over | 0.5 | +204 | 31% | 1 | +1.7% | ✅ |
| Bryce Harper | Hits | Under | 0.5 | +154 | 38% | 1 | +23.9% | ❌ |
| Ryan Jeffers | H+R+RBI | Under | 1.5 | -135 | 55% | 3 | +0.0% | ❌ |
| Francisco Lindor | H+R+RBI | Over | 1.5 | -123 | 52% | 0 | +0.0% | ❌ |
| Willson Contreras | H+R+RBI | Under | 1.5 | +101 | 47% | 1 | +2.5% | ✅ |
| Zack Gelof | Hits | Under | 0.5 | +104 | 48% | 0 | +0.0% | ✅ |
| Dominic Canzone | H+R+RBI | Under | 1.5 | -144 | 56% | 1 | +1.4% | ✅ |
| Sal Stewart | Hits | Over | 0.5 | -247 | 69% | 3 | -1.1% | ✅ |
| Luis Robert Jr. | H+R+RBI | Under | 1.5 | -156 | 58% | 7 | -1.8% | ❌ |
| Donovan Walton | H+R+RBI | Over | 0.5 | -136 | 55% | 3 | -2.2% | ✅ |
| Elly De La Cruz | H+R+RBI | Under | 1.5 | -116 | 51% | 9 | +1.6% | ❌ |
| Jarren Duran | RBI | Over | 0.5 | +194 | 32% | 0 | +3.2% | ❌ |
| Junior Caminero | Hits | Under | 1.5 | -236 | 68% | 1 | +2.1% | ✅ |
| Jackson Chourio | H+R+RBI | Under | 1.5 | +106 | 46% | 0 | — | ✅ |
| Julio Rodriguez | H+R+RBI | Over | 1.5 | -113 | 50% | 0 | -1.7% | ❌ |
| Ronald Acuna Jr. | Hits | Under | 0.5 | +136 | 41% | 0 | — | ✅ |
| Spencer Jones | Hits | Over | 0.5 | +112 | 46% | 0 | — | ❌ |
| Drew Romo | H+R+RBI | Under | 0.5 | -102 | 48% | 3 | -2.0% | ❌ |
| Bryson Stott | Hits | Over | 0.5 | -170 | 61% | 0 | — | ❌ |
| Trea Turner | RBI | Over | 0.5 | +215 | 30% | 0 | -21.2% | ❌ |
| Ernie Clement | H+R+RBI | Over | 1.5 | +110 | 45% | 2 | — | ✅ |
| Trea Turner | H+R+RBI | Under | 1.5 | +105 | 46% | 4 | — | ❌ |
| Jake Bauers | RBI | Over | 0.5 | +187 | 33% | 2 | — | ✅ |
| Pete Alonso | Hits | Over | 0.5 | -216 | 66% | 2 | -0.1% | ✅ |
| Andrew Benintendi | RBI | Over | 0.5 | +200 | 31% | 1 | +0.7% | ✅ |
| Andrew Benintendi | Hits | Under | 0.5 | +114 | 45% | 1 | +0.0% | ❌ |
| Corey Seager | Hits | Over | 0.5 | -228 | 67% | 0 | +0.0% | ❌ |
| Jackson Merrill | Hits | Over | 0.5 | -188 | 63% | 2 | +0.0% | ✅ |
| JJ Bleday | Hits | Over | 0.5 | -188 | 63% | 4 | -2.9% | ✅ |
| Byron Buxton | Hits | Over | 0.5 | -206 | 65% | 0 | +0.0% | ❌ |
| Dillon Dingler | RBI | Over | 0.5 | +144 | 38% | 0 | -2.0% | ❌ |
| Javier Sanoja | RBI | Over | 0.5 | +206 | 30% | 0 | — | ❌ |
| Kyle Isbel | Hits | Over | 0.5 | -150 | 57% | 1 | -1.6% | ✅ |
| Cole Carrigg | RBI | Over | 0.5 | +185 | 33% | 0 | -2.7% | ❌ |
| Mickey Gasper | RBI | Over | 0.5 | +201 | 31% | 0 | -2.6% | ❌ |
| Luis Garcia Jr. | H+R+RBI | Over | 1.5 | +119 | 42% | 4 | — | ✅ |
| Gunnar Henderson | H+R+RBI | Over | 1.5 | +107 | 45% | 1 | +2.0% | ❌ |
| Geraldo Perdomo | RBI | Over | 0.5 | +228 | 28% | 0 | +23.8% | ❌ |
| Ryan Vilade | RBI | Over | 0.5 | +234 | 28% | 0 | — | ❌ |
| Nathan Church | H+R+RBI | Over | 1.5 | +114 | 43% | 3 | — | ✅ |
| Daylen Lile | H+R+RBI | Over | 1.5 | +115 | 43% | 1 | — | ❌ |
| Tim Tawa | RBI | Over | 0.5 | +230 | 28% | 2 | +13.4% | ✅ |
| Jac Caglianone | RBI | Over | 0.5 | +173 | 34% | 0 | -1.4% | ❌ |
| George Springer | RBI | Over | 0.5 | +215 | 30% | 1 | — | ✅ |
| Dominic Canzone | Hits | Over | 0.5 | -181 | 62% | 0 | -2.5% | ❌ |
| Luis Arraez | H+R+RBI | Under | 1.5 | +118 | 42% | 2 | +21.1% | ❌ |
| Colt Keith | Hits | Under | 0.5 | +160 | 37% | 0 | +7.9% | ✅ |
| Shohei Ohtani | H+R+RBI | Under | 1.5 | +109 | 44% | 0 | — | ✅ |
| Leody Taveras | H+R+RBI | Under | 0.5 | +135 | 39% | 1 | +0.4% | ❌ |
| JJ Wetherholt | RBI | Over | 0.5 | +203 | 30% | 1 | -15.8% | ✅ |
| Junior Caminero | H+R+RBI | Under | 1.5 | +116 | 43% | 2 | +0.5% | ❌ |
| Brett Baty | RBI | Over | 0.5 | +227 | 28% | 0 | +2.2% | ❌ |
| Bryce Harper | RBI | Over | 0.5 | +170 | 34% | 3 | -22.9% | ✅ |
| Brady House | H+R+RBI | Under | 0.5 | +138 | 39% | 0 | — | ✅ |
| Tyler Stephenson | Hits | Over | 0.5 | -147 | 57% | 2 | -1.4% | ✅ |
| Ceddanne Rafaela | RBI | Over | 0.5 | +179 | 33% | 0 | -2.1% | ❌ |
| Coby Mayo | Hits | Under | 0.5 | +117 | 44% | 2 | -2.2% | ❌ |
| J.T. Realmuto | RBI | Over | 0.5 | +205 | 30% | 1 | -18.7% | ✅ |
| Vinnie Pasquantino | RBI | Over | 0.5 | +209 | 30% | 0 | +1.6% | ❌ |
| Ian Happ | RBI | Over | 0.5 | +226 | 28% | 0 | — | ❌ |
| Joc Pederson | Hits | Under | 0.5 | +132 | 41% | 0 | -2.5% | ✅ |
| Mickey Gasper | Hits | Over | 0.5 | -160 | 58% | 1 | +0.0% | ✅ |
| Willson Contreras | RBI | Over | 0.5 | +141 | 38% | 0 | -4.0% | ❌ |
| Evan Carter | Hits | Over | 0.5 | -142 | 56% | 0 | -1.5% | ❌ |
| Ryan Weathers | Ks (P) | Over | 5.5 | +104 | 47% | 3 | — | ❌ |
| Ronald Acuna Jr. | RBI | Over | 0.5 | +219 | 29% | 0 | — | ❌ |
| Tyler Stephenson | RBI | Over | 0.5 | +225 | 28% | 3 | -4.1% | ✅ |
| Ryan Vilade | Hits | Under | 0.5 | +123 | 42% | 0 | — | ✅ |
| Royce Lewis | RBI | Over | 0.5 | +208 | 30% | 0 | +1.6% | ❌ |
| Griffin Conine | Hits | Under | 0.5 | +160 | 36% | 0 | — | ✅ |
| Luis Campusano | RBI | Over | 0.5 | +210 | 29% | 0 | — | ❌ |
| Moises Ballesteros | Hits | Under | 0.5 | +122 | 42% | 2 | -9.4% | ❌ |
| Jackson Merrill | RBI | Over | 0.5 | +181 | 32% | 2 | -2.1% | ✅ |
| Owen Caissie | Hits | Under | 0.5 | +106 | 46% | 1 | — | ❌ |
| Mookie Betts | Hits | Under | 0.5 | +181 | 33% | 0 | -5.1% | ✅ |
| Jacob Lopez | Ks (P) | Over | 4.5 | -125 | 53% | 9 | +0.0% | ✅ |
| Gunnar Henderson | Hits | Under | 0.5 | +142 | 39% | 1 | +1.3% | ❌ |
| Luis Rengifo | RBI | Over | 0.5 | +239 | 26% | 0 | +0.0% | ❌ |
| Tommy Edman | Hits | Under | 0.5 | +144 | 38% | 0 | -7.2% | ✅ |
| Drake Baldwin | RBI | Over | 0.5 | +197 | 30% | 0 | — | ❌ |
| Cam Smith | RBI | Over | 0.5 | +197 | 30% | 0 | +1.0% | ❌ |
| Ceddanne Rafaela | Hits | Over | 1.5 | +189 | 32% | 1 | -1.4% | ❌ |
| Kevin McGonigle | RBI | Over | 0.5 | +182 | 32% | 0 | -7.5% | ❌ |
| Munetaka Murakami | RBI | Over | 0.5 | +156 | 35% | 0 | +2.4% | ❌ |
| Carter Jensen | RBI | Over | 0.5 | +212 | 29% | 0 | -8.2% | ❌ |
| Luis Castillo | Ks (P) | Under | 4.5 | +101 | 48% | 3 | +5.3% | ✅ |
| Andruw Monasterio | RBI | Over | 0.5 | +204 | 29% | 0 | -2.2% | ❌ |
| Jake Mangum | Hits | Under | 0.5 | +116 | 43% | 0 | -2.3% | ✅ |
| Taylor Ward | RBI | Over | 0.5 | +250 | 25% | 0 | +2.6% | ❌ |
| Yordan Alvarez | Hits | Over | 1.5 | +187 | 32% | 0 | +2.9% | ❌ |
| Christian Scott | Ks (P) | Over | 6.5 | +121 | 43% | 6 | -2.2% | ❌ |
| Xander Bogaerts | RBI | Over | 0.5 | +232 | 27% | 0 | -3.5% | ❌ |
| Julio Rodriguez | RBI | Over | 0.5 | +174 | 32% | 0 | -2.5% | ❌ |
| George Springer | Hits | Under | 0.5 | +140 | 39% | 3 | — | ❌ |
| Otto Lopez | RBI | Over | 0.5 | +191 | 30% | 2 | — | ✅ |
| Ty France | Hits | Under | 0.5 | +159 | 36% | 1 | +2.0% | ❌ |
| Logan Henderson | Ks (P) | Under | 6.5 | -120 | 52% | 4 | — | ✅ |
| Kyle Karros | RBI | Over | 0.5 | +209 | 28% | 0 | +9.6% | ❌ |
| William Contreras | RBI | Over | 0.5 | +181 | 31% | 1 | — | ✅ |
| Matt Olson | RBI | Over | 0.5 | +176 | 32% | 0 | — | ❌ |
| JJ Bleday | RBI | Over | 0.5 | +202 | 29% | 3 | -4.1% | ✅ |
| Dillon Dingler | Hits | Under | 0.5 | +201 | 31% | 1 | +5.2% | ❌ |
| Jared Young | RBI | Over | 0.5 | +202 | 29% | 0 | +3.1% | ❌ |
| Jarren Duran | Hits | Under | 0.5 | +136 | 39% | 0 | +0.0% | ✅ |
| Ezequiel Duran | Hits | Under | 0.5 | +150 | 36% | 0 | +2.0% | ✅ |
| Otto Lopez | Hits | Over | 1.5 | +181 | 32% | 1 | — | ❌ |
| Brandon Nimmo | Hits | Under | 0.5 | +188 | 31% | 0 | -2.4% | ✅ |
| Oneil Cruz | RBI | Over | 0.5 | +271 | 36% | 2 | +9.1% | ✅ |
| Brooks Lee | RBI | Over | 0.5 | +297 | 32% | 1 | +0.5% | ✅ |
| Jose Caballero | RBI | Over | 0.5 | +393 | 25% | 0 | — | ❌ |
| Mauricio Dubon | RBI | Over | 0.5 | +338 | 27% | 0 | — | ❌ |
| Cole Young | RBI | Over | 0.5 | +275 | 31% | 0 | -4.8% | ❌ |
| Cole Carrigg | Hits | Under | 1.5 | -258 | 84% | 0 | — | ✅ |
| Esteury Ruiz | RBI | Under | 0.5 | -318 | 88% | 0 | — | ✅ |
| Marcus Semien | RBI | Over | 0.5 | +291 | 29% | 1 | +2.6% | ✅ |
| Jordan Walker | Hits | Over | 0.5 | -252 | 80% | 0 | -21.1% | ❌ |
| Jung Hoo Lee | RBI | Over | 0.5 | +258 | 31% | 0 | +2.6% | ❌ |
| Esmerlyn Valdez | RBI | Over | 0.5 | +273 | 30% | 0 | +7.5% | ❌ |
| Gabriel Moreno | Hits | Over | 0.5 | -279 | 81% | 1 | — | ✅ |
| Chase Meidroth | RBI | Over | 0.5 | +289 | 28% | 0 | +2.9% | ❌ |
| Nick Gonzales | RBI | Over | 0.5 | +305 | 27% | 0 | -7.1% | ❌ |
| Zack Gelof | RBI | Over | 0.5 | +305 | 27% | 0 | +2.5% | ❌ |
| Freddie Freeman | Hits | Over | 0.5 | -252 | 76% | 1 | +0.1% | ✅ |
| Richie Palacios | RBI | Over | 0.5 | +273 | 29% | 0 | +4.8% | ❌ |
| Bryan Reynolds | RBI | Over | 0.5 | +277 | 28% | 0 | +2.2% | ❌ |
| TJ Rumfield | Hits | Over | 0.5 | -252 | 76% | 0 | +1.5% | ❌ |
| Connor Norby | RBI | Under | 0.5 | -299 | 79% | 1 | — | ❌ |
| Jeremy Pena | Hits | Under | 1.5 | -258 | 76% | 1 | -0.9% | ✅ |
| Tyler O'Neill | RBI | Under | 0.5 | -315 | 79% | 0 | -1.5% | ✅ |
| Myles Straw | RBI | Under | 0.5 | -478 | 86% | 0 | — | ✅ |
| Xavier Edwards | Hits | Over | 0.5 | -268 | 75% | 1 | — | ✅ |
| Jac Caglianone | Hits | Over | 0.5 | -258 | 75% | 1 | +0.1% | ✅ |
| Nathaniel Lowe | Hits | Under | 1.5 | -263 | 75% | 1 | -0.2% | ✅ |
| Leody Taveras | RBI | Over | 0.5 | +319 | 25% | 0 | +5.8% | ❌ |
| Zach McKinstry | RBI | Under | 0.5 | -327 | 79% | 0 | -1.2% | ✅ |
| Jose Siri | RBI | Under | 0.5 | -321 | 78% | 0 | -2.0% | ✅ |
| Ke'Bryan Hayes | RBI | Under | 0.5 | -485 | 85% | 0 | +0.8% | ✅ |
| Andrew Vaughn | RBI | Under | 0.5 | -264 | 74% | 0 | — | ✅ |
| Jakob Marsee | RBI | Under | 0.5 | -335 | 79% | 1 | — | ❌ |
| Trevor Larnach | RBI | Over | 0.5 | +311 | 25% | 0 | -2.8% | ❌ |
| Colt Keith | RBI | Under | 0.5 | -350 | 80% | 0 | -2.6% | ✅ |
| Jorbit Vivas | RBI | Under | 0.5 | -467 | 84% | 0 | — | ✅ |
| Jackson Chourio | Hits | Over | 0.5 | -262 | 74% | 0 | — | ❌ |
| Alec Bohm | Hits | Over | 0.5 | -264 | 74% | 2 | — | ✅ |
| Dylan Crews | RBI | Under | 0.5 | -321 | 78% | 1 | — | ❌ |
| Derek Hill | RBI | Under | 0.5 | -365 | 80% | 1 | +4.2% | ❌ |
| Bo Bichette | Hits | Over | 0.5 | -270 | 74% | 2 | -0.1% | ✅ |
| Evan Carter | RBI | Under | 0.5 | -319 | 77% | 0 | +1.8% | ✅ |
| Donovan Walton | RBI | Under | 0.5 | -479 | 84% | 1 | +0.9% | ❌ |
| Teoscar Hernandez | RBI | Under | 0.5 | -261 | 73% | 1 | -2.1% | ❌ |
| Matt McLain | RBI | Over | 0.5 | +305 | 25% | 2 | -4.7% | ✅ |
| Ozzie Albies | RBI | Over | 0.5 | +267 | 28% | 0 | — | ❌ |
| Jake Cronenworth | RBI | Under | 0.5 | -341 | 78% | 2 | +0.0% | ❌ |
| Cedric Mullins | RBI | Under | 0.5 | -259 | 73% | 0 | +3.3% | ✅ |
| Austin Wells | RBI | Under | 0.5 | -509 | 84% | 1 | — | ❌ |
| Austin Riley | RBI | Over | 0.5 | +279 | 26% | 0 | — | ❌ |
| Lawrence Butler | RBI | Under | 0.5 | -392 | 80% | 1 | +1.5% | ❌ |
| Joe Mack | RBI | Under | 0.5 | -258 | 72% | 0 | — | ✅ |
| Daulton Varsho | RBI | Under | 0.5 | -348 | 77% | 1 | -0.8% | ❌ |
| Coby Mayo | RBI | Under | 0.5 | -291 | 74% | 0 | -0.7% | ✅ |
| Jacob Young | RBI | Under | 0.5 | -373 | 78% | 0 | — | ✅ |
| Nick Loftin | RBI | Under | 0.5 | -330 | 76% | 0 | +2.5% | ✅ |
| Danny Jansen | RBI | Under | 0.5 | -342 | 76% | 0 | +3.2% | ✅ |
| Michael Massey | RBI | Under | 0.5 | -312 | 74% | 0 | -0.2% | ✅ |
| Dane Myers | RBI | Under | 0.5 | -509 | 82% | 0 | -1.3% | ✅ |
| Kyle Tucker | RBI | Under | 0.5 | -273 | 72% | 2 | +2.2% | ❌ |
| Tommy Edman | RBI | Under | 0.5 | -298 | 73% | 0 | -3.4% | ✅ |
| Joc Pederson | RBI | Under | 0.5 | -283 | 72% | 0 | +0.4% | ✅ |
| Gavin Sheets | RBI | Under | 0.5 | -339 | 75% | 0 | +0.7% | ✅ |
| Michael Harris II | RBI | Under | 0.5 | -277 | 71% | 1 | — | ❌ |
| Trea Turner | Hits | Over | 0.5 | -271 | 71% | 2 | — | ✅ |
| Joey Ortiz | RBI | Under | 0.5 | -355 | 76% | 0 | — | ✅ |
| Edmundo Sosa | RBI | Under | 0.5 | -292 | 72% | 2 | — | ❌ |
| Gunnar Henderson | RBI | Under | 0.5 | -315 | 74% | 0 | -0.9% | ✅ |
| Francisco Alvarez | RBI | Under | 0.5 | -321 | 74% | 0 | -0.5% | ✅ |
| Brett Sullivan | RBI | Under | 0.5 | -290 | 72% | 0 | +0.2% | ✅ |
| Daylen Lile | RBI | Under | 0.5 | -265 | 70% | 0 | — | ✅ |
| Owen Caissie | RBI | Under | 0.5 | -270 | 70% | 0 | — | ✅ |
| Josh Lowe | RBI | Over | 0.5 | +283 | 25% | 0 | — | ❌ |
| Yainer Diaz | RBI | Under | 0.5 | -278 | 71% | 1 | -0.1% | ❌ |
| Spencer Torkelson | RBI | Under | 0.5 | -257 | 69% | 0 | +0.8% | ✅ |
| Jeff McNeil | RBI | Over | 0.5 | +290 | 25% | 0 | -2.5% | ❌ |
| Spencer Jones | RBI | Over | 0.5 | +324 | 22% | 0 | — | ❌ |
| Brady House | RBI | Over | 0.5 | +251 | 27% | 0 | — | ❌ |
| Jonah Heim | RBI | Over | 0.5 | +268 | 25% | 1 | -1.3% | ✅ |
| Drew Romo | RBI | Over | 0.5 | +301 | 23% | 0 | +0.5% | ❌ |
| Ernie Clement | RBI | Over | 0.5 | +259 | 26% | 0 | — | ❌ |
| Henry Bolte | RBI | Over | 0.5 | +316 | 22% | 0 | +2.5% | ❌ |
| A.J. Ewing | RBI | Over | 0.5 | +267 | 25% | 0 | +0.0% | ❌ |
| Jazz Chisholm Jr. | RBI | Over | 0.5 | +261 | 25% | 0 | — | ❌ |
| Henry Davis | RBI | Over | 0.5 | +308 | 22% | 0 | -6.2% | ❌ |
| Tristan Peters | RBI | Over | 0.5 | +303 | 22% | 1 | +0.0% | ✅ |
| Tyrone Taylor | RBI | Over | 0.5 | +309 | 22% | 1 | +14.2% | ✅ |
| Moises Ballesteros | RBI | Over | 0.5 | +256 | 25% | 1 | +13.4% | ✅ |
| Jackson Holliday | RBI | Over | 0.5 | +286 | 23% | 0 | -3.3% | ❌ |
| Luke Keaschall | RBI | Over | 0.5 | +303 | 22% | 2 | +0.0% | ✅ |
| Sam Antonacci | RBI | Over | 0.5 | +266 | 24% | 1 | +0.6% | ✅ |
| Bryan Torres | RBI | Over | 0.5 | +264 | 24% | 0 | — | ❌ |
| Mike Yastrzemski | RBI | Over | 0.5 | +347 | 19% | 0 | — | ❌ |
| Jake Mangum | RBI | Over | 0.5 | +346 | 19% | 0 | -4.3% | ❌ |
| Heliot Ramos | RBI | Over | 0.5 | +259 | 24% | 0 | — | ❌ |
| Carlos Cortes | RBI | Over | 0.5 | +267 | 23% | 0 | +0.8% | ❌ |
| Kyle Isbel | RBI | Over | 0.5 | +262 | 23% | 1 | -5.7% | ✅ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Atlanta Braves @ Milwaukee Brewers | **YRFI** | High | 62% | 47% | ✅ |
| Washington Nationals @ Miami Marlins | **NRFI** | High | 67% | 53% | ❌ |
| St. Louis Cardinals @ Philadelphia Phillies | **YRFI** | High | 78% | 52% | ✅ |
| Los Angeles Angels @ Texas Rangers | **NRFI** | High | 64% | 47% | ❌ |
| Athletics @ Houston Astros | **YRFI** | High | 59% | 50% | ❌ |
| New York Mets @ Chicago White Sox | **YRFI** | High | 64% | 48% | ✅ |
| Chicago Cubs @ Seattle Mariners | **YRFI** | High | 69% | 47% | ✅ |
| San Francisco Giants @ Boston Red Sox | **YRFI** | High | 58% | 43% | ✅ |
| Cincinnati Reds @ Arizona Diamondbacks | **YRFI** | High | 62% | 50% | ✅ |
| Cleveland Guardians @ Colorado Rockies | **YRFI** | High | 72% | 53% | ❌ |
| Minnesota Twins @ San Diego Padres | **YRFI** | High | 60% | 50% | ✅ |
| Pittsburgh Pirates @ Los Angeles Dodgers | **YRFI** | Medium | 50% | 46% | ✅ |
| Toronto Blue Jays @ New York Yankees | **NRFI** | Low | 66% | 62% | ❌ |
| Tampa Bay Rays @ Baltimore Orioles | **YRFI** | Low | 52% | 48% | ❌ |
| Detroit Tigers @ Kansas City Royals | **NRFI** | Coin flip | 51% | 51% | ✅ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Yordan Alvarez | Athletics @ Houston Astros | 28% | ❌ |
| 2 | Max Muncy | Pittsburgh Pirates @ Los Angeles Dodgers | 28% | ❌ |
| 3 | Shohei Ohtani | Pittsburgh Pirates @ Los Angeles Dodgers | 27% | ❌ |
| 4 | Matt Olson | Atlanta Braves @ Milwaukee Brewers | 27% | ❌ |
| 5 | Kyle Schwarber | St. Louis Cardinals @ Philadelphia Phillies | 26% | ✅ |
| 6 | Jordan Walker | St. Louis Cardinals @ Philadelphia Phillies | 25% | ❌ |
| 7 | Mickey Moniak | Cleveland Guardians @ Colorado Rockies | 25% | ✅ |
| 8 | Joc Pederson | Los Angeles Angels @ Texas Rangers | 24% | ❌ |
| 9 | Kazuma Okamoto | Toronto Blue Jays @ New York Yankees | 23% | ❌ |
| 10 | Munetaka Murakami | New York Mets @ Chicago White Sox | 22% | ❌ |

*2 homered · model expected 2.6*

### 2026-08-21 — bets 6-3 (+1.34u) · props 353-339 · NRFI 9-6 · HR 3-7

**Locked bets**

| Market | Pick | Line | Price | Score | CLV | Result |
|---|---|---|---|---|---|---|
| Moneyline | Boston Red Sox ML | — | -178 | 9.5 | +6.6% | ✅ +0.56u |
| Total | Under 11.0 | 11.0 | +100 | 9.5 | -1.0% | ✅ +1.00u |
| Moneyline | Los Angeles Dodgers ML | — | -230 | 9.5 | +3.1% | ✅ +0.43u |
| Moneyline | Chicago Cubs ML | — | -108 | 9.5 | -3.7% | ❌ -1.00u |
| F5 Total | F5 Over 2.5 | 2.5 | -160 | 7.4 | — | ❌ -1.00u |
| Total | Over 6.5 | 6.5 | -102 | 6.5 | — | ❌ -1.00u |
| Moneyline | Cleveland Guardians ML | — | -157 | 5.7 | -4.0% | ✅ +0.64u |
| F5 Total | F5 Over 4.5 | 4.5 | -113 | 5.6 | -9.4% | ✅ +0.88u |
| F5 Total | F5 Over 4.5 | 4.5 | -120 | 5.4 | -1.9% | ✅ +0.83u |

**Player props**

| Player | Mkt | Call | Line | Price | Model | Actual | CLV | Result |
|---|---|---|---|---|---|---|---|---|
| Tanner Gordon | Ks (P) | Over | 3.5 | +122 | 78% | 2 | -2.2% | ❌ |
| Sean Manaea | Ks (P) | Over | 5.5 | -132 | 79% | 4 | +2.5% | ❌ |
| Dane Myers | Hits | Under | 0.5 | +163 | 54% | 1 | -3.7% | ❌ |
| Reid Detmers | Ks (P) | Over | 6.5 | +106 | 61% | 5 | +7.4% | ❌ |
| Jose Tena | Hits | Under | 0.5 | +127 | 58% | 0 | — | ✅ |
| Jorge Mateo | Hits | Under | 0.5 | +115 | 61% | 0 | -4.0% | ✅ |
| Nick Loftin | Hits | Under | 0.5 | +124 | 58% | 0 | +6.2% | ✅ |
| Sonny Gray | Ks (P) | Under | 5.5 | -122 | 66% | 6 | +1.1% | ❌ |
| Brenton Doyle | Hits | Under | 0.5 | +118 | 59% | 0 | -4.8% | ✅ |
| Jakob Marsee | Hits | Under | 0.5 | +157 | 49% | 1 | +8.4% | ❌ |
| Luis Rengifo | Hits | Under | 0.5 | +160 | 49% | 2 | -1.1% | ❌ |
| Yoshinobu Yamamoto | Ks (P) | Under | 6.5 | +116 | 53% | 9 | -4.4% | ❌ |
| Myles Straw | Hits | Under | 0.5 | -115 | 66% | 0 | +5.3% | ✅ |
| Jose Siri | Hits | Under | 0.5 | -115 | 66% | 1 | +1.2% | ❌ |
| Colson Montgomery | Hits | Over | 0.5 | -143 | 72% | 1 | +2.8% | ✅ |
| Connor Norby | Hits | Under | 0.5 | +126 | 54% | 1 | — | ❌ |
| Esteury Ruiz | Hits | Under | 0.5 | -106 | 62% | 1 | — | ❌ |
| Masyn Winn | Hits | Over | 0.5 | -151 | 73% | 0 | — | ❌ |
| Alejandro Kirk | Hits | Under | 0.5 | +184 | 43% | 1 | +15.9% | ❌ |
| Chase Meidroth | Hits | Over | 0.5 | -194 | 80% | 0 | -1.3% | ❌ |
| Jonah Heim | Hits | Under | 0.5 | +120 | 55% | 0 | +5.3% | ✅ |
| Ke'Bryan Hayes | Hits | Under | 0.5 | -112 | 64% | 1 | -4.4% | ❌ |
| Mickey Moniak | Hits | Under | 0.5 | +158 | 47% | 0 | +0.4% | ✅ |
| Heriberto Hernandez | Hits | Under | 0.5 | +140 | 50% | 0 | +5.7% | ✅ |
| Nick Allen | H+R+RBI | Under | 0.5 | +124 | 59% | 1 | +4.7% | ❌ |
| Carter Jensen | Hits | Under | 0.5 | +115 | 56% | 1 | +0.5% | ❌ |
| Esteury Ruiz | H+R+RBI | Under | 0.5 | +129 | 57% | 1 | — | ❌ |
| Nick Allen | Hits | Under | 0.5 | -102 | 60% | 0 | +5.9% | ✅ |
| Jacob Misiorowski | Ks (P) | Under | 9.5 | -128 | 63% | 6 | — | ✅ |
| Michael Conforto | Hits | Under | 0.5 | -121 | 65% | 0 | +0.0% | ✅ |
| Alec Burleson | RBI | Over | 0.5 | +219 | 41% | 0 | — | ❌ |
| Yoshinobu Yamamoto | Ks (P) | Under | 7.5 | -149 | 67% | 9 | +0.3% | ❌ |
| Cal Raleigh | Hits | Under | 0.5 | +117 | 55% | 1 | +4.8% | ❌ |
| Luis Robert Jr. | Hits | Under | 0.5 | +124 | 53% | 1 | -0.9% | ❌ |
| Freddy Peralta | Ks (P) | Under | 5.5 | -142 | 66% | 6 | +1.1% | ❌ |
| Angel Martinez | Hits | Under | 1.5 | -215 | 80% | 0 | — | ✅ |
| Dane Myers | H+R+RBI | Under | 1.5 | -125 | 72% | 1 | -1.4% | ✅ |
| Drake Baldwin | Hits | Over | 0.5 | -134 | 67% | 0 | — | ❌ |
| Mauricio Dubon | Hits | Over | 0.5 | -125 | 65% | 2 | — | ✅ |
| Pedro Pages | Hits | Under | 0.5 | -146 | 69% | 1 | -3.2% | ❌ |
| Cam Smith | Hits | Under | 0.5 | +142 | 48% | 0 | +0.4% | ✅ |
| Matt Olson | Hits | Over | 0.5 | -113 | 62% | 1 | — | ✅ |
| Trevor Rogers | Ks (P) | Under | 4.5 | -106 | 57% | 6 | +1.8% | ❌ |
| Daulton Varsho | Hits | Under | 0.5 | +150 | 46% | 1 | +0.0% | ❌ |
| Caleb Durbin | Hits | Under | 0.5 | +168 | 43% | 1 | -2.2% | ❌ |
| Eduardo Rodriguez | Ks (P) | Under | 5.5 | -130 | 62% | 4 | +5.0% | ✅ |
| Josh Naylor | Hits | Over | 0.5 | -194 | 76% | 1 | -1.1% | ✅ |
| Myles Straw | H+R+RBI | Under | 0.5 | +105 | 60% | 0 | +6.0% | ✅ |
| Jorge Mateo | H+R+RBI | Under | 1.5 | -162 | 76% | 1 | -1.4% | ✅ |
| Nick Lodolo | Ks (P) | Under | 3.5 | -104 | 56% | 2 | +0.0% | ✅ |
| Zach Neto | Hits | Over | 0.5 | -163 | 71% | 1 | -0.7% | ✅ |
| Jake Bauers | H+R+RBI | Over | 0.5 | -153 | 74% | 0 | — | ❌ |
| Jordan Walker | RBI | Over | 0.5 | +197 | 41% | 2 | -17.5% | ✅ |
| Sal Stewart | RBI | Over | 0.5 | +187 | 42% | 0 | +0.3% | ❌ |
| Jake Bauers | Hits | Over | 0.5 | -118 | 61% | 0 | — | ❌ |
| Jakob Marsee | H+R+RBI | Under | 1.5 | -111 | 64% | 2 | +5.6% | ❌ |
| Michael Harris II | Hits | Over | 0.5 | -149 | 68% | 2 | — | ✅ |
| Isaac Collins | Hits | Under | 0.5 | +114 | 53% | 1 | +3.9% | ❌ |
| Matt Olson | H+R+RBI | Over | 0.5 | -148 | 72% | 1 | — | ✅ |
| Brandon Marsh | Hits | Over | 0.5 | -183 | 73% | 2 | +4.8% | ✅ |
| Rafael Devers | Hits | Over | 0.5 | -174 | 72% | 1 | +8.1% | ✅ |
| Daulton Varsho | H+R+RBI | Under | 1.5 | -113 | 64% | 1 | -0.4% | ✅ |
| Sean Burke | Ks (P) | Over | 6.5 | +112 | 51% | 4 | +1.9% | ❌ |
| Ian Happ | Hits | Over | 0.5 | -133 | 64% | 2 | +1.6% | ✅ |
| Salvador Perez | Hits | Under | 0.5 | +143 | 46% | 1 | +0.4% | ❌ |
| Jesus Luzardo | Ks (P) | Under | 7.5 | -142 | 63% | 9 | +0.0% | ❌ |
| Mike Trout | Hits | Over | 0.5 | -174 | 71% | 0 | -1.5% | ❌ |
| Everson Pereira | Hits | Over | 0.5 | +114 | 52% | 1 | +9.6% | ✅ |
| Luis Arraez | Hits | Over | 1.5 | +189 | 38% | 3 | +20.4% | ✅ |
| Jose Ramirez | Hits | Under | 1.5 | -190 | 73% | 0 | +1.2% | ✅ |
| Pete Alonso | Hits | Over | 0.5 | -229 | 77% | 2 | -0.9% | ✅ |
| Nick Loftin | H+R+RBI | Under | 1.5 | -158 | 72% | 0 | +5.8% | ✅ |
| Jackson Chourio | Hits | Over | 0.5 | -193 | 73% | 1 | — | ✅ |
| Jonathan Aranda | RBI | Over | 0.5 | +213 | 38% | 0 | — | ❌ |
| Spencer Horwitz | Hits | Under | 0.5 | +119 | 50% | 0 | +0.9% | ✅ |
| Jose Tena | H+R+RBI | Under | 1.5 | -153 | 71% | 0 | — | ✅ |
| Noah Cameron | Ks (P) | Over | 5.5 | -106 | 55% | 2 | -6.6% | ❌ |
| Evan Carter | Hits | Under | 0.5 | -130 | 62% | 2 | +1.0% | ❌ |
| Colson Montgomery | H+R+RBI | Over | 1.5 | +124 | 52% | 3 | +5.2% | ✅ |
| Dillon Dingler | Hits | Under | 0.5 | +190 | 38% | 0 | +7.0% | ✅ |
| Taylor Ward | Hits | Over | 0.5 | -177 | 70% | 0 | +3.1% | ❌ |
| Dylan Beavers | Hits | Over | 0.5 | -124 | 61% | 1 | -3.4% | ✅ |
| Connor Norby | H+R+RBI | Under | 1.5 | -139 | 67% | 1 | — | ✅ |
| Seiya Suzuki | RBI | Over | 0.5 | +205 | 38% | 0 | +0.0% | ❌ |
| Jake Rogers | Hits | Under | 0.5 | -124 | 61% | 1 | -5.4% | ❌ |
| Yordan Alvarez | Hits | Over | 1.5 | +178 | 39% | 2 | -2.8% | ✅ |
| Ozzie Albies | H+R+RBI | Over | 0.5 | -131 | 66% | 0 | — | ❌ |
| Zack Gelof | H+R+RBI | Over | 1.5 | +126 | 51% | 0 | -2.6% | ❌ |
| Yandy Diaz | Hits | Over | 1.5 | +197 | 37% | 0 | +1.0% | ❌ |
| Elly De La Cruz | Hits | Over | 0.5 | -234 | 77% | 0 | -1.3% | ❌ |
| Fernando Tatis Jr. | Hits | Over | 0.5 | -224 | 76% | 3 | +2.8% | ✅ |
| Nick Gonzales | Hits | Over | 0.5 | -185 | 71% | 2 | -3.6% | ✅ |
| Jose Ramirez | H+R+RBI | Under | 2.5 | -128 | 64% | 0 | +2.0% | ✅ |
| Drake Baldwin | H+R+RBI | Over | 0.5 | -175 | 73% | 0 | — | ❌ |
| Colson Montgomery | RBI | Over | 0.5 | +214 | 37% | 1 | +5.4% | ✅ |
| Randal Grichuk | H+R+RBI | Under | 1.5 | -122 | 63% | 4 | +1.4% | ❌ |
| Gleyber Torres | RBI | Over | 0.5 | +249 | 33% | 0 | +0.3% | ❌ |
| Oneil Cruz | Hits | Over | 0.5 | -135 | 63% | 0 | -4.0% | ❌ |
| Brandon Lowe | Hits | Over | 0.5 | -145 | 64% | 2 | -1.4% | ✅ |
| Elias Diaz | H+R+RBI | Under | 0.5 | +116 | 53% | 1 | +6.9% | ❌ |
| Daulton Varsho | RBI | Under | 0.5 | -227 | 79% | 0 | -1.7% | ✅ |
| Brandon Lowe | RBI | Over | 0.5 | +246 | 33% | 0 | +2.7% | ❌ |
| Freddie Freeman | Hits | Over | 0.5 | -236 | 76% | 0 | -1.3% | ❌ |
| Jackson Merrill | Hits | Over | 0.5 | -237 | 76% | 0 | -0.2% | ❌ |
| Cal Raleigh | H+R+RBI | Under | 1.5 | -142 | 67% | 5 | +2.8% | ❌ |
| Angel Martinez | H+R+RBI | Under | 2.5 | -145 | 68% | 0 | — | ✅ |
| Jake McCarthy | RBI | Over | 0.5 | +213 | 36% | 0 | +3.0% | ❌ |
| Gary Sanchez | Hits | Over | 0.5 | -110 | 57% | 0 | — | ❌ |
| Heriberto Hernandez | H+R+RBI | Under | 1.5 | -120 | 62% | 0 | +6.9% | ✅ |
| Mauricio Dubon | H+R+RBI | Over | 0.5 | -147 | 68% | 2 | — | ✅ |
| Brenton Doyle | H+R+RBI | Under | 1.5 | -161 | 70% | 0 | -1.7% | ✅ |
| Gabriel Moreno | RBI | Over | 0.5 | +173 | 41% | 1 | +6.2% | ✅ |
| Zach Neto | H+R+RBI | Over | 1.5 | +112 | 53% | 1 | +0.5% | ❌ |
| Javier Sanoja | Hits | Under | 0.5 | +146 | 44% | 2 | — | ❌ |
| Javier Baez | Hits | Over | 0.5 | -173 | 68% | 1 | -1.5% | ✅ |
| Jordan Walker | H+R+RBI | Over | 1.5 | -104 | 57% | 7 | — | ✅ |
| Henry Davis | Hits | Under | 0.5 | -128 | 60% | 0 | +2.0% | ✅ |
| Mike Yastrzemski | Hits | Over | 0.5 | +131 | 47% | 2 | — | ✅ |
| Austin Riley | Hits | Over | 0.5 | -108 | 56% | 0 | — | ❌ |
| Ozzie Albies | Hits | Over | 0.5 | -109 | 56% | 0 | — | ❌ |
| Emerson Hancock | Ks (P) | Under | 4.5 | +126 | 46% | 6 | +0.0% | ❌ |
| Chase Meidroth | H+R+RBI | Over | 1.5 | +103 | 55% | 0 | -1.9% | ❌ |
| Austin Riley | H+R+RBI | Over | 0.5 | -129 | 63% | 0 | — | ❌ |
| Miguel Vargas | Hits | Over | 0.5 | -213 | 73% | 2 | -1.4% | ✅ |
| Isaac Collins | H+R+RBI | Under | 1.5 | -164 | 70% | 1 | +3.1% | ✅ |
| Javier Sanoja | H+R+RBI | Under | 1.5 | -134 | 64% | 5 | — | ❌ |
| Jose Siri | H+R+RBI | Under | 0.5 | +104 | 55% | 2 | +0.0% | ❌ |
| Jordan Walker | Hits | Over | 0.5 | -219 | 74% | 3 | — | ✅ |
| Cam Schlittler | Ks (P) | Under | 6.5 | -115 | 56% | 4 | -1.2% | ✅ |
| Michael Massey | Hits | Under | 0.5 | +134 | 46% | 1 | +0.0% | ❌ |
| Josh Bell | Hits | Over | 0.5 | -188 | 70% | 0 | +0.0% | ❌ |
| Jesus Sanchez | Hits | Over | 0.5 | +107 | 52% | 2 | +3.0% | ✅ |
| Randal Grichuk | RBI | Under | 0.5 | -219 | 76% | 1 | +1.0% | ❌ |
| Travis Bazzana | Hits | Over | 1.5 | +193 | 36% | 4 | — | ✅ |
| Jackson Chourio | H+R+RBI | Over | 1.5 | +107 | 54% | 2 | — | ✅ |
| Kyle Isbel | Hits | Under | 0.5 | +108 | 51% | 2 | +1.5% | ❌ |
| Hao-Yu Lee | H+R+RBI | Under | 1.5 | -141 | 65% | 1 | -0.6% | ✅ |
| Brooks Lee | RBI | Over | 0.5 | +234 | 33% | 0 | -6.4% | ❌ |
| Willy Adames | Hits | Over | 0.5 | -168 | 67% | 0 | +0.4% | ❌ |
| Jung Hoo Lee | Hits | Over | 0.5 | -235 | 75% | 0 | -0.5% | ❌ |
| Dillon Dingler | RBI | Over | 0.5 | +184 | 39% | 0 | +8.4% | ❌ |
| Patrick Bailey | H+R+RBI | Under | 1.5 | -121 | 60% | 6 | -2.7% | ❌ |
| Cole Young | Hits | Over | 0.5 | -158 | 65% | 1 | -4.5% | ✅ |
| Michael Harris II | H+R+RBI | Over | 0.5 | -174 | 70% | 3 | — | ✅ |
| Munetaka Murakami | RBI | Over | 0.5 | +196 | 37% | 0 | +2.1% | ❌ |
| Sal Stewart | Hits | Over | 0.5 | -226 | 74% | 1 | +0.5% | ✅ |
| Carson Benge | Hits | Over | 0.5 | -190 | 70% | 1 | +1.4% | ✅ |
| Michael Massey | H+R+RBI | Under | 1.5 | -142 | 65% | 2 | +1.4% | ❌ |
| Brandon Lowe | H+R+RBI | Over | 1.5 | +131 | 48% | 4 | — | ✅ |
| Salvador Perez | H+R+RBI | Under | 1.5 | -135 | 63% | 1 | +0.0% | ✅ |
| Masyn Winn | H+R+RBI | Over | 1.5 | +138 | 46% | 0 | — | ❌ |
| Nathaniel Lowe | H+R+RBI | Under | 2.5 | -155 | 67% | 5 | — | ❌ |
| Brice Turang | H+R+RBI | Over | 1.5 | +141 | 46% | 1 | — | ❌ |
| Luis Rengifo | H+R+RBI | Under | 1.5 | -122 | 60% | 4 | +0.0% | ❌ |
| Matthew Boyd | Ks (P) | Under | 4.5 | +108 | 50% | 3 | +1.0% | ✅ |
| Rafael Devers | H+R+RBI | Over | 1.5 | +112 | 52% | 3 | +9.1% | ✅ |
| Brandon Nimmo | Hits | Over | 0.5 | -231 | 74% | 0 | -1.4% | ❌ |
| Heliot Ramos | H+R+RBI | Under | 1.5 | -110 | 57% | 1 | +0.0% | ✅ |
| Brooks Lee | Hits | Over | 0.5 | -168 | 66% | 0 | -2.5% | ❌ |
| Griffin Conine | H+R+RBI | Under | 1.5 | -124 | 61% | 0 | +4.4% | ✅ |
| Elias Diaz | Hits | Under | 0.5 | -104 | 54% | 1 | +5.8% | ❌ |
| Oneil Cruz | H+R+RBI | Over | 1.5 | +130 | 48% | 0 | — | ❌ |
| Donovan Walton | H+R+RBI | Over | 0.5 | -147 | 65% | 1 | -4.1% | ✅ |
| Andrés Chaparro | Hits | Under | 0.5 | +103 | 52% | 1 | -1.5% | ❌ |
| Andruw Monasterio | H+R+RBI | Under | 1.5 | -134 | 62% | 1 | +1.6% | ✅ |
| Dylan Beavers | H+R+RBI | Over | 0.5 | -161 | 67% | 3 | -2.7% | ✅ |
| Bryce Eldridge | Hits | Over | 0.5 | -169 | 66% | 1 | -2.8% | ✅ |
| Yandy Diaz | RBI | Over | 0.5 | +192 | 37% | 0 | +0.0% | ❌ |
| Alec Burleson | H+R+RBI | Over | 1.5 | +111 | 52% | 3 | — | ✅ |
| Jose Altuve | H+R+RBI | Under | 1.5 | +103 | 54% | 2 | +0.0% | ❌ |
| Chase DeLauter | H+R+RBI | Under | 2.5 | -122 | 60% | 1 | -1.1% | ✅ |
| Max Muncy | RBI | Under | 0.5 | -190 | 71% | 0 | +1.1% | ✅ |
| Willi Castro | Hits | Over | 0.5 | -246 | 75% | 1 | -2.4% | ✅ |
| Vaughn Grissom | RBI | Over | 0.5 | +236 | 32% | 0 | -2.0% | ❌ |
| Royce Lewis | Hits | Over | 0.5 | -176 | 67% | 0 | +2.0% | ❌ |
| Liam Hicks | H+R+RBI | Over | 1.5 | +123 | 49% | 0 | — | ❌ |
| Jose Ramirez | RBI | Under | 0.5 | -154 | 66% | 0 | +1.0% | ✅ |
| Ildemaro Vargas | RBI | Over | 0.5 | +212 | 35% | 1 | +11.0% | ✅ |
| Jake McCarthy | Hits | Over | 1.5 | +161 | 40% | 0 | +6.1% | ❌ |
| Mike Yastrzemski | H+R+RBI | Over | 0.5 | +110 | 52% | 2 | — | ✅ |
| Zack Gelof | RBI | Over | 0.5 | +237 | 32% | 0 | +0.9% | ❌ |
| Brett Baty | H+R+RBI | Over | 0.5 | -128 | 60% | 4 | +5.4% | ✅ |
| Zach Neto | RBI | Over | 0.5 | +214 | 34% | 0 | -2.2% | ❌ |
| Sal Stewart | H+R+RBI | Over | 1.5 | -111 | 57% | 1 | +0.8% | ❌ |
| Trent Grisham | Hits | Under | 0.5 | +137 | 44% | 0 | +11.8% | ✅ |
| Nathan Lukes | Hits | Under | 0.5 | +129 | 46% | 0 | +1.8% | ✅ |
| Carter Jensen | H+R+RBI | Under | 1.5 | -151 | 65% | 3 | -1.6% | ❌ |
| Kyle Isbel | H+R+RBI | Under | 0.5 | +134 | 46% | 5 | +2.2% | ❌ |
| Alejandro Kirk | H+R+RBI | Under | 1.5 | -120 | 58% | 2 | +11.7% | ❌ |
| Andruw Monasterio | Hits | Under | 0.5 | +139 | 44% | 0 | +0.8% | ✅ |
| Luis Robert Jr. | H+R+RBI | Under | 1.5 | -150 | 64% | 2 | +1.8% | ❌ |
| Josh Bell | RBI | Over | 0.5 | +197 | 36% | 0 | -4.2% | ❌ |
| Jared Young | Hits | Over | 0.5 | -135 | 60% | 1 | +4.7% | ✅ |
| Wyatt Langford | H+R+RBI | Under | 1.5 | -114 | 57% | 3 | +7.5% | ❌ |
| Cam Smith | H+R+RBI | Under | 1.5 | -132 | 61% | 0 | +1.0% | ✅ |
| Tim Tawa | H+R+RBI | Under | 1.5 | -132 | 61% | 4 | -2.0% | ❌ |
| Xavier Edwards | H+R+RBI | Under | 1.5 | -102 | 54% | 0 | +3.3% | ✅ |
| Corey Seager | H+R+RBI | Under | 1.5 | -120 | 58% | 2 | +2.9% | ❌ |
| Shohei Ohtani | H+R+RBI | Under | 2.5 | -153 | 64% | 3 | — | ❌ |
| Joey Cantillo | Ks (P) | Under | 5.5 | -111 | 54% | 5 | -2.2% | ✅ |
| Adley Rutschman | RBI | Over | 0.5 | +193 | 36% | 0 | -7.0% | ❌ |
| Julio Rodriguez | Hits | Under | 0.5 | +190 | 36% | 1 | +0.7% | ❌ |
| Matt McLain | H+R+RBI | Over | 0.5 | -176 | 68% | 0 | — | ❌ |
| Ryan Jeffers | RBI | Over | 0.5 | +216 | 34% | 0 | +9.3% | ❌ |
| Jackson Holliday | H+R+RBI | Under | 1.5 | -133 | 60% | 3 | +2.2% | ❌ |
| Daylen Lile | H+R+RBI | Under | 1.5 | +107 | 51% | 4 | +6.0% | ❌ |
| Michael Busch | Hits | Over | 0.5 | -174 | 66% | 2 | +0.0% | ✅ |
| Owen Caissie | H+R+RBI | Under | 1.5 | -160 | 65% | 1 | +0.9% | ✅ |
| Kazuma Okamoto | H+R+RBI | Over | 0.5 | -177 | 68% | 1 | -4.2% | ✅ |
| Pedro Pages | H+R+RBI | Under | 0.5 | -118 | 57% | 1 | -3.2% | ❌ |
| Josh Naylor | H+R+RBI | Over | 1.5 | +111 | 50% | 2 | +2.9% | ✅ |
| Dylan Crews | Hits | Under | 0.5 | +127 | 46% | 1 | +8.1% | ❌ |
| Jake Burger | Hits | Over | 0.5 | -193 | 68% | 0 | -6.8% | ❌ |
| Nick Gonzales | H+R+RBI | Over | 1.5 | +134 | 45% | 4 | -5.3% | ✅ |
| Isaac Paredes | Hits | Over | 0.5 | -200 | 69% | 1 | +1.0% | ✅ |
| Kazuma Okamoto | RBI | Over | 0.5 | +246 | 30% | 0 | -0.3% | ❌ |
| Yordan Alvarez | H+R+RBI | Under | 2.5 | -138 | 61% | 5 | -0.6% | ❌ |
| Julio Rodriguez | H+R+RBI | Under | 1.5 | -105 | 54% | 1 | -0.9% | ✅ |
| Alex Bregman | Hits | Over | 0.5 | -193 | 68% | 2 | +0.0% | ✅ |
| Owen Caissie | Hits | Under | 0.5 | +107 | 50% | 1 | +2.5% | ❌ |
| Griffin Conine | RBI | Under | 0.5 | -213 | 72% | 0 | +5.9% | ✅ |
| Ryan Vilade | Hits | Over | 0.5 | -161 | 64% | 2 | +1.6% | ✅ |
| Francisco Alvarez | H+R+RBI | Under | 1.5 | -159 | 64% | 0 | +2.6% | ✅ |
| Zack Gelof | Hits | Over | 0.5 | -150 | 62% | 0 | -1.9% | ❌ |
| Vinnie Pasquantino | Hits | Over | 0.5 | -197 | 68% | 2 | -2.7% | ✅ |
| Shohei Ohtani | Hits | Over | 0.5 | -237 | 72% | 1 | -0.9% | ✅ |
| Otto Lopez | H+R+RBI | Under | 1.5 | +110 | 50% | 2 | +2.9% | ❌ |
| Joey Ortiz | Hits | Over | 0.5 | -111 | 54% | 0 | — | ❌ |
| Yainer Diaz | H+R+RBI | Under | 1.5 | -123 | 58% | 1 | -6.3% | ✅ |
| William Contreras | RBI | Over | 0.5 | +241 | 31% | 1 | — | ✅ |
| Everson Pereira | H+R+RBI | Over | 0.5 | -112 | 55% | 1 | +7.0% | ✅ |
| Miguel Vargas | H+R+RBI | Over | 1.5 | -114 | 56% | 5 | -0.4% | ✅ |
| Nathan Lukes | H+R+RBI | Under | 1.5 | -172 | 66% | 0 | +0.2% | ✅ |
| Jackson Holliday | Hits | Under | 0.5 | +137 | 43% | 1 | +1.7% | ❌ |
| Pete Alonso | H+R+RBI | Over | 1.5 | -127 | 58% | 6 | -1.1% | ✅ |
| Alex Bregman | H+R+RBI | Over | 1.5 | +106 | 51% | 5 | +2.0% | ✅ |
| Ernie Clement | Hits | Over | 0.5 | -199 | 68% | 1 | +2.2% | ✅ |
| Max Muncy | H+R+RBI | Under | 1.5 | -126 | 58% | 0 | +0.0% | ✅ |
| Heliot Ramos | RBI | Under | 0.5 | -234 | 73% | 0 | +3.0% | ✅ |
| TJ Rumfield | H+R+RBI | Under | 1.5 | +106 | 51% | 0 | +1.5% | ✅ |
| Colton Cowser | Hits | Under | 0.5 | -132 | 58% | 2 | +1.0% | ❌ |
| Geraldo Perdomo | Hits | Over | 0.5 | -234 | 72% | 3 | -3.0% | ✅ |
| Gary Sanchez | H+R+RBI | Over | 0.5 | -144 | 62% | 0 | — | ❌ |
| Brady House | RBI | Over | 0.5 | +237 | 31% | 0 | -8.4% | ❌ |
| Jose Fernandez | H+R+RBI | Under | 1.5 | -149 | 62% | 2 | +0.8% | ❌ |
| Evan Carter | H+R+RBI | Under | 0.5 | +109 | 50% | 3 | +2.5% | ❌ |
| Corey Seager | Hits | Under | 0.5 | +151 | 41% | 2 | +4.2% | ❌ |
| Elly De La Cruz | H+R+RBI | Over | 1.5 | -119 | 56% | 0 | +0.4% | ❌ |
| A.J. Ewing | Hits | Over | 0.5 | -171 | 65% | 0 | +1.9% | ❌ |
| Seiya Suzuki | H+R+RBI | Over | 1.5 | -103 | 53% | 1 | +0.0% | ❌ |
| J.T. Realmuto | Hits | Under | 0.5 | +134 | 44% | 2 | -6.4% | ❌ |
| William Contreras | Hits | Over | 0.5 | -160 | 63% | 4 | — | ✅ |
| Seiya Suzuki | Hits | Over | 0.5 | -194 | 67% | 1 | +0.0% | ✅ |
| Donovan Walton | Hits | Over | 0.5 | -119 | 56% | 1 | -3.6% | ✅ |
| Rafael Devers | RBI | Over | 0.5 | +201 | 34% | 1 | -0.3% | ✅ |
| Otto Lopez | Hits | Under | 1.5 | -234 | 72% | 1 | +4.6% | ✅ |
| JJ Wetherholt | H+R+RBI | Over | 1.5 | +115 | 48% | 0 | — | ❌ |
| Justin Crawford | H+R+RBI | Under | 1.5 | -154 | 63% | 1 | -3.8% | ✅ |
| Pete Alonso | RBI | Over | 0.5 | +163 | 39% | 3 | +1.9% | ✅ |
| Alex Bregman | RBI | Over | 0.5 | +208 | 34% | 2 | -0.3% | ✅ |
| Ryan Gusto | Ks (P) | Under | 4.5 | -157 | 62% | 2 | -0.2% | ✅ |
| Pete Crow-Armstrong | Hits | Over | 0.5 | -216 | 70% | 1 | +1.1% | ✅ |
| Ke'Bryan Hayes | H+R+RBI | Under | 0.5 | +108 | 50% | 1 | -4.2% | ❌ |
| Bobby Witt Jr. | H+R+RBI | Under | 1.5 | -104 | 53% | 2 | +0.0% | ❌ |
| Oneil Cruz | RBI | Over | 0.5 | +202 | 34% | 0 | -5.9% | ❌ |
| Caleb Durbin | RBI | Over | 0.5 | +216 | 33% | 0 | -2.2% | ❌ |
| Randal Grichuk | Hits | Under | 0.5 | +145 | 42% | 2 | +0.0% | ❌ |
| Hunter Feduccia | Hits | Under | 0.5 | -141 | 60% | 1 | +3.1% | ❌ |
| Xander Bogaerts | Hits | Under | 0.5 | +121 | 46% | 0 | -10.9% | ✅ |
| Hunter Feduccia | H+R+RBI | Under | 0.5 | +103 | 51% | 2 | +2.5% | ❌ |
| Ronald Acuna Jr. | Hits | Over | 0.5 | -141 | 60% | 0 | — | ❌ |
| Brendan Donovan | Hits | Under | 0.5 | +160 | 39% | 1 | -0.4% | ❌ |
| Justin Foscue | H+R+RBI | Under | 0.5 | +108 | 50% | 0 | — | ✅ |
| Moises Ballesteros | H+R+RBI | Under | 0.5 | +137 | 43% | 0 | — | ✅ |
| Jacob Young | H+R+RBI | Over | 0.5 | -174 | 65% | 1 | -4.0% | ✅ |
| Nathaniel Lowe | Hits | Under | 1.5 | -240 | 72% | 2 | +1.8% | ❌ |
| Jonah Heim | RBI | Over | 0.5 | +239 | 30% | 0 | -7.1% | ❌ |
| Jose Caballero | Hits | Over | 0.5 | -122 | 56% | 0 | -0.4% | ❌ |
| Spencer Torkelson | Hits | Over | 0.5 | -154 | 62% | 0 | -0.8% | ❌ |
| Andrew Vaughn | Hits | Over | 0.5 | -180 | 65% | 1 | — | ✅ |
| Andrew Vaughn | H+R+RBI | Under | 1.5 | -150 | 62% | 2 | — | ❌ |
| Munetaka Murakami | H+R+RBI | Over | 1.5 | +109 | 49% | 1 | +1.9% | ❌ |
| Michael Conforto | H+R+RBI | Under | 0.5 | +107 | 50% | 0 | -1.9% | ✅ |
| Vaughn Grissom | H+R+RBI | Over | 1.5 | +121 | 46% | 0 | +1.4% | ❌ |
| Andrés Chaparro | RBI | Over | 0.5 | +228 | 31% | 0 | -2.1% | ❌ |
| Jackson Merrill | H+R+RBI | Over | 1.5 | -117 | 55% | 0 | +0.8% | ❌ |
| Josh Bell | H+R+RBI | Over | 1.5 | +103 | 50% | 1 | +0.5% | ❌ |
| Bobby Witt Jr. | RBI | Under | 0.5 | -248 | 73% | 0 | +0.9% | ✅ |
| Ryan Jeffers | Hits | Under | 0.5 | +157 | 40% | 0 | -1.5% | ✅ |
| Francisco Lindor | Hits | Over | 0.5 | -185 | 66% | 0 | +2.5% | ❌ |
| William Contreras | H+R+RBI | Over | 1.5 | +127 | 45% | 5 | — | ✅ |
| Jackson Chourio | RBI | Over | 0.5 | +232 | 31% | 0 | — | ❌ |
| Willson Contreras | Hits | Under | 0.5 | +166 | 38% | 1 | +2.3% | ❌ |
| Mike Trout | H+R+RBI | Over | 1.5 | +106 | 50% | 0 | -3.3% | ❌ |
| Jose Caballero | H+R+RBI | Over | 0.5 | -177 | 65% | 1 | +0.6% | ✅ |
| Moises Ballesteros | Hits | Under | 0.5 | +108 | 49% | 0 | -11.1% | ✅ |
| Jackson Merrill | RBI | Over | 0.5 | +198 | 34% | 0 | +2.8% | ❌ |
| Austin Wells | H+R+RBI | Under | 0.5 | +129 | 44% | 0 | — | ✅ |
| Jared Young | H+R+RBI | Over | 0.5 | -164 | 63% | 2 | — | ✅ |
| Carlos Cortes | Hits | Over | 0.5 | -150 | 61% | 1 | +1.3% | ✅ |
| Pete Crow-Armstrong | RBI | Over | 0.5 | +175 | 37% | 1 | +2.2% | ✅ |
| Mickey Gasper | RBI | Over | 0.5 | +250 | 29% | 1 | +0.0% | ✅ |
| Yandy Diaz | H+R+RBI | Over | 1.5 | -139 | 59% | 0 | -1.9% | ❌ |
| Junior Caminero | H+R+RBI | Over | 1.5 | -129 | 57% | 3 | +0.3% | ✅ |
| Lawrence Butler | H+R+RBI | Under | 1.5 | -150 | 61% | 0 | +4.2% | ✅ |
| Geraldo Perdomo | RBI | Under | 0.5 | -245 | 72% | 1 | +0.7% | ❌ |
| Trent Grisham | H+R+RBI | Under | 1.5 | -110 | 53% | 1 | +15.4% | ✅ |
| Joey Ortiz | H+R+RBI | Over | 0.5 | -141 | 59% | 0 | — | ❌ |
| Willy Adames | H+R+RBI | Over | 1.5 | +115 | 47% | 0 | +1.9% | ❌ |
| Ivan Herrera | Hits | Over | 0.5 | -189 | 66% | 1 | -15.1% | ✅ |
| Drew Gilbert | Hits | Over | 0.5 | -146 | 60% | 2 | +6.5% | ✅ |
| Jonathan Aranda | Hits | Over | 0.5 | -210 | 68% | 0 | — | ❌ |
| Spencer Horwitz | H+R+RBI | Under | 1.5 | -178 | 65% | 0 | +0.8% | ✅ |
| Justin Crawford | Hits | Over | 0.5 | -156 | 61% | 0 | +5.5% | ❌ |
| Brooks Lee | H+R+RBI | Over | 1.5 | +121 | 46% | 0 | -4.7% | ❌ |
| Fernando Tatis Jr. | H+R+RBI | Over | 1.5 | -124 | 56% | 5 | +2.8% | ✅ |
| Jacob Gonzalez | Hits | Under | 0.5 | -110 | 53% | 0 | +2.1% | ✅ |
| Julio Rodriguez | RBI | Under | 0.5 | -224 | 70% | 0 | +0.4% | ✅ |
| Alec Bohm | RBI | Over | 0.5 | +172 | 37% | 3 | +6.7% | ✅ |
| Matt Olson | RBI | Over | 0.5 | +219 | 32% | 0 | — | ❌ |
| Travis Bazzana | RBI | Under | 0.5 | -200 | 67% | 3 | +2.2% | ❌ |
| Dylan Crews | H+R+RBI | Under | 1.5 | -153 | 61% | 1 | +5.7% | ✅ |
| Angel Martinez | RBI | Under | 0.5 | -164 | 63% | 0 | — | ✅ |
| Mickey Moniak | RBI | Over | 0.5 | +152 | 40% | 0 | -3.5% | ❌ |
| Yainer Diaz | Hits | Over | 0.5 | -215 | 69% | 1 | +6.0% | ✅ |
| Geraldo Perdomo | H+R+RBI | Under | 1.5 | -107 | 52% | 6 | +1.3% | ❌ |
| Andrés Chaparro | H+R+RBI | Over | 0.5 | -172 | 64% | 1 | -1.8% | ✅ |
| Travis Bazzana | H+R+RBI | Under | 1.5 | +118 | 46% | 9 | +4.8% | ❌ |
| Elly De La Cruz | RBI | Over | 0.5 | +205 | 33% | 0 | +1.3% | ❌ |
| Henry Davis | H+R+RBI | Under | 0.5 | -102 | 51% | 0 | +2.4% | ✅ |
| Luis Garcia Jr. | Hits | Under | 0.5 | +167 | 38% | 0 | — | ✅ |
| Eugenio Suarez | RBI | Over | 0.5 | +201 | 33% | 0 | +3.1% | ❌ |
| Wilyer Abreu | H+R+RBI | Under | 1.5 | -101 | 50% | 5 | -2.9% | ❌ |
| JT Ginn | Ks (P) | Over | 4.5 | -125 | 56% | 4 | +0.0% | ❌ |
| Eugenio Suarez | H+R+RBI | Under | 1.5 | -153 | 61% | 0 | +1.5% | ✅ |
| Jesus Sanchez | H+R+RBI | Over | 0.5 | -117 | 54% | 2 | +4.1% | ✅ |
| A.J. Ewing | H+R+RBI | Under | 1.5 | -148 | 60% | 0 | -2.0% | ✅ |
| Nolan Arenado | Hits | Under | 0.5 | +155 | 39% | 1 | +0.0% | ❌ |
| Ezequiel Duran | RBI | Over | 0.5 | +248 | 29% | 0 | +2.0% | ❌ |
| Dominic Canzone | H+R+RBI | Under | 1.5 | -147 | 60% | 0 | +0.8% | ✅ |
| Christian Walker | Hits | Over | 0.5 | -171 | 63% | 2 | +1.7% | ✅ |
| Matt McLain | Hits | Over | 0.5 | -136 | 58% | 0 | +2.1% | ❌ |
| Fernando Tatis Jr. | RBI | Over | 0.5 | +189 | 35% | 1 | +0.7% | ✅ |
| Manny Machado | H+R+RBI | Under | 1.5 | -105 | 51% | 4 | +4.0% | ❌ |
| Nathaniel Lowe | RBI | Under | 0.5 | -167 | 63% | 0 | +4.8% | ✅ |
| Kyle Schwarber | H+R+RBI | Under | 1.5 | +106 | 49% | 0 | — | ✅ |
| Jeff McNeil | H+R+RBI | Under | 1.5 | -117 | 54% | 1 | +5.5% | ✅ |
| Samuel Basallo | H+R+RBI | Under | 1.5 | -122 | 55% | 0 | +5.5% | ✅ |
| Caleb Durbin | H+R+RBI | Under | 1.5 | -118 | 54% | 2 | +0.0% | ❌ |
| Byron Buxton | Hits | Over | 0.5 | -222 | 69% | 0 | +3.2% | ❌ |
| Jarren Duran | RBI | Over | 0.5 | +212 | 32% | 0 | +0.0% | ❌ |
| Nico Hoerner | Hits | Over | 0.5 | -218 | 68% | 1 | +0.0% | ✅ |
| Bryce Harper | Hits | Under | 0.5 | +165 | 38% | 0 | -3.6% | ✅ |
| Kody Clemens | Hits | Over | 0.5 | -183 | 64% | 1 | -2.0% | ✅ |
| Drew Gilbert | H+R+RBI | Under | 1.5 | -186 | 65% | 5 | -7.5% | ❌ |
| Jonah Heim | H+R+RBI | Under | 1.5 | -173 | 63% | 0 | — | ✅ |
| Ildemaro Vargas | H+R+RBI | Under | 1.5 | +108 | 48% | 1 | -1.4% | ✅ |
| Ezequiel Tovar | Hits | Under | 0.5 | +118 | 46% | 0 | +1.9% | ✅ |
| Dillon Dingler | H+R+RBI | Under | 1.5 | -104 | 51% | 0 | +1.9% | ✅ |
| George Springer | H+R+RBI | Under | 1.5 | -152 | 60% | 0 | — | ✅ |
| Jung Hoo Lee | H+R+RBI | Over | 1.5 | -102 | 50% | 0 | -2.4% | ❌ |
| Randy Arozarena | Hits | Over | 0.5 | -241 | 70% | 1 | -1.5% | ✅ |
| J.T. Realmuto | H+R+RBI | Under | 1.5 | -136 | 57% | 4 | -3.6% | ❌ |
| Ben Rice | H+R+RBI | Under | 1.5 | +103 | 49% | 0 | +13.2% | ✅ |
| Ceddanne Rafaela | H+R+RBI | Under | 1.5 | +110 | 47% | 2 | +0.5% | ❌ |
| Ezequiel Tovar | H+R+RBI | Under | 1.5 | -154 | 60% | 0 | +1.5% | ✅ |
| Ian Happ | H+R+RBI | Over | 1.5 | +127 | 44% | 4 | +0.4% | ✅ |
| Mickey Moniak | H+R+RBI | Under | 1.5 | -110 | 52% | 0 | +1.7% | ✅ |
| Justin Foscue | Hits | Under | 0.5 | -120 | 54% | 0 | -11.0% | ✅ |
| Heriberto Hernandez | RBI | Under | 0.5 | -240 | 70% | 0 | +4.3% | ✅ |
| Pete Crow-Armstrong | H+R+RBI | Over | 1.5 | -121 | 54% | 3 | +3.2% | ✅ |
| Gabriel Moreno | H+R+RBI | Over | 1.5 | -136 | 57% | 3 | +2.1% | ✅ |
| Brett Baty | Hits | Over | 0.5 | -101 | 50% | 2 | +7.3% | ✅ |
| Jake Cronenworth | Hits | Over | 0.5 | -184 | 64% | 0 | -5.7% | ❌ |
| Henry Bolte | Hits | Over | 0.5 | -193 | 65% | 0 | -0.2% | ❌ |
| Colton Cowser | H+R+RBI | Over | 0.5 | -131 | 56% | 3 | +0.0% | ✅ |
| Brandon Marsh | H+R+RBI | Over | 1.5 | +101 | 49% | 5 | +5.3% | ✅ |
| Vinnie Pasquantino | H+R+RBI | Under | 1.5 | -132 | 56% | 5 | +1.3% | ❌ |
| Kyle Tucker | Hits | Over | 0.5 | -151 | 60% | 0 | +1.6% | ❌ |
| Ivan Herrera | H+R+RBI | Over | 1.5 | +105 | 48% | 2 | — | ✅ |
| Cole Young | H+R+RBI | Over | 1.5 | +123 | 44% | 2 | — | ✅ |
| Ronald Acuna Jr. | H+R+RBI | Over | 1.5 | +137 | 42% | 1 | — | ❌ |
| Kazuma Okamoto | Hits | Over | 0.5 | -141 | 58% | 1 | -3.1% | ✅ |
| Jonny Deluca | H+R+RBI | Under | 1.5 | -141 | 58% | 1 | -2.1% | ✅ |
| JJ Bleday | H+R+RBI | Under | 1.5 | -154 | 60% | 0 | +2.9% | ✅ |
| Taylor Ward | H+R+RBI | Over | 1.5 | +114 | 46% | 1 | +7.0% | ❌ |
| Manny Machado | RBI | Under | 0.5 | -198 | 66% | 1 | +5.7% | ❌ |
| Bo Bichette | Hits | Over | 0.5 | -224 | 68% | 1 | +2.4% | ✅ |
| Samuel Basallo | Hits | Under | 0.5 | +144 | 41% | 0 | +6.1% | ✅ |
| Brendan Donovan | H+R+RBI | Under | 1.5 | -131 | 56% | 2 | +0.0% | ❌ |
| Mookie Betts | Hits | Over | 0.5 | -194 | 65% | 1 | +0.0% | ✅ |
| Isaac Paredes | H+R+RBI | Under | 1.5 | -117 | 53% | 3 | -0.4% | ❌ |
| Connor Prielipp | Ks (P) | Over | 5.5 | +112 | 47% | 7 | -4.1% | ✅ |
| Yordan Alvarez | RBI | Under | 0.5 | -172 | 62% | 2 | -0.2% | ❌ |
| Jake Rogers | H+R+RBI | Over | 0.5 | -136 | 56% | 4 | +3.3% | ✅ |
| Nolan Arenado | RBI | Over | 0.5 | +162 | 37% | 1 | +1.6% | ✅ |
| Joe Mack | H+R+RBI | Over | 0.5 | -171 | 62% | 0 | +1.1% | ❌ |
| Ryan Vilade | H+R+RBI | Under | 1.5 | -163 | 61% | 2 | -2.2% | ❌ |
| Jeff McNeil | Hits | Under | 0.5 | +199 | 33% | 1 | +12.4% | ❌ |
| Alejandro Kirk | RBI | Over | 0.5 | +222 | 30% | 1 | -10.6% | ✅ |
| Isaac Paredes | RBI | Over | 0.5 | +187 | 34% | 1 | +4.0% | ✅ |
| Jacob Gonzalez | H+R+RBI | Under | 0.5 | +109 | 47% | 0 | +3.0% | ✅ |
| Ezequiel Duran | Hits | Under | 0.5 | +122 | 44% | 4 | +1.4% | ❌ |
| Cal Raleigh | RBI | Under | 0.5 | -247 | 70% | 3 | +0.2% | ❌ |
| Brady House | H+R+RBI | Under | 1.5 | -150 | 59% | 1 | +4.2% | ✅ |
| Wyatt Langford | Hits | Under | 0.5 | +150 | 39% | 1 | +4.2% | ❌ |
| Andy Pages | H+R+RBI | Under | 1.5 | -102 | 49% | 0 | +1.4% | ✅ |
| Teoscar Hernandez | Hits | Under | 0.5 | +115 | 46% | 0 | +0.5% | ✅ |
| Ceddanne Rafaela | Hits | Under | 1.5 | -239 | 70% | 2 | +0.0% | ❌ |
| Carson Benge | H+R+RBI | Over | 1.5 | +109 | 47% | 2 | +4.5% | ✅ |
| Josh Naylor | RBI | Over | 0.5 | +247 | 28% | 0 | +2.4% | ❌ |
| Jarren Duran | H+R+RBI | Under | 1.5 | -133 | 56% | 2 | -1.3% | ❌ |
| Jarren Duran | Hits | Under | 0.5 | +139 | 41% | 2 | -2.0% | ❌ |
| Chase DeLauter | Hits | Under | 1.5 | -171 | 62% | 1 | +1.1% | ✅ |
| Adley Rutschman | H+R+RBI | Under | 1.5 | -118 | 53% | 2 | +4.8% | ❌ |
| Bo Bichette | RBI | Over | 0.5 | +213 | 31% | 1 | +7.9% | ✅ |
| Gunnar Henderson | H+R+RBI | Over | 1.5 | -108 | 51% | 1 | -5.6% | ❌ |
| Tommy Edman | H+R+RBI | Under | 1.5 | -140 | 57% | 1 | +3.7% | ✅ |
| Ceddanne Rafaela | RBI | Over | 0.5 | +197 | 33% | 0 | -2.3% | ❌ |
| Corbin Carroll | H+R+RBI | Over | 1.5 | -144 | 57% | 4 | -2.0% | ✅ |
| Junior Caminero | RBI | Over | 0.5 | +145 | 40% | 0 | +4.7% | ❌ |
| Marcus Semien | H+R+RBI | Over | 0.5 | -171 | 61% | 3 | — | ✅ |
| Gleyber Torres | H+R+RBI | Under | 1.5 | -117 | 52% | 0 | +2.3% | ✅ |
| Jake Mangum | H+R+RBI | Over | 0.5 | -179 | 62% | 1 | -1.4% | ✅ |
| Alec Burleson | Hits | Over | 0.5 | -180 | 63% | 1 | — | ✅ |
| Shohei Ohtani | RBI | Under | 0.5 | -182 | 63% | 0 | -0.2% | ✅ |
| Bobby Witt Jr. | Hits | Under | 0.5 | +188 | 34% | 2 | +2.1% | ❌ |
| Brandon Nimmo | H+R+RBI | Under | 1.5 | -119 | 53% | 0 | +0.4% | ✅ |
| Bryce Eldridge | RBI | Over | 0.5 | +232 | 29% | 1 | -0.6% | ✅ |
| Bryce Eldridge | H+R+RBI | Over | 1.5 | +117 | 45% | 2 | -4.0% | ✅ |
| Jazz Chisholm Jr. | Hits | Under | 0.5 | +108 | 47% | 0 | — | ✅ |
| Jonathan Aranda | H+R+RBI | Over | 1.5 | -111 | 51% | 0 | — | ❌ |
| Adley Rutschman | Hits | Over | 0.5 | -212 | 67% | 1 | -3.4% | ✅ |
| Gunnar Henderson | Hits | Over | 0.5 | -203 | 66% | 1 | -2.6% | ✅ |
| Henry Bolte | H+R+RBI | Over | 1.5 | +107 | 47% | 0 | +1.5% | ❌ |
| Francisco Alvarez | Hits | Under | 0.5 | +111 | 46% | 0 | +2.4% | ✅ |
| Tim Tawa | Hits | Under | 0.5 | +149 | 39% | 2 | +0.0% | ❌ |
| Freddie Freeman | H+R+RBI | Under | 1.5 | -101 | 49% | 0 | +1.5% | ✅ |
| Kyle Tucker | H+R+RBI | Under | 1.5 | -152 | 58% | 0 | -1.3% | ✅ |
| Byron Buxton | RBI | Under | 0.5 | -243 | 68% | 0 | -3.7% | ✅ |
| Carlos Cortes | H+R+RBI | Under | 1.5 | -180 | 62% | 1 | -2.9% | ✅ |
| Luis Arraez | H+R+RBI | Over | 1.5 | -145 | 57% | 4 | — | ✅ |
| Ryan Jeffers | H+R+RBI | Over | 1.5 | -103 | 49% | 0 | +1.9% | ❌ |
| Heliot Ramos | Hits | Under | 0.5 | +178 | 35% | 1 | +0.4% | ❌ |
| Spencer Jones | H+R+RBI | Over | 0.5 | -166 | 60% | 4 | -0.2% | ✅ |
| Cole Carrigg | H+R+RBI | Under | 1.5 | +106 | 47% | 1 | +2.0% | ✅ |
| Jake Burger | H+R+RBI | Under | 1.5 | -130 | 54% | 0 | +8.3% | ✅ |
| Josh Lowe | H+R+RBI | Over | 0.5 | -162 | 60% | 0 | -1.4% | ❌ |
| Andy Pages | Hits | Over | 0.5 | -238 | 69% | 0 | -1.6% | ❌ |
| Trevor Larnach | Hits | Over | 0.5 | -144 | 58% | 0 | +0.8% | ❌ |
| Kyle Schwarber | RBI | Under | 0.5 | -186 | 62% | 0 | -3.2% | ✅ |
| TJ Rumfield | RBI | Under | 0.5 | -233 | 67% | 0 | -1.1% | ✅ |
| Wilyer Abreu | RBI | Under | 0.5 | -216 | 66% | 1 | -0.7% | ❌ |
| Mookie Betts | H+R+RBI | Under | 1.5 | -126 | 54% | 3 | -1.4% | ❌ |
| Chase DeLauter | RBI | Under | 0.5 | -173 | 61% | 0 | -2.9% | ✅ |
| Spencer Jones | Hits | Over | 0.5 | -119 | 53% | 1 | -2.0% | ✅ |
| Byron Buxton | H+R+RBI | Over | 1.5 | -116 | 51% | 1 | +6.3% | ❌ |
| Teoscar Hernandez | H+R+RBI | Under | 1.5 | -155 | 58% | 0 | -1.8% | ✅ |
| Liam Hicks | Hits | Under | 0.5 | +118 | 45% | 0 | +7.4% | ✅ |
| Patrick Bailey | Hits | Under | 0.5 | +142 | 40% | 2 | -2.4% | ❌ |
| Michael Busch | H+R+RBI | Over | 1.5 | +111 | 45% | 3 | +1.9% | ✅ |
| Randy Arozarena | H+R+RBI | Under | 1.5 | -109 | 50% | 2 | +2.1% | ❌ |
| Austin Wells | Hits | Under | 0.5 | -106 | 50% | 0 | — | ✅ |
| Alec Bohm | H+R+RBI | Under | 1.5 | -103 | 48% | 7 | -6.2% | ❌ |
| Royce Lewis | RBI | Over | 0.5 | +209 | 31% | 0 | +3.3% | ❌ |
| Luke Keaschall | H+R+RBI | Under | 1.5 | -141 | 56% | 1 | -7.5% | ✅ |
| Nico Hoerner | H+R+RBI | Over | 1.5 | +101 | 48% | 1 | +0.0% | ❌ |
| Wilyer Abreu | Hits | Under | 0.5 | +173 | 36% | 3 | -5.2% | ❌ |
| Bryan Reynolds | H+R+RBI | Over | 1.5 | +132 | 41% | 0 | +0.4% | ❌ |
| Luis Garcia Jr. | H+R+RBI | Under | 1.5 | -116 | 51% | 0 | — | ✅ |
| Michael Busch | RBI | Over | 0.5 | +206 | 31% | 0 | +2.3% | ❌ |
| Josh Lowe | Hits | Over | 0.5 | -132 | 55% | 0 | -1.7% | ❌ |
| Ty France | Hits | Over | 0.5 | -195 | 64% | 1 | +2.5% | ✅ |
| Samuel Basallo | RBI | Under | 0.5 | -229 | 66% | 0 | +3.9% | ✅ |
| Kyle Schwarber | Hits | Over | 0.5 | -212 | 66% | 0 | +3.2% | ❌ |
| Bo Bichette | H+R+RBI | Over | 1.5 | -103 | 48% | 3 | +3.7% | ✅ |
| Christian Walker | RBI | Over | 0.5 | +182 | 34% | 1 | +2.5% | ✅ |
| Ty France | H+R+RBI | Under | 1.5 | -133 | 54% | 5 | -5.2% | ❌ |
| Trevor Larnach | H+R+RBI | Over | 1.5 | +135 | 40% | 0 | — | ❌ |
| Kevin McGonigle | H+R+RBI | Over | 1.5 | -114 | 51% | 3 | -0.4% | ✅ |
| Xander Bogaerts | H+R+RBI | Under | 1.5 | -162 | 59% | 0 | -7.4% | ✅ |
| Braden Montgomery | H+R+RBI | Under | 1.5 | -143 | 56% | 1 | — | ✅ |
| Hao-Yu Lee | Hits | Over | 0.5 | -166 | 60% | 1 | +3.4% | ✅ |
| Braden Montgomery | Hits | Under | 0.5 | +135 | 41% | 0 | — | ✅ |
| JJ Wetherholt | Hits | Over | 0.5 | -184 | 63% | 0 | -15.8% | ❌ |
| Nolan Arenado | H+R+RBI | Over | 1.5 | -117 | 51% | 3 | +0.0% | ✅ |
| Jake McCarthy | H+R+RBI | Under | 1.5 | +123 | 43% | 1 | -2.2% | ✅ |
| Munetaka Murakami | Hits | Over | 0.5 | -149 | 58% | 0 | +1.1% | ❌ |
| Javier Baez | H+R+RBI | Over | 1.5 | +115 | 44% | 1 | -4.4% | ❌ |
| Dominic Canzone | Hits | Under | 0.5 | +134 | 41% | 0 | +0.0% | ✅ |
| Bryson Stott | RBI | Over | 0.5 | +190 | 33% | 0 | +9.4% | ❌ |
| Willi Castro | H+R+RBI | Over | 1.5 | -129 | 53% | 2 | -3.2% | ✅ |
| Cole Carrigg | RBI | Over | 0.5 | +173 | 35% | 0 | -0.7% | ❌ |
| Jake Cronenworth | H+R+RBI | Over | 1.5 | +111 | 45% | 1 | -6.2% | ❌ |
| Bryson Stott | H+R+RBI | Under | 1.5 | -120 | 51% | 1 | -8.3% | ✅ |
| Troy Melton | Ks (P) | Under | 4.5 | -111 | 51% | 3 | +6.3% | ✅ |
| Michael Harris II | RBI | Over | 0.5 | +237 | 28% | 1 | — | ✅ |
| Spencer Torkelson | H+R+RBI | Over | 1.5 | +102 | 47% | 0 | -4.3% | ❌ |
| Bryce Harper | H+R+RBI | Over | 1.5 | -128 | 53% | 1 | +5.4% | ❌ |
| Willson Contreras | H+R+RBI | Under | 1.5 | -109 | 49% | 5 | +1.7% | ❌ |
| Christian Walker | H+R+RBI | Over | 1.5 | +106 | 46% | 3 | +4.0% | ✅ |
| Eugenio Suarez | Hits | Under | 0.5 | +113 | 45% | 0 | +0.5% | ✅ |
| Joe Mack | Hits | Over | 0.5 | -127 | 54% | 0 | +2.0% | ❌ |
| Willson Contreras | RBI | Over | 0.5 | +160 | 36% | 3 | -1.9% | ✅ |
| Bryson Stott | Hits | Under | 0.5 | +148 | 39% | 0 | -11.4% | ✅ |
| Jonny Deluca | Hits | Over | 0.5 | -186 | 62% | 1 | +3.2% | ✅ |
| Ben Rice | RBI | Over | 0.5 | +152 | 37% | 0 | -3.5% | ❌ |
| Royce Lewis | H+R+RBI | Over | 1.5 | +103 | 46% | 0 | -1.0% | ❌ |
| Manny Machado | Hits | Over | 0.5 | -230 | 67% | 2 | -1.2% | ✅ |
| Leody Taveras | H+R+RBI | Over | 1.5 | +116 | 43% | 1 | — | ❌ |
| Griffin Conine | Hits | Over | 0.5 | -167 | 60% | 0 | -0.9% | ❌ |
| JJ Bleday | Hits | Under | 0.5 | +126 | 42% | 0 | +5.6% | ✅ |
| Kody Clemens | H+R+RBI | Over | 1.5 | +101 | 46% | 3 | -2.4% | ✅ |
| Ty France | RBI | Over | 0.5 | +208 | 30% | 3 | +13.2% | ✅ |
| Miguel Vargas | RBI | Over | 0.5 | +160 | 36% | 2 | -1.9% | ✅ |
| Mickey Gasper | Hits | Over | 0.5 | -161 | 59% | 0 | -1.0% | ❌ |
| Brady House | Hits | Under | 0.5 | +129 | 42% | 1 | +5.5% | ❌ |
| Trea Turner | H+R+RBI | Under | 1.5 | +104 | 46% | 0 | -7.3% | ✅ |
| Leody Taveras | Hits | Over | 0.5 | -168 | 60% | 1 | -7.2% | ✅ |
| Ezequiel Duran | H+R+RBI | Over | 1.5 | +121 | 42% | 4 | -0.5% | ✅ |
| Francisco Lindor | H+R+RBI | Over | 1.5 | -103 | 47% | 0 | +0.9% | ❌ |
| Luis Garcia Jr. | RBI | Over | 0.5 | +164 | 35% | 0 | — | ❌ |
| Willy Adames | RBI | Over | 0.5 | +212 | 30% | 0 | +11.8% | ❌ |
| Luis Arraez | RBI | Over | 0.5 | +178 | 33% | 0 | +13.5% | ❌ |
| Jazz Chisholm Jr. | H+R+RBI | Over | 1.5 | +117 | 43% | 0 | — | ❌ |
| Javier Baez | RBI | Over | 0.5 | +250 | 26% | 0 | -2.2% | ❌ |
| Ernie Clement | H+R+RBI | Over | 1.5 | +117 | 43% | 1 | +3.3% | ❌ |
| Jacob Young | Hits | Over | 0.5 | -143 | 56% | 0 | -4.3% | ❌ |
| Gleyber Torres | Hits | Under | 0.5 | +150 | 38% | 0 | +3.3% | ✅ |
| Trea Turner | RBI | Over | 0.5 | +206 | 30% | 0 | +7.4% | ❌ |
| Dominic Canzone | RBI | Over | 0.5 | +218 | 29% | 0 | -3.6% | ❌ |
| Jose Altuve | Hits | Under | 0.5 | +184 | 33% | 2 | +0.3% | ❌ |
| Bryce Harper | RBI | Over | 0.5 | +166 | 34% | 0 | +4.3% | ❌ |
| Mickey Gasper | H+R+RBI | Over | 1.5 | +121 | 42% | 1 | +0.0% | ❌ |
| Jonny Deluca | RBI | Over | 0.5 | +228 | 28% | 0 | -2.4% | ❌ |
| Ryan Vilade | RBI | Over | 0.5 | +228 | 28% | 0 | -4.9% | ❌ |
| Kevin McGonigle | RBI | Over | 0.5 | +191 | 32% | 1 | -0.7% | ✅ |
| Logan Webb | Ks (P) | Over | 4.5 | -119 | 52% | 2 | -7.1% | ❌ |
| Jake Mangum | Hits | Over | 0.5 | -146 | 56% | 1 | -1.4% | ✅ |
| Daylen Lile | RBI | Over | 0.5 | +173 | 33% | 1 | -5.2% | ✅ |
| Spencer Torkelson | RBI | Over | 0.5 | +187 | 32% | 0 | -5.3% | ❌ |
| Luke Keaschall | Hits | Under | 0.5 | +152 | 38% | 1 | -7.0% | ❌ |
| Andy Pages | RBI | Over | 0.5 | +163 | 35% | 0 | +2.3% | ❌ |
| Jake Burger | RBI | Over | 0.5 | +181 | 32% | 0 | -6.0% | ❌ |
| Marcus Semien | Hits | Over | 0.5 | -140 | 55% | 2 | +4.5% | ✅ |
| J.T. Realmuto | RBI | Over | 0.5 | +214 | 29% | 2 | +6.4% | ✅ |
| Bubba Chandler | Ks (P) | Under | 4.5 | -144 | 57% | 6 | +0.8% | ❌ |
| JJ Bleday | RBI | Over | 0.5 | +208 | 30% | 0 | -8.9% | ❌ |
| Trent Grisham | RBI | Over | 0.5 | +176 | 33% | 0 | -3.2% | ❌ |
| Kody Clemens | RBI | Over | 0.5 | +174 | 33% | 2 | -6.8% | ✅ |
| Brice Turang | Hits | Under | 0.5 | +112 | 44% | 1 | — | ❌ |
| Tommy Edman | Hits | Under | 0.5 | +136 | 40% | 1 | +7.3% | ❌ |
| Willi Castro | RBI | Over | 0.5 | +168 | 34% | 1 | +0.8% | ✅ |
| Lawrence Butler | Hits | Under | 0.5 | +125 | 42% | 0 | +6.1% | ✅ |
| Max Muncy | Hits | Under | 0.5 | +120 | 43% | 0 | +3.8% | ✅ |
| Joe Mack | RBI | Over | 0.5 | +247 | 26% | 0 | +6.4% | ❌ |
| George Springer | Hits | Under | 0.5 | +138 | 39% | 0 | — | ✅ |
| Mike Trout | RBI | Over | 0.5 | +213 | 29% | 0 | -2.8% | ❌ |
| MacKenzie Gore | Ks (P) | Over | 6.5 | -123 | 53% | 7 | +8.2% | ✅ |
| Andruw Monasterio | RBI | Over | 0.5 | +215 | 28% | 1 | +0.0% | ✅ |
| Bryan Reynolds | Hits | Under | 0.5 | +123 | 42% | 0 | +0.9% | ✅ |
| Corbin Carroll | RBI | Over | 0.5 | +174 | 32% | 0 | -2.8% | ❌ |
| Jazz Chisholm Jr. | RBI | Over | 0.5 | +207 | 29% | 0 | — | ❌ |
| Dylan Crews | RBI | Over | 0.5 | +235 | 26% | 0 | -10.2% | ❌ |
| Jose Altuve | RBI | Over | 0.5 | +220 | 27% | 0 | +2.6% | ❌ |
| Brandon Marsh | RBI | Over | 0.5 | +197 | 30% | 1 | +6.1% | ✅ |
| Freddie Freeman | RBI | Over | 0.5 | +186 | 30% | 0 | +2.1% | ❌ |
| Vaughn Grissom | Hits | Under | 0.5 | +134 | 39% | 0 | -0.8% | ✅ |
| Ian Happ | RBI | Over | 0.5 | +224 | 27% | 1 | +3.2% | ✅ |
| Kyle Tucker | RBI | Over | 0.5 | +211 | 28% | 0 | +5.1% | ❌ |
| Chris Sale | Ks (P) | Over | 7.5 | -108 | 49% | 6 | — | ❌ |
| Luis Rengifo | RBI | Over | 0.5 | +213 | 28% | 1 | -5.2% | ✅ |
| Carson Benge | RBI | Over | 0.5 | +207 | 28% | 0 | +0.0% | ❌ |
| George Springer | RBI | Over | 0.5 | +222 | 27% | 0 | — | ❌ |
| Jose Fernandez | Hits | Under | 0.5 | +126 | 40% | 1 | +0.0% | ❌ |
| Ezequiel Tovar | RBI | Over | 0.5 | +232 | 26% | 0 | -3.8% | ❌ |
| Carter Jensen | RBI | Over | 0.5 | +241 | 25% | 1 | +0.6% | ✅ |
| Ben Rice | Hits | Under | 0.5 | +166 | 34% | 0 | +14.2% | ✅ |
| Kevin McGonigle | Hits | Under | 0.5 | +167 | 34% | 2 | +3.1% | ❌ |
| Brice Turang | RBI | Over | 0.5 | +360 | 35% | 0 | — | ❌ |
| Liam Hicks | RBI | Over | 0.5 | +258 | 37% | 0 | -10.7% | ❌ |
| Mauricio Dubon | RBI | Over | 0.5 | +397 | 27% | 0 | — | ❌ |
| Jake Bauers | RBI | Over | 0.5 | +277 | 33% | 0 | — | ❌ |
| Chase Meidroth | RBI | Over | 0.5 | +295 | 30% | 0 | -6.2% | ❌ |
| Braden Montgomery | RBI | Over | 0.5 | +255 | 34% | 0 | — | ❌ |
| Drake Baldwin | RBI | Over | 0.5 | +287 | 30% | 0 | — | ❌ |
| Trevor Larnach | RBI | Over | 0.5 | +335 | 26% | 0 | +11.8% | ❌ |
| Dylan Beavers | RBI | Over | 0.5 | +276 | 30% | 1 | -6.7% | ✅ |
| Brendan Donovan | RBI | Over | 0.5 | +292 | 29% | 1 | -7.5% | ✅ |
| Masyn Winn | RBI | Over | 0.5 | +296 | 28% | 0 | — | ❌ |
| Ozzie Albies | RBI | Over | 0.5 | +305 | 27% | 0 | — | ❌ |
| Nico Hoerner | RBI | Over | 0.5 | +259 | 31% | 0 | +0.0% | ❌ |
| Corbin Carroll | Hits | Over | 0.5 | -254 | 79% | 2 | -1.3% | ✅ |
| Jung Hoo Lee | RBI | Over | 0.5 | +292 | 28% | 0 | +5.7% | ❌ |
| Jorge Mateo | RBI | Under | 0.5 | -320 | 83% | 0 | -0.1% | ✅ |
| JJ Wetherholt | RBI | Over | 0.5 | +300 | 27% | 0 | -11.1% | ❌ |
| Esteury Ruiz | RBI | Under | 0.5 | -428 | 88% | 0 | — | ✅ |
| Ivan Herrera | RBI | Over | 0.5 | +271 | 29% | 0 | -11.7% | ❌ |
| Carlos Cortes | RBI | Over | 0.5 | +267 | 30% | 0 | +10.2% | ❌ |
| Jeff McNeil | RBI | Over | 0.5 | +254 | 31% | 0 | -4.3% | ❌ |
| Cole Young | RBI | Over | 0.5 | +271 | 29% | 0 | -7.2% | ❌ |
| Spencer Horwitz | RBI | Over | 0.5 | +344 | 24% | 0 | +2.8% | ❌ |
| Jose Tena | RBI | Under | 0.5 | -322 | 82% | 0 | — | ✅ |
| Brenton Doyle | RBI | Under | 0.5 | -357 | 83% | 0 | +0.5% | ✅ |
| Dane Myers | RBI | Under | 0.5 | -326 | 82% | 0 | -4.5% | ✅ |
| Jakob Marsee | RBI | Under | 0.5 | -306 | 80% | 0 | +3.4% | ✅ |
| Nick Allen | RBI | Under | 0.5 | -437 | 87% | 0 | +1.1% | ✅ |
| Austin Wells | RBI | Under | 0.5 | -330 | 81% | 0 | — | ✅ |
| Joey Ortiz | RBI | Over | 0.5 | +329 | 24% | 0 | — | ❌ |
| Austin Riley | RBI | Over | 0.5 | +290 | 27% | 0 | — | ❌ |
| Connor Norby | RBI | Under | 0.5 | -293 | 78% | 0 | — | ✅ |
| Jose Siri | RBI | Under | 0.5 | -369 | 82% | 0 | -0.1% | ✅ |
| Gabriel Moreno | Hits | Over | 0.5 | -269 | 76% | 2 | — | ✅ |
| Cole Carrigg | Hits | Under | 1.5 | -263 | 75% | 1 | — | ✅ |
| Francisco Alvarez | RBI | Under | 0.5 | -290 | 77% | 0 | +2.8% | ✅ |
| Elias Diaz | RBI | Under | 0.5 | -408 | 83% | 0 | +2.3% | ✅ |
| Junior Caminero | Hits | Over | 0.5 | -258 | 74% | 2 | -2.2% | ✅ |
| Daylen Lile | Hits | Under | 1.5 | -259 | 74% | 3 | — | ❌ |
| Nick Gonzales | RBI | Over | 0.5 | +319 | 25% | 2 | -6.5% | ✅ |
| Jose Caballero | RBI | Over | 0.5 | +268 | 28% | 1 | +7.6% | ✅ |
| Michael Massey | RBI | Under | 0.5 | -303 | 77% | 0 | +1.8% | ✅ |
| Justin Foscue | RBI | Under | 0.5 | -404 | 82% | 0 | +0.9% | ✅ |
| Xander Bogaerts | RBI | Over | 0.5 | +266 | 28% | 0 | +8.0% | ❌ |
| Myles Straw | RBI | Under | 0.5 | -588 | 88% | 0 | +0.8% | ✅ |
| Brandon Nimmo | RBI | Under | 0.5 | -259 | 74% | 0 | -0.9% | ✅ |
| Ke'Bryan Hayes | RBI | Under | 0.5 | -485 | 85% | 0 | -0.3% | ✅ |
| Ronald Acuna Jr. | RBI | Over | 0.5 | +258 | 29% | 0 | — | ❌ |
| Hunter Feduccia | RBI | Under | 0.5 | -492 | 85% | 0 | +1.1% | ✅ |
| Ildemaro Vargas | Hits | Under | 1.5 | -260 | 74% | 0 | +0.0% | ✅ |
| Jose Fernandez | RBI | Under | 0.5 | -320 | 78% | 0 | +0.7% | ✅ |
| Hao-Yu Lee | RBI | Under | 0.5 | -282 | 75% | 0 | +5.0% | ✅ |
| Alec Bohm | Hits | Over | 0.5 | -255 | 73% | 3 | — | ✅ |
| Jacob Young | RBI | Over | 0.5 | +281 | 27% | 0 | -1.6% | ❌ |
| Bryan Reynolds | RBI | Over | 0.5 | +275 | 27% | 0 | +3.3% | ❌ |
| Vinnie Pasquantino | RBI | Under | 0.5 | -272 | 74% | 1 | +3.2% | ❌ |
| Pedro Pages | RBI | Under | 0.5 | -567 | 86% | 0 | +0.2% | ✅ |
| Xavier Edwards | RBI | Under | 0.5 | -277 | 74% | 0 | +1.8% | ✅ |
| Xavier Edwards | Hits | Over | 0.5 | -258 | 73% | 0 | -2.0% | ❌ |
| Kyle Isbel | RBI | Under | 0.5 | -420 | 81% | 2 | -0.1% | ❌ |
| Isaac Collins | RBI | Under | 0.5 | -363 | 79% | 0 | +2.3% | ✅ |
| Taylor Ward | RBI | Under | 0.5 | -318 | 76% | 0 | -1.8% | ✅ |
| Jake Rogers | RBI | Under | 0.5 | -376 | 79% | 2 | -1.5% | ❌ |
| Leody Taveras | RBI | Over | 0.5 | +251 | 28% | 0 | -8.6% | ❌ |
| Corey Seager | RBI | Under | 0.5 | -256 | 72% | 0 | +3.9% | ✅ |
| Nick Loftin | RBI | Under | 0.5 | -377 | 79% | 0 | +2.9% | ✅ |
| Lawrence Butler | RBI | Under | 0.5 | -303 | 75% | 0 | +2.9% | ✅ |
| Mike Yastrzemski | RBI | Over | 0.5 | +420 | 19% | 0 | — | ❌ |
| Henry Davis | RBI | Under | 0.5 | -404 | 79% | 0 | +1.6% | ✅ |
| TJ Rumfield | Hits | Over | 0.5 | -269 | 72% | 0 | +0.1% | ❌ |
| Wyatt Langford | RBI | Under | 0.5 | -288 | 73% | 1 | -0.1% | ❌ |
| Nathan Lukes | RBI | Under | 0.5 | -450 | 81% | 0 | +0.8% | ✅ |
| Michael Conforto | RBI | Under | 0.5 | -379 | 78% | 0 | -0.8% | ✅ |
| Patrick Bailey | RBI | Under | 0.5 | -252 | 71% | 3 | -1.4% | ❌ |
| Randy Arozarena | RBI | Under | 0.5 | -261 | 71% | 1 | +2.7% | ❌ |
| Cam Smith | RBI | Under | 0.5 | -285 | 73% | 0 | +2.1% | ✅ |
| Henry Bolte | RBI | Over | 0.5 | +271 | 26% | 0 | -3.6% | ❌ |
| Teoscar Hernandez | RBI | Under | 0.5 | -296 | 74% | 0 | -1.1% | ✅ |
| Drew Gilbert | RBI | Under | 0.5 | -368 | 77% | 2 | +2.7% | ❌ |
| Luke Keaschall | RBI | Under | 0.5 | -358 | 76% | 0 | +3.4% | ✅ |
| Jake Cronenworth | RBI | Under | 0.5 | -358 | 76% | 0 | +1.3% | ✅ |
| Tim Tawa | RBI | Under | 0.5 | -288 | 72% | 1 | -1.2% | ❌ |
| Colton Cowser | RBI | Under | 0.5 | -380 | 77% | 0 | +3.0% | ✅ |
| A.J. Ewing | RBI | Under | 0.5 | -393 | 78% | 0 | +0.2% | ✅ |
| Yainer Diaz | RBI | Under | 0.5 | -301 | 73% | 0 | -2.5% | ✅ |
| Salvador Perez | RBI | Under | 0.5 | -273 | 71% | 0 | -0.1% | ✅ |
| Owen Caissie | RBI | Under | 0.5 | -288 | 72% | 0 | +3.0% | ✅ |
| Gunnar Henderson | RBI | Under | 0.5 | -256 | 70% | 0 | +2.5% | ✅ |
| Justin Crawford | RBI | Under | 0.5 | -390 | 78% | 1 | -2.3% | ❌ |
| Moises Ballesteros | RBI | Under | 0.5 | -410 | 78% | 0 | -2.6% | ✅ |
| Trea Turner | Hits | Under | 1.5 | -266 | 71% | 0 | -4.1% | ✅ |
| Luis Robert Jr. | RBI | Under | 0.5 | -312 | 74% | 0 | +1.8% | ✅ |
| Andrew Vaughn | RBI | Under | 0.5 | -342 | 75% | 1 | — | ❌ |
| Otto Lopez | RBI | Under | 0.5 | -290 | 72% | 1 | -4.5% | ❌ |
| Francisco Lindor | RBI | Under | 0.5 | -264 | 70% | 0 | +0.6% | ✅ |
| Mookie Betts | RBI | Under | 0.5 | -257 | 69% | 2 | -1.2% | ❌ |
| Tommy Edman | RBI | Under | 0.5 | -317 | 73% | 0 | +0.6% | ✅ |
| Everson Pereira | RBI | Over | 0.5 | +338 | 22% | 0 | -4.8% | ❌ |
| Jackson Holliday | RBI | Over | 0.5 | +267 | 26% | 1 | -0.8% | ✅ |
| Javier Sanoja | RBI | Over | 0.5 | +253 | 27% | 2 | — | ✅ |
| Ernie Clement | RBI | Over | 0.5 | +305 | 23% | 0 | +15.1% | ❌ |
| Matt McLain | RBI | Over | 0.5 | +265 | 25% | 0 | -0.3% | ❌ |
| Marcus Semien | RBI | Over | 0.5 | +265 | 25% | 1 | +7.3% | ✅ |
| Gary Sanchez | RBI | Over | 0.5 | +263 | 25% | 0 | — | ❌ |
| Donovan Walton | RBI | Over | 0.5 | +321 | 22% | 0 | -3.7% | ❌ |
| Brett Baty | RBI | Over | 0.5 | +289 | 23% | 2 | +9.9% | ✅ |
| Jake Mangum | RBI | Over | 0.5 | +394 | 18% | 0 | -4.6% | ❌ |
| Josh Lowe | RBI | Over | 0.5 | +309 | 22% | 0 | -2.4% | ❌ |
| Jared Young | RBI | Over | 0.5 | +258 | 25% | 0 | +8.5% | ❌ |
| Jacob Gonzalez | RBI | Over | 0.5 | +313 | 22% | 0 | -5.1% | ❌ |
| Spencer Jones | RBI | Over | 0.5 | +261 | 24% | 2 | +12.5% | ✅ |
| Evan Carter | RBI | Over | 0.5 | +340 | 19% | 0 | -1.8% | ❌ |
| Jesus Sanchez | RBI | Over | 0.5 | +317 | 20% | 0 | +13.0% | ❌ |

*Bold = cleared its edge and EV gate.*

**NRFI / YRFI forced calls**

| Game | Call | Confidence | Model | Market | Result |
|---|---|---|---|---|---|
| Atlanta Braves @ Milwaukee Brewers | **YRFI** | High | 56% | 38% | ❌ |
| St. Louis Cardinals @ Philadelphia Phillies | **YRFI** | High | 58% | 46% | ✅ |
| San Francisco Giants @ Boston Red Sox | **YRFI** | High | 61% | 42% | ❌ |
| Tampa Bay Rays @ Baltimore Orioles | **YRFI** | High | 59% | 50% | ✅ |
| New York Mets @ Chicago White Sox | **YRFI** | High | 63% | 45% | ❌ |
| Athletics @ Houston Astros | **YRFI** | High | 78% | 50% | ❌ |
| Cleveland Guardians @ Colorado Rockies | **YRFI** | High | 62% | 53% | ✅ |
| Cincinnati Reds @ Arizona Diamondbacks | **YRFI** | High | 67% | 47% | ✅ |
| Minnesota Twins @ San Diego Padres | **YRFI** | High | 67% | — | ✅ |
| Chicago Cubs @ Seattle Mariners | **YRFI** | High | 74% | 46% | ✅ |
| Detroit Tigers @ Kansas City Royals | **YRFI** | Medium | 51% | 46% | ❌ |
| Pittsburgh Pirates @ Los Angeles Dodgers | **NRFI** | Medium | 60% | 53% | ❌ |
| Toronto Blue Jays @ New York Yankees | **NRFI** | Coin flip | 51% | 55% | ✅ |
| Washington Nationals @ Miami Marlins | **NRFI** | Coin flip | 52% | 52% | ✅ |
| Los Angeles Angels @ Texas Rangers | **NRFI** | Coin flip | 55% | 53% | ✅ |

**HR board — top 10**

| # | Player | Game | P(HR) | Result |
|---|---|---|---|---|
| 1 | Munetaka Murakami | New York Mets @ Chicago White Sox | 28% | ❌ |
| 2 | Ben Rice | Toronto Blue Jays @ New York Yankees | 27% | ❌ |
| 3 | Kyle Schwarber | St. Louis Cardinals @ Philadelphia Phillies | 27% | ❌ |
| 4 | Luis García Jr. | Toronto Blue Jays @ New York Yankees | 24% | ❌ |
| 5 | Yordan Alvarez | Athletics @ Houston Astros | 22% | ❌ |
| 6 | Colson Montgomery | New York Mets @ Chicago White Sox | 22% | ✅ |
| 7 | Miguel Vargas | New York Mets @ Chicago White Sox | 22% | ✅ |
| 8 | Pete Alonso | Tampa Bay Rays @ Baltimore Orioles | 21% | ✅ |
| 9 | Paul Goldschmidt | Toronto Blue Jays @ New York Yankees | 21% | ❌ |
| 10 | Nathaniel Lowe | Cleveland Guardians @ Colorado Rockies | 21% | ❌ |

*3 homered · model expected 2.3*

> **CLV caveat.** Beating the close is evidence of skill only when the move came from the market re-evaluating information we also had. If a scratch or injury broke after we locked, we collect the CLV without having known anything — that is luck wearing the costume of skill. Read CLV in aggregate, never on a single bet.

> CLV is the signal that matters here, not W-L — per the sharp-bettor method, beating the closing line is what indicates a real edge. A small sample of wins with negative CLV is luck, not edge.

### Moneyline probability calibration (Model A, n=362)

Brier score: **0.2437** (0.25 = coin flip knowledge; lower is better)

| Model home-win band | n | Predicted avg | Actual home-win % |
|---|---|---|---|
| 0%–40% | 49 | 36% | 37% |
| 40%–45% | 57 | 43% | 46% |
| 45%–50% | 61 | 47% | 39% |
| 50%–55% | 50 | 52% | 44% |
| 55%–60% | 61 | 58% | 66% |
| 60%–65% | 44 | 62% | 57% |
| 65%+ | 40 | 69% | 65% |

> Calibrated = predicted ≈ actual per band. Systematic gaps mean the win probabilities themselves need retuning before any ML edge claim.

### Model A — segments (finding the winning slice)

- **by market:** Moneyline 212-150 (+2%, CLV -3.9%)  ·  NRFI 6-5 (+1%, CLV -4.0%)  ·  Run Line 42-48 (-2%)  ·  Total 86-89 (-4%, CLV +0.8%)  ·  F5 Total 14-20 (-28%, CLV -2.5%)
- **by side:** Under 61-55 (+1%, CLV +1.5%)  ·  team 274-223 (-0%, CLV -3.5%)  ·  Over 25-34 (-16%, CLV +0.4%)
- **by fav_band:** unknown 20-14 (+12%)  ·  pickem 183-163 (+1%, CLV +0.2%)  ·  fav 106-77 (-5%, CLV -7.7%)  ·  dog 29-46 (-7%, CLV -1.9%)  ·  heavy fav 22-12 (-8%, CLV -1.7%)

### Model B — segments (finding the winning slice)

- **by market:** Total 64-49 (+9%)  ·  Moneyline 142-101 (+4%)  ·  Run Line 31-41 (-7%)
- **by side:** Over 13-7 (+24%)  ·  Under 51-42 (+6%)  ·  team 173-142 (+1%)
- **by fav_band:** pickem 129-98 (+9%)  ·  fav 68-40 (+4%)  ·  dog 27-40 (-5%)  ·  unknown 2-3 (-24%)  ·  heavy fav 11-10 (-26%)

## Model A — picks by date

### 2026-08-24 — 3-2  (+0.41u)

| Result | Verdict | Game | Market | Pick | Line | Books (best in bold) | CLV | P/L |
|---|---|---|---|---|---|---|---|---|
| ✅ WIN | LEAN | Chicago Cubs @ Arizona Diamondbacks | Moneyline | Chicago Cubs ML | — | **FanDuel -142** / DraftKings -150 | -11.5% | +0.70 |
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
