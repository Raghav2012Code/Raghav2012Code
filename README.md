# Raghav Krishna

Robotics and web, built in Chennai. ESP32 hardware, ML pipelines, and full-stack apps, most of it deployed.

I lead a two-person team, and I keep coming back to the same kind of problem: something specific to a place. A rooftop solar market in Chennai. A vaccine cold chain. The junctions where traffic accidents cluster.

**[raghavkrishna-dev.vercel.app](https://raghavkrishna-dev.vercel.app)**

## Competitions

| Project | Event | Result |
| :--- | :--- | :--- |
| **CRASH** | ZRC Technoxian 2026 | **Top 5**, qualified for NRC (Delhi) |
| **Volt** | Shark Tank Challenge 2026 | Participated |
| **Apex GP** | Technoviz | Participated |

## Team projects

I lead these with one other developer. Every commit count below covers the complete repository history.

### [Volt](https://github.com/abivan100-stack/volt-ledger)
Peer-to-peer rooftop solar trading

[![Live](https://img.shields.io/badge/live-volt--ledger.vercel.app-2ea44f)](https://volt-ledger.vercel.app)
[![Repo](https://img.shields.io/badge/repo-abivan100-stack/volt--ledger-8b949e)](https://github.com/abivan100-stack/volt-ledger)

India's grid buys rooftop surplus at roughly ₹3.00/kWh and resells it next door at ₹8.00. Volt clears the same trade near ₹5.50, so the value stays on the street. Every trade is sealed into a SHA-256 chain computed in the browser. Edit any past entry and that block, plus every block after it, fails verification.

`78 of 251 commits`

### [Vault](https://github.com/abivan100-stack/vault)
Vaccine cold chain ledger

[![Repo](https://img.shields.io/badge/repo-abivan100-stack/vault-8b949e)](https://github.com/abivan100-stack/vault)

A monitoring console for one vaccine shipment, from loading bay to handoff. A simulator drives the temperature feed, and the hash chain underneath it is real. Every event commits to `sequence + event + timestamp + detail + prevHash` under SHA-256, so the record verifies after the fact. The README draws the line precisely: verification proves that stored entries were never edited or reordered, and it says nothing about whether a reading was true. The exported PDF repeats that caveat on every page.

`41 of 101 commits`

### [CRASH](https://github.com/abivan100-stack/C.R.A.S.H)
Road accident hotspot mapping

[![Repo](https://img.shields.io/badge/repo-abivan100-stack/C.R.A.S.H-8b949e)](https://github.com/abivan100-stack/C.R.A.S.H)

Maps accidents across Greater Chennai, ranks the deadliest junctions by severity-weighted risk, and turns each hotspot into an intervention recommendation. The README publishes a correction with the measured numbers: fatal share is 6.2% at night against 6.3% by day, which retired an earlier claim about weather and visibility.

`7 of 94 commits`

### [Apex GP](https://github.com/Raghav2012Code/f1-team-dashboard)
F1 race strategy dashboard

[![Live](https://img.shields.io/badge/live-f1--team--dashboard.vercel.app-2ea44f)](https://f1-team-dashboard.vercel.app)
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/f1--team--dashboard-8b949e)](https://github.com/Raghav2012Code/f1-team-dashboard)

A live race desk for the Belgian Grand Prix: a moving 20-car field, tyre strategy, race control, and analytics. Built with vanilla HTML, CSS, and JavaScript, so there is no build step. Circuit data drives the weather, dates, and lap badges, so switching to another Grand Prix moves the whole interface with it.

## Solo projects

### [EPL Predictor](https://github.com/Raghav2012Code/epl-predictor)
Match outcome forecasting

[![Live](https://img.shields.io/badge/live-epl--predictor.vercel.app-2ea44f)](https://epl-predictor-van-89de.vercel.app)
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/epl--predictor-8b949e)](https://github.com/Raghav2012Code/epl-predictor)

Calibrated Home/Draw/Away probabilities for the 2026/27 Premier League. A stacked ensemble of tuned Random Forest, XGBoost, logistic regression, and Elo-Poisson members, benchmarked with time-ordered validation, with production selected by Ranked Probability Score. The test suite asserts zero temporal leakage: no match sees a result from its own date or any later one, and odds frames are gated to pre-kickoff fields.

`172 commits`, MIT, [CI](https://github.com/Raghav2012Code/epl-predictor/actions)

### [Urbania](https://github.com/Raghav2012Code/urbania)
2D city simulation

[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/urbania-8b949e)](https://github.com/Raghav2012Code/urbania)

C++17 with raylib. A road network with A* pathfinding, citizen employment matching, pollution diffusion, land value, happiness, and a public transit foundation. The simulation clock advances independently of frame rate, so pause and fast-forward stay consistent across every system. The roadmap lists bus vehicle movement, transit ridership, trains, and save/load as still to come.

`44 commits`, MIT

### [Diecastly](https://github.com/Raghav2012Code/diecastly)
D2C inventory and point of sale

[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/diecastly-8b949e)](https://github.com/Raghav2012Code/diecastly)

Built for a small diecast collectibles business where most sales happen by hand, in cash or UPI, and only 10 to 15 percent need shipping. The database is the source of truth: stock, orders, and payments move only through `security definer` RPCs, and payment state is derived from an append-only ledger at read time. Guest order access requires both the order number and a 122-bit token, and phone or email carries no access.

`37 commits`, MIT

## Other work

- [dev-portfolio](https://github.com/Raghav2012Code/dev-portfolio): the source of this page
- [ariadne-](https://github.com/Raghav2012Code/ariadne-): pathfinding visualizer with 7 search algorithms
- [brew-and-co](https://github.com/Raghav2012Code/brew-and-co): coffee roastery storefront and subscriptions
- [productivity-hub](https://github.com/Raghav2012Code/productivity-hub): local-first habits, tasks, and focus timer
- [kanban](https://github.com/Raghav2012Code/kanban): local-first Kanban board
- [sort-pulse](https://github.com/Raghav2012Code/sort-pulse): sorting algorithm visualizer with telemetry
- [lebron-fan-page](https://github.com/Raghav2012Code/lebron-fan-page): a LeBron James fan tribute

## Contact

- GitHub: [@Raghav2012Code](https://github.com/Raghav2012Code)
- Email: [raghavgamerz670@gmail.com](mailto:raghavgamerz670@gmail.com)
- Portfolio: [raghavkrishna-dev.vercel.app](https://raghavkrishna-dev.vercel.app)

Topics on this page: `profile` `readme` `robotics` `esp32` `ml` `chennai`
