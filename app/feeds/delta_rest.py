from typing import Any

import requests

BASE = "https://api.india.delta.exchange/v2"


class DeltaREST:
    def __init__(self, api_key: str = "", api_secret: str = "") -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()

    def candles(self, symbol: str, resolution: str, start: int, end: int) -> dict[str, Any]:
        """Fetch OHLCV/other candle series. 'symbol' can be 'SOLUSD' or 'MARK:SOLUSD', etc."""
        url = f"{BASE}/history/candles"
        params = {"symbol": symbol, "resolution": resolution, "start": start, "end": end}
        r = self.session.get(url, params=params, timeout=20)
        r.raise_for_status()
        return r.json()

    def products(self) -> dict[str, Any]:
        url = f"{BASE}/products"
        r = self.session.get(url, timeout=20)
        r.raise_for_status()
        return r.json()
