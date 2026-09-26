from dataclasses import dataclass


@dataclass(frozen=True)
class LoginResult:
    success: bool
    message: str


class Account:
    def __init__(self, password: str) -> None:
        self._password = password
        self.failed_attempts = 0
        self.locked = False

    def authenticate(self, password: str) -> LoginResult:
        if self.locked:
            return LoginResult(False, "Аккаунт заблокирован")

        if password == self._password:
            self.failed_attempts = 0
            return LoginResult(True, "Вход выполнен")

        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.locked = True
            return LoginResult(False, "Аккаунт заблокирован")

        return LoginResult(False, "Неверный пароль")
