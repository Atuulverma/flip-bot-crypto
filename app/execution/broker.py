from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderResult:
    ok: bool
    order_id: Optional[str] = None
    message: str = ""


class PaperBroker:
    """Simulate fills; for now assume immediate fill."""

    def place_order(self, side: str, qty: float, price: float | None = None) -> OrderResult:
        return OrderResult(ok=True, order_id="paper-123")


class LiveBroker:
    """Integrate with Delta's Python API in later commits."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

    def place_order(self, side: str, qty: float, price: float | None = None) -> OrderResult:
        # TODO: Implement actual REST call with rounding and idempotency
        return OrderResult(ok=False, message="Not implemented")
