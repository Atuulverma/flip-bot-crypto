from pathlib import Path

WM_DIR = Path(".wm")


def get(symbol: str, resolution: str) -> str | None:
    p = WM_DIR / f"{symbol}_{resolution}.wm"
    if not p.exists():
        return None
    return p.read_text().strip()


def set_(symbol: str, resolution: str, value: str) -> None:
    WM_DIR.mkdir(parents=True, exist_ok=True)
    (WM_DIR / f"{symbol}_{resolution}.wm").write_text(value)
