from behave import then


@then('клиент видит сообщение "{message}"')
@then('пользователь видит сообщение "{message}"')
def step_actor_sees_message(context, message):
    assert context.message == message
