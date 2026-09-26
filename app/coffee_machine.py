from dataclasses import dataclass


@dataclass(frozen=True)
class BrewResult:
    success: bool
    message: str


class CoffeeMachine:
    CAPPUCCINO_MILK_ML = 100

    def __init__(self, milk_ml: int) -> None:
        self.milk_ml = milk_ml

    def make_cappuccino(self) -> BrewResult:
        if self.milk_ml < self.CAPPUCCINO_MILK_ML:
            return BrewResult(False, "Недостаточно молока")

        self.milk_ml -= self.CAPPUCCINO_MILK_ML
        return BrewResult(True, "Капучино готов")
