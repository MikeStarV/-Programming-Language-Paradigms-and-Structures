from coffee.models import Order, CreditCardPayment

def main():
    order = Order()
    order.add_coffee("espresso")
    order.add_coffee("cappuccino")

    order.set_payment_strategy(CreditCardPayment())

    result = order.process_order()
    print(result)


if __name__ == "__main__":
    main()
