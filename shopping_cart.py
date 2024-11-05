from decimal import Decimal
from typing import Dict, Optional
from product import Product

class ShoppingCart:
    def __init__(self):
        self._items: Dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    def remove_product(self, product: Product, quantity: Optional[int] = None) -> None:
        if product not in self._items:
            raise ValueError("Product not in cart")
        if quantity is None or self._items[product] <= quantity:
            del self._items[product]
        else:
            self._items[product] -= quantity

    def get_total(self) -> Decimal:
        total = Decimal('0')
        for product, quantity in self._items.items():
            total += product.get_final_price() * quantity
        return total

    def get_items(self) -> Dict[Product, int]:
        return self._items.copy()
