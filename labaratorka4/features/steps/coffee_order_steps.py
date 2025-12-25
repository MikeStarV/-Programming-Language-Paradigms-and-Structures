from behave import given, when, then
from coffee.models import Order, CreditCardPayment, CashPayment

@given("я создаю новый заказ")
def step_create_order(context):
    context.order = Order()

@given('я добавляю "{coffee_type}" в заказ')
def step_add_coffee(context, coffee_type):
    context.order.add_coffee(coffee_type)

@when("я выбираю оплату картой")
def step_choose_card_payment(context):
    context.order.set_payment_strategy(CreditCardPayment())

@when("я выбираю оплату наличными")
def step_choose_cash_payment(context):
    context.order.set_payment_strategy(CashPayment())

@when("я обрабатываю заказ")
def step_process_order(context):
    try:
        context.result = context.order.process_order()
        context.error_raised = False
    except RuntimeError:
        context.error_raised = True

@then('результат оплаты должен содержать "{text}"')
def step_check_result(context, text):
    assert not context.error_raised, "Ошибка при обработке заказа"
    assert text in context.result

@then("общая стоимость должна быть {amount:d}")
def step_check_total(context, amount):
    assert context.order.get_total_cost() == amount

@then("должна быть вызвана ошибка")
def step_error_raised(context):
    assert context.error_raised, "Ошибка не была вызвана"
