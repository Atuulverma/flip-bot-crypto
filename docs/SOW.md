Here’s the one-page Statement of Work (SOW) for your new crypto bot, incorporating all requirements and the Trader Critique knobs you asked for.

⸻

Statement of Work (SOW) — Crypto Flip Engine Bot

Objective

Deliver a modular, professional-grade crypto trading bot for Delta Exchange, focused on a flip-only trendline strategy (green = long, red = short, reverse on flip). System to be data-rich, configurable, and safe for novice operators.

⸻

Scope

1. Data & Features
	•	365 days backfill per symbol (OHLCV, MARK, OI, Funding).
	•	Live feeds (REST + WS): OHLCV, orderbook depth, trades, OI.
	•	Feature bus with aligned vectors:
	•	Supertrend, EMA20/50, ADX, ATR, RSI, MACD, BB/Keltner widths.
	•	OI momentum, Funding z-score, Mark-premium.
	•	Orderbook imbalance, tape delta.

2. Engine
	•	TL-Rider (flip-only) engine:
	•	TREND regime → Supertrend-only.
	•	CHOP regime → Supertrend+EMA confirm, fallback to Supertrend+ADX.
	•	Decision record per trade: features, regime, combo, reason codes.
	•	Trader Critique knobs (configurable in settings.py):
	•	CATASTROPHE_SL_ENABLE (bool) → if true, apply 2–3× ATR hard stop.
	•	SUPERTREND_PRESETS (dict) → per-symbol parameters.
	•	CONTEXT_VETO_STRICT (bool) → if false, OI/Funding/Mark only down-weight or delay TREND entries (never veto).

3. Trading Modes
	•	Paper Trade:
	•	Configurable starting balance (default = Delta wallet).
	•	Reset to wallet balance option.
	•	Isolated ledger & PnL tracking.
	•	Live Trade:
	•	Orders via Delta Python API (tick/step rounding, fee/slip).
	•	Kill-switch + idempotent client IDs.
	•	Filter: dashboard toggle for Paper vs Live trades & PnL.

4. UI & UX
	•	Dashboard (React/Dash):
	•	Status bar (WS health, engine state, PnL today/7d).
	•	Chart: candles, regime ribbons, flips, indicators.
	•	Trades table with filters.
	•	Config pages: symbol mgmt, risk, paper wallet, logs purge.
	•	User presets: Conservative / Balanced / Aggressive.
	•	First-run wizard for novice onboarding.

5. Risk & Safety
	•	Circuit-breakers: kill-switch, max daily loss, flip-frequency guard.
	•	Config immutability in Live (arm-change workflow).
	•	Catastrophe SL knob-driven.

6. Observability
	•	Structured logs (JSON).
	•	Metrics for Grafana/ELK: flips, latency, error rates, drawdowns.
	•	Controls: purge logs, purge paper trades, reindex data.

7. Quality & Standards
	•	Code: ruff, black, mypy.
	•	Tests: unit, integration, deterministic backtest.
	•	File discipline: ≤ 400 LOC typical, ≤ 800 LOC max.
	•	CI/CD: GitHub Actions with artifacts (docker/wheel), staged deploys.

⸻

Deliverables
	1.	Engine package engines/tl_rider/ with combos B, C, D, config knobs.
	2.	Dashboard UI with Paper/Live toggle, trade filters, symbol mgmt.
	3.	Backfill + WS system with 365d ready-state.
	4.	Observability stack with logs & Grafana/ELK.
	5.	Runbook & wizard for novice users.

⸻

Acceptance
	•	Engine produces deterministic Paper backtests with logged decision records.
	•	Live orders place successfully with proper rounding and safety checks.
	•	Catastrophe SL, ST presets, Context veto all knob-driven.
	•	Paper/Live PnL separable, resettable.
	•	Dashboard shows accurate state, trades, and PnL.

⸻

⚡ Verdict: This bot is modular, professional, and trader-first, with configurable safety knobs, fool-proof UX, and standards-compliant code.
