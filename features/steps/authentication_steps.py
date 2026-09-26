from behave import given, then, when

from app.auth import Account


@given('существует активный аккаунт пользователя с паролем "{password}"')
def step_active_account(context, password):
    context.account = Account(password)


@when("пользователь вводит неверный пароль {attempts:d} раза")
def step_user_enters_wrong_password(context, attempts):
    for _ in range(attempts):
        context.login_success = context.account.authenticate("wrong-password")
    context.message = context.account.message


@then("аккаунт пользователя заблокирован")
def step_account_is_locked(context):
    assert context.account.locked is True


@then('последующая попытка входа с паролем "{password}" отклоняется')
def step_valid_password_is_rejected(context, password):
    context.login_success = context.account.authenticate(password)
    context.message = context.account.message
    assert context.login_success is False
