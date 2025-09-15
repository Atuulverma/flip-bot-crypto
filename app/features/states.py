import pandas as pd

from .builders_core import adx, ema


def classify_trend_chop(df: pd.DataFrame) -> pd.Series:
    """Simple TREND/CHOP classifier: TREND if ADX>=20 and EMA20 slope strong.
    Placeholder; refine later.
    """
    if len(df) == 0:
        return pd.Series([], dtype=object)
    adx14 = adx(df, 14)
    ema20 = ema(df, 20)
    slope = ema20.diff()
    strong = slope.abs() >= slope.abs().rolling(100, min_periods=20).median()
    ADX14_MIN = 20
    trend = (adx14 >= ADX14_MIN) & strong
    return pd.Series(["TREND" if t else "CHOP" for t in trend], index=df.index)
