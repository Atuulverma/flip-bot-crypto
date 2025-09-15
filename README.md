# flip-bot-crypto

Flip-only trendline engine for Delta Exchange. Professional, modular skeleton with CI gates.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # edit keys later
uvicorn app.main:app --reload
# visit http://127.0.0.1:8000/health


# flip-bot-crypto

Flip-only trendline engine for Delta Exchange. Modular, data-first design.

## Quick start (dev)
- Create and fill `.env` from `.env.example`.
- `pip install -r requirements.txt`
- `pytest`
- `uvicorn app.main:app --reload` (API skeleton)
```
