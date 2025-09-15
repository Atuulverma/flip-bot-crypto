from dataclasses import dataclass
from typing import Any


@dataclass
class DecisionRecord:
    ts: str
    market_state: str
    combo_used: str
    reason: dict[str, Any]
