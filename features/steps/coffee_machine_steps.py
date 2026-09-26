from behave import given, then, when

from app.coffee_machine import CoffeeMachine


@given("для капучино требуется {required_ml:d} мл молока")
def step_cappuccino_requires_milk(context, required_ml):
    assert CoffeeMachine.CAPPUCCINO_MILK_ML == required_ml


@given("в кофемашине есть {milk_ml:d} мл молока")
def step_machine_has_milk(context, milk_ml):
    context.machine = CoffeeMachine(milk_ml)


@when("пользователь выбирает капучино")
def step_user_selects_cappuccino(context):
    context.drink_prepared = context.machine.make_cappuccino()
    context.message = context.machine.message


@then("кофемашина не готовит напиток")
def step_machine_rejects_drink(context):
    assert context.drink_prepared is False


@then("молока в кофемашине остается {milk_ml:d} мл")
def step_milk_is_unchanged(context, milk_ml):
    assert context.machine.milk_ml == milk_ml
