from dataclasses import dataclass


@dataclass(frozen=True)
class WithdrawalResult:
    success: bool
    message: str


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def withdraw(self, amount: int) -> WithdrawalResult:
        if amount > self.balance:
            return WithdrawalResult(False, "Недостаточно средств")

        self.balance -= amount
        return WithdrawalResult(True, "Операция выполнена")
