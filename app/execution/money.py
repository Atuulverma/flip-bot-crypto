from dataclasses import dataclass
from math import floor


@dataclass
class SizingConfig:
    leverage: int
    capital_pct: float
    min_qty: float = 0.1
    step_size: float = 0.1


def compute_order_qty(equity_usd: float, price: float, cfg: SizingConfig) -> float:
    """Compute position size using % capital and leverage, rounded to step.

    qty = (equity * pct * leverage) / price
    """
    notional = equity_usd * cfg.capital_pct * cfg.leverage
    raw_qty = 0.0 if price <= 0 else (notional / price)
    steps = floor(raw_qty / cfg.step_size)
    qty = max(cfg.min_qty, steps * cfg.step_size)
    return qty
