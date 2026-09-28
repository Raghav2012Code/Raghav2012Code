# Raghav Krishna

Robotics + web. ESP32 hardware, and things I deploy. Chennai, India.

Team lead on a two-person team. I work across embedded hardware, ML pipelines, and
full-stack apps — and I care most about problems that are specific to somewhere,
not generic dashboards.

**[raghavkrishna-dev.vercel.app](https://raghavkrishna-dev.vercel.app)**

## Competitions

| Project | Event | Result |
| :--- | :--- | :--- |
| **CRASH** — Chennai Road Accident Safety Hub | ZRC Technoxian 2026 | **Top 5**, qualified for NRC, Delhi |
| **Volt** — peer-to-peer rooftop solar ledger | Shark Tank Challenge 2026 | Participated |
| **Apex GP** — F1 team dashboard | Technoviz | Participated |

## Team projects

I lead these with one other developer. Commit counts below are the full
repository history, not a sample.

### [Volt](https://github.com/abivan100-stack/volt-ledger) — peer-to-peer rooftop solar trading
[![Live](https://img.shields.io/badge/live-volt--ledger.vercel.app-2ea44f)](https://volt-ledger.vercel.app)
[![Repo](https://img.shields.io/badge/repo-abivan100-stack/volt--ledger-8b949e)](https://github.com/abivan100-stack/volt-ledger)

India's grid buys rooftop surplus at roughly ₹3.00/kWh and resells it next door at
₹8.00. Volt clears the same trade near ₹5.50, so the value stays on the street.
Every trade is sealed into a SHA-256 chain computed in the browser, which makes
the ledger tamper-evident: edit any past entry and that block plus every block
after it fails verification.

`78 of 251 commits` · 2 stars

### [Vault](https://github.com/abivan100-stack/vault) — vaccine cold chain ledger
[![Repo](https://img.shields.io/badge/repo-abivan100-stack/vault-8b949e)](https://github.com/abivan100-stack/vault)

A monitoring console for a vaccine shipment's cold chain. Readings are simulated;
the ledger is not. Every event commits to `sequence + event + timestamp + detail +
prevHash` under SHA-256, so the record can be verified after the fact. The README
is explicit about the limits — tamper-*evident*, not tamper-proof, and it says so
in three places rather than claiming more than it can prove.

`41 of 101 commits` · 1 star

### [CRASH](https://github.com/abivan100-stack/C.R.A.S.H) — road accident hotspot mapping
[![Repo](https://img.shields.io/badge/repo-abivan100-stack/C.R.A.S.H-8b949e)](https://github.com/abivan100-stack/C.R.A.S.H)

Maps accidents across Greater Chennai, ranks the deadliest junctions by
severity-weighted risk, and turns each hotspot into an intervention
recommendation. The README documents a correction where earlier docs claimed a
correlation the data does not support, with the measured numbers — fatal share is
6.2% at night vs 6.3% by day.

`7 of 94 commits` · 2 stars

### [Apex GP](https://github.com/Raghav2012Code/f1-team-dashboard) — F1 race strategy dashboard
[![Live](https://img.shields.io/badge/live-f1--team--dashboard.vercel.app-2ea44f)](https://f1-team-dashboard.vercel.app)
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/f1--team--dashboard-8b949e)](https://github.com/Raghav2012Code/f1-team-dashboard)

A live race desk for the Belgian Grand Prix: moving 20-car field, tyre strategy,
race control, and analytics. Vanilla HTML/CSS/JS, no build step.

## Solo projects

### [EPL Predictor](https://github.com/Raghav2012Code/epl-predictor) — match outcome forecasting
[![Live](https://img.shields.io/badge/live-epl--predictor.vercel.app-2ea44f)](https://epl-predictor-van-89de.vercel.app)
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/epl--predictor-8b949e)](https://github.com/Raghav2012Code/epl-predictor)

Calibrated Home/Draw/Away probabilities for the 2026/27 Premier League. A stacked
ensemble — tuned Random Forest, XGBoost, logistic regression, and Elo-Poisson —
benchmarked with time-ordered validation, with production selected by Ranked
Probability Score. The test suite asserts zero temporal leakage: a match never sees
a result from the same date or later, and odds frames are gated to pre-kickoff
fields only.

`172 commits` · 1 star · MIT · [CI](https://github.com/Raghav2012Code/epl-predictor/actions)

### [Urbania](https://github.com/Raghav2012Code/urbania) — 2D city simulation
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/urbania-8b949e)](https://github.com/Raghav2012Code/urbania)

C++17 with raylib. Road network with A* pathfinding, citizen employment matching,
pollution diffusion, land value, happiness, and a public transit foundation. The
simulation clock advances independently of frame rate, so pause and fast-forward
stay consistent across every system. The README is honest that citizens, trains,
and save/load are not implemented yet.

`44 commits` · MIT

### [Diecastly](https://github.com/Raghav2012Code/diecastly) — D2C inventory and POS
[![Repo](https://img.shields.io/badge/repo-Raghav2012Code/diecastly-8b949e)](https://github.com/Raghav2012Code/diecastly)

Built for a real small business selling diecast collectibles, where most sales are
hand-to-hand cash or UPI and only 10–15% ship. The database is the source of
truth: stock, orders, and payments change only through `security definer` RPCs, and
payment state is derived from an append-only ledger rather than stored. Guest order
access needs both the order number and a 122-bit token — phone and email never
authorise.

`37 commits` · MIT

## Also

- [dev-portfolio](https://github.com/Raghav2012Code/dev-portfolio) — this site's source
- [ariadne-](https://github.com/Raghav2012Code/ariadne-) — pathfinding visualizer, 7 search algorithms
- [brew-and-co](https://github.com/Raghav2012Code/brew-and-co) · [productivity-hub](https://github.com/Raghav2012Code/productivity-hub) · [kanban](https://github.com/Raghav2012Code/kanban) · [sort-pulse](https://github.com/Raghav2012Code/sort-pulse) · [lebron-fan-page](https://github.com/Raghav2012Code/lebron-fan-page)

## Contact

- GitHub — [@Raghav2012Code](https://github.com/Raghav2012Code)
- Email — [raghavgamerz670@gmail.com](mailto:raghavgamerz670@gmail.com)
