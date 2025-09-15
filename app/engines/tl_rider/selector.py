# from typing import Tuple

from .combos import ComboB, ComboC, ComboD, ComboName


class Selector:
    def __init__(self) -> None:
        self.b = ComboB()
        self.c = ComboC()
        self.d = ComboD()

    def choose(self, market_state: str) -> tuple[ComboName, object]:
        if market_state == "TREND":
            return "B", self.b
        return "C", self.c  # fallback to D handled in engine if needed
