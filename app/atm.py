class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance
        self.message = ""

    def withdraw(self, amount: int) -> bool:
        """Снимает деньги, если на счете достаточно средств."""
        if amount > self.balance:
            self.message = "Недостаточно средств"
            return False

        self.balance -= amount
        self.message = "Операция выполнена"
        return True
