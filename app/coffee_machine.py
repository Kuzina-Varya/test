class CoffeeMachine:
    CAPPUCCINO_MILK_ML = 100

    def __init__(self, milk_ml: int) -> None:
        self.milk_ml = milk_ml
        self.message = ""

    def make_cappuccino(self) -> bool:
        """Готовит капучино, если в кофемашине достаточно молока."""
        if self.milk_ml < self.CAPPUCCINO_MILK_ML:
            self.message = "Недостаточно молока"
            return False

        self.milk_ml -= self.CAPPUCCINO_MILK_ML
        self.message = "Капучино готов"
        return True
