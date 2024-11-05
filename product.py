from decimal import Decimal

class Product:
    def __init__(self, id: int, name: str, price: Decimal, description: str):
        self.id = id
        self._name = name
        self._price = price
        self._description = description
        self._tax_rate = Decimal('0.10')
        self._discount_rate = Decimal('0.00')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, value: Decimal) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value

    def set_discount(self, discount_rate: Decimal) -> None:
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1")
        self._discount_rate = discount_rate

    def get_price_with_tax(self) -> Decimal:
        return self.price * (1 + self._tax_rate)

    def get_final_price(self) -> Decimal:
        price_with_tax = self.get_price_with_tax()
        return price_with_tax * (1 - self._discount_rate)
