# app/features/builders_supertrend.py
import pandas as pd


def _roll_upper(prev_close: float, prev_final_upper: float, basic_upper_i: float) -> float:
    # Supertrend rolling rule for upper band
    if prev_close <= prev_final_upper:
        return min(basic_upper_i, prev_final_upper)
    return basic_upper_i


def _roll_lower(prev_close: float, prev_final_lower: float, basic_lower_i: float) -> float:
    # Supertrend rolling rule for lower band
    if prev_close >= prev_final_lower:
        return max(basic_lower_i, prev_final_lower)
    return basic_lower_i


def _next_dir(
    prev_dir: int, close_i: float, final_upper_i: float, final_lower_i: float
) -> tuple[int, float]:
    # Compute next direction and supertrend value for bar i
    if prev_dir == 1:
        st_i = final_lower_i
        if close_i < st_i:
            return -1, final_upper_i
        return 1, st_i
    else:
        st_i = final_upper_i
        if close_i > st_i:
            return 1, final_lower_i
        return -1, st_i


def supertrend_direction(df: pd.DataFrame, period: int, multiplier: float) -> pd.Series:
    """
    Return +1 for uptrend, -1 for downtrend, 0 for undefined using a simple Supertrend.
    Bar-close calculation; no future leak.
    """
    if len(df) == 0:
        return pd.Series([], dtype=int)

    hl2 = (df["high"] + df["low"]) / 2.0

    # True range and ATR
    tr = pd.concat(
        [
            df["high"] - df["low"],
            (df["high"] - df["close"].shift()).abs(),
            (df["low"] - df["close"].shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)
    atr = tr.rolling(period, min_periods=period).mean()

    basic_upper = hl2 + multiplier * atr
    basic_lower = hl2 - multiplier * atr

    final_upper = basic_upper.copy()
    final_lower = basic_lower.copy()

    # Roll final bands
    for i in range(1, len(df)):
        prev_close = df["close"].iloc[i - 1]
        final_upper.iloc[i] = _roll_upper(prev_close, final_upper.iloc[i - 1], basic_upper.iloc[i])
        final_lower.iloc[i] = _roll_lower(prev_close, final_lower.iloc[i - 1], basic_lower.iloc[i])

    # Direction & ST line
    direction = [0] * len(df)
    st = [0.0] * len(df)

    direction[0] = 1  # arbitrary start
    st[0] = float(final_lower.iloc[0])

    for i in range(1, len(df)):
        direction[i], st[i] = _next_dir(
            direction[i - 1],
            float(df["close"].iloc[i]),
            float(final_upper.iloc[i]),
            float(final_lower.iloc[i]),
        )

    return pd.Series(direction, index=df.index)
