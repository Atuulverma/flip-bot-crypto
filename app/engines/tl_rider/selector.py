from .combos import Combo, ComboB, ComboC, ComboD, ComboName


class Selector:
    def __init__(self) -> None:
        self.b: Combo = ComboB()
        self.c: Combo = ComboC()
        self.d: Combo = ComboD()

    def choose(self, market_state: str) -> tuple[ComboName, Combo]:
        if market_state == "TREND":
            return "B", self.b
        return "C", self.c  # fallback to D handled in engine if needed
