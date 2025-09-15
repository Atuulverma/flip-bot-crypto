from pydantic_settings import BaseSettings
from typing import Dict, Any
import json

class Settings(BaseSettings):
    DELTA_API_KEY: str = ""
    DELTA_API_SECRET: str = ""

    SYMBOLS: str = "SOLUSD"
    RESOLUTIONS: str = "5m"

    LEVERAGE_DEFAULT: int = 5
    CAPITAL_ALLOC_PCT_PER_TRADE: float = 0.05
    MAX_DAILY_LOSS_PCT: float = 0.02

    CATASTROPHE_SL_ENABLE: bool = False
    CATASTROPHE_SL_ATR_MULT: float = 2.5

    SUPERTREND_PRESETS_RAW: str = '{"SOLUSD": {"period": 10, "multiplier": 3.0}}'

    CONTEXT_VETO_STRICT: bool = False

    def supertrend_preset(self) -> Dict[str, Dict[str, Any]]:
        try:
            return json.loads(self.SUPERTREND_PRESETS_RAW)
        except Exception:
            return {"SOLUSD": {"period": 10, "multiplier": 3.0}}

settings = Settings()  # type: ignore
