class Account:
    MAX_FAILED_ATTEMPTS = 3

    def __init__(self, password: str) -> None:
        self._password = password
        self.failed_attempts = 0
        self.locked = False
        self.message = ""

    def authenticate(self, password: str) -> bool:
        """Проверяет пароль и блокирует аккаунт после трех ошибок."""
        if self.locked:
            self.message = "Аккаунт заблокирован"
            return False

        if password == self._password:
            self.failed_attempts = 0
            self.message = "Вход выполнен"
            return True

        self.failed_attempts += 1
        if self.failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            self.locked = True
            self.message = "Аккаунт заблокирован"
            return False

        self.message = "Неверный пароль"
        return False
