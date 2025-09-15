import json
from typing import Any

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API keys
    # --- Delta Exchange API
    DELTA_REGION: str = "india"
    DELTA_BASE_URL: str = "https://api.india.delta.exchange"
    DELTA_WS_URL: str = "wss://socket.india.delta.exchange"
    DELTA_API_KEY: str = "zpNEp3PxUL1e7qNIOAiAIzVa3PFwBl"
    DELTA_API_SECRET: str = "tE3IvuF7hLUsNRvNFs3vVrxZF7VoV9pxa0692iOMMhfp9bkkBJyabqhoAAXz"

    # Universe
    SYMBOLS: str = "SOLUSD"
    RESOLUTIONS: str = "5m"

    # Risk & sizing
    LEVERAGE_DEFAULT: int = 5
    CAPITAL_ALLOC_PCT_PER_TRADE: float = 0.05
    MAX_DAILY_LOSS_PCT: float = 0.02

    # Trader knobs
    CATASTROPHE_SL_ENABLE: bool = False
    CATASTROPHE_SL_ATR_MULT: float = 2.5

    # Supertrend presets (per symbol; JSON string)
    SUPERTREND_PRESETS_RAW: str = '{"SOLUSD": {"period": 10, "multiplier": 3.0}}'

    # Context behavior
    CONTEXT_VETO_STRICT: bool = False

    def supertrend_preset(self) -> dict[str, dict[str, Any]]:
        try:
            return json.loads(self.SUPERTREND_PRESETS_RAW)
        except Exception:
            return {"SOLUSD": {"period": 10, "multiplier": 3.0}}


settings = Settings()  # type: ignore
