from typing import Optional

import pandas as pd

from ...features.states import classify_trend_chop
from .decision_record import DecisionRecord
from .selector import Selector

MIN_COLORS_REQUIRED = 2


class Engine:
    """Flip-only engine: long on GREEN, short on RED, exit/reverse on opposite flip."""

    def __init__(self) -> None:
        self.selector = Selector()
        self.position: Optional[str] = None  # 'LONG' | 'SHORT' | None

    def _current_flip(self, colors: pd.Series) -> Optional[str]:

        if len(colors) < MIN_COLORS_REQUIRED:
            return None
        prev, curr = colors.iloc[-2], colors.iloc[-1]
        if prev != curr and curr in ("GREEN", "RED"):
            return "LONG" if curr == "GREEN" else "SHORT"
        return None

    def on_bar_close(self, df: pd.DataFrame) -> Optional[DecisionRecord]:
        if len(df) == 0:
            return None
        # 1) Classify market state (TREND/CHOP)
        market_state = classify_trend_chop(df).iloc[-1]
        # 2) Choose combo based on state
        combo_name, combo = self.selector.choose(market_state)
        # 3) Compute regime colors
        colors = combo.regime(df)
        # 4) Detect flip
        flip = self._current_flip(colors)
        if flip is None:
            return None
        # 5) Produce decision record (execution routed elsewhere)
        record = DecisionRecord(
            ts=str(df.index[-1]),
            market_state=market_state,
            combo_used=combo_name,
            reason={
                "prev_color": colors.iloc[-2],
                "curr_color": colors.iloc[-1],
                "flip": flip,
            },
        )
        # Update position (for paper model this would trigger reverse)
        self.position = flip
        return record
