from unittest.mock import Mock
from coffee.models import Order, PaymentStrategy


def test_payment_strategy_called_with_correct_amount():
    mock_strategy = Mock(spec=PaymentStrategy)

    order = Order()
    order.add_coffee("espresso")
    order.add_coffee("espresso")  # 300 руб
    order.set_payment_strategy(mock_strategy)

    order.process_order()

    mock_strategy.pay.assert_called_once_with(300.0)
