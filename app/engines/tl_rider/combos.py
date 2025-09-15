from typing import Literal

import pandas as pd

from ...features.builders_core import adx, ema
from ...features.builders_supertrend import supertrend_direction

ComboName = Literal["B", "C", "D"]


class Combo:
    def regime(self, df: pd.DataFrame) -> pd.Series:
        """Return series of 'GREEN'|'RED'|'GRAY' for each bar."""
        raise NotImplementedError


class ComboB(Combo):  # Supertrend-only
    def __init__(self, period: int = 10, multiplier: float = 3.0) -> None:
        self.period = period
        self.multiplier = multiplier

    def regime(self, df: pd.DataFrame) -> pd.Series:
        d = supertrend_direction(df, self.period, self.multiplier)
        return d.map({1: "GREEN", -1: "RED", 0: "GRAY"})


class ComboC(Combo):  # Supertrend + EMA20>EMA50 alignment
    def __init__(self, period: int = 10, multiplier: float = 3.0) -> None:
        self.period = period
        self.multiplier = multiplier

    def regime(self, df: pd.DataFrame) -> pd.Series:
        d = supertrend_direction(df, self.period, self.multiplier)
        e20 = ema(df, 20)
        e50 = ema(df, 50)
        out = []
        for i in range(len(df)):
            if d.iloc[i] == 1 and e20.iloc[i] > e50.iloc[i]:
                out.append("GREEN")
            elif d.iloc[i] == -1 and e20.iloc[i] < e50.iloc[i]:
                out.append("RED")
            else:
                out.append("GRAY")
        return pd.Series(out, index=df.index)


class ComboD(Combo):  # Supertrend + ADX filter
    def __init__(self, period: int = 10, multiplier: float = 3.0, adx_floor: int = 18) -> None:
        self.period = period
        self.multiplier = multiplier
        self.adx_floor = adx_floor

    def regime(self, df: pd.DataFrame) -> pd.Series:
        d = supertrend_direction(df, self.period, self.multiplier)
        a = adx(df, 14)
        out = []
        for i in range(len(df)):
            if a.iloc[i] >= self.adx_floor:
                out.append("GREEN" if d.iloc[i] == 1 else "RED")
            else:
                out.append("GRAY")
        return pd.Series(out, index=df.index)
