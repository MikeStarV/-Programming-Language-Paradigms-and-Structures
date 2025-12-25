from abc import ABC, abstractmethod




class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Coffee):
    def get_description(self) -> str:
        return "Эспрессо"

    def cost(self) -> float:
        return 150.0


class Cappuccino(Coffee):
    def get_description(self) -> str:
        return "Капучино"

    def cost(self) -> float:
        return 200.0


class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type: str) -> Coffee:
        if coffee_type == "espresso":
            return Espresso()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Unknown coffee type")


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Оплачено {amount} руб. банковской картой."


class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Оплачено {amount} руб. наличными."




class Order:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_coffee(self, coffee_type: str):
        coffee = CoffeeFactory.create_coffee(coffee_type)
        self.items.append(coffee)

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def get_total_cost(self) -> float:
        return sum(item.cost() for item in self.items)

    def process_order(self) -> str:
        if not self.payment_strategy:
            raise RuntimeError("Payment method not selected")

        total = self.get_total_cost()
        return self.payment_strategy.pay(total)
