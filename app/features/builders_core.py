import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD, ADXIndicator, EMAIndicator
from ta.volatility import AverageTrueRange, BollingerBands, KeltnerChannel


def ema(df: pd.DataFrame, span: int, col: str = "close") -> pd.Series:
    return EMAIndicator(close=df[col], window=span).ema_indicator()


def adx(df: pd.DataFrame, length: int = 14) -> pd.Series:
    ind = ADXIndicator(high=df["high"], low=df["low"], close=df["close"], window=length)
    return ind.adx()


def atr(df: pd.DataFrame, length: int = 14) -> pd.Series:
    return AverageTrueRange(
        high=df["high"], low=df["low"], close=df["close"], window=length
    ).average_true_range()


def rsi(df: pd.DataFrame, length: int = 14) -> pd.Series:
    return RSIIndicator(close=df["close"], window=length).rsi()


def macd_hist(df: pd.DataFrame) -> pd.Series:
    macd = MACD(close=df["close"])
    return macd.macd_diff()


def bb_width(df: pd.DataFrame, window: int = 20) -> pd.Series:
    bb = BollingerBands(close=df["close"], window=window)
    return (bb.bollinger_hband() - bb.bollinger_lband()) / df["close"]


def keltner_width(df: pd.DataFrame, window: int = 20) -> pd.Series:
    kc = KeltnerChannel(high=df["high"], low=df["low"], close=df["close"], window=window)
    return (kc.keltner_channel_hband() - kc.keltner_channel_lband()) / df["close"]
