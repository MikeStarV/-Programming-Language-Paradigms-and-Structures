import pytest
from coffee.models import Order, CreditCardPayment


def test_total_cost_calculation():
    order = Order()
    order.add_coffee("espresso")
    order.add_coffee("cappuccino")

    assert order.get_total_cost() == 350.0


def test_successful_payment():
    order = Order()
    order.add_coffee("espresso")
    order.set_payment_strategy(CreditCardPayment())

    result = order.process_order()
    assert "банковской картой" in result


def test_payment_without_strategy():
    order = Order()
    order.add_coffee("espresso")

    with pytest.raises(RuntimeError):
        order.process_order()
