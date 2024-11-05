import unittest
from decimal import Decimal
from unittest.mock import Mock
from shopping_cart import ShoppingCart
from product import Product

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # Initialize the shopping cart
        self.cart = ShoppingCart()

        # Create mock Product instances
        self.product1 = Mock(spec=Product)
        self.product1.get_final_price.return_value = Decimal('11.00')  # Product 1 with tax
        self.product2 = Mock(spec=Product)
        self.product2.get_final_price.return_value = Decimal('22.00')  # Product 2 with tax

    def test_add_product(self):
        self.cart.add_product(self.product1, 2)
        items = self.cart.get_items()
        self.assertEqual(items[self.product1], 2)

    def test_remove_product(self):
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product(self.product1, 1)
        items = self.cart.get_items()
        self.assertEqual(items[self.product1], 1)

    def test_cart_total(self):
        self.cart.add_product(self.product1, 2)  # 2 * 11.00 = 22.00
        self.cart.add_product(self.product2, 1)  # 1 * 22.00 = 22.00
        expected = Decimal('44.00')
        self.assertEqual(self.cart.get_total(), expected)
