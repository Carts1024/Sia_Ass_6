import unittest
from decimal import Decimal
from unittest.mock import Mock
from shopping_cart import ShoppingCart
from product import Product

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Initialize shopping cart
        self.cart = ShoppingCart()

        # Create mock Product instance
        self.product = Mock(spec=Product)
        self.product.get_final_price.return_value = Decimal('8.80')  # Price with discount applied

    def test_add_and_calculate(self):
        self.cart.add_product(self.product, 2)  # 2 * 8.80 = 17.60
        expected = Decimal('17.60')
        self.assertEqual(self.cart.get_total(), expected)

    def test_remove_product_integration(self):
        self.cart.add_product(self.product, 2)
        self.cart.remove_product(self.product, 1)
        self.assertEqual(self.cart.get_items()[self.product], 1)
        self.cart.remove_product(self.product)
        self.assertNotIn(self.product, self.cart.get_items())
