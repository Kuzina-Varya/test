# Behave scenarios with Git pre-commit hook

This repository contains three Gherkin scenarios and minimal Python logic for:

- ATM overdraft rejection
- Account lockout after three failed login attempts
- Coffee machine rejection when there is not enough milk for cappuccino

## Run tests

```powershell
python -m behave
```

The local Git pre-commit hook also runs `python -m behave` before each commit.

The repository is configured to use `.githooks/pre-commit` as `core.hooksPath`.
