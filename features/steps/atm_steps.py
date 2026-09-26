from behave import given, then, when

from app.atm import BankAccount


@given("на счете клиента {balance:d} рублей")
def step_account_with_balance(context, balance):
    context.account = BankAccount(balance)


@when("клиент пытается снять {amount:d} рублей")
def step_client_withdraws(context, amount):
    context.operation_success = context.account.withdraw(amount)
    context.message = context.account.message


@then("банкомат отклоняет операцию")
def step_atm_rejects_operation(context):
    assert context.operation_success is False


@then("баланс клиента остается {balance:d} рублей")
def step_balance_is_unchanged(context, balance):
    assert context.account.balance == balance
