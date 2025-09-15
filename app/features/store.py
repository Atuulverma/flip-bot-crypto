import pandas as pd


class FeatureStore:
    """Minimal store mapping keys -> DataFrames (bar-aligned)."""

    def __init__(self) -> None:
        self.frames: dict[str, pd.DataFrame] = {}

    def put(self, key: str, df: pd.DataFrame) -> None:
        self.frames[key] = df

    def get(self, key: str) -> pd.DataFrame:
        return self.frames[key]
