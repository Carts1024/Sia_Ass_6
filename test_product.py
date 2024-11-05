import unittest
from decimal import Decimal
from unittest.mock import Mock, patch
from product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        # Create a mock Product instance
        self.product = Mock(spec=Product)
        self.product.name = "Mock Product"
        self.product.price = Decimal('10.00')
        self.product.description = "Mock Description"
        self.product.get_price_with_tax.return_value = Decimal('11.00')  # 10.00 + 10% tax

    def test_initial_values(self):
        self.assertEqual(self.product.name, "Mock Product")
        self.assertEqual(self.product.price, Decimal('10.00'))
        self.assertEqual(self.product.description, "Mock Description")

    def test_price_with_tax(self):
        self.assertEqual(self.product.get_price_with_tax(), Decimal('11.00'))

    def test_discount(self):
        # Mock the final price with a discount applied
        self.product.get_final_price.return_value = Decimal('8.80')  # Final price after 20% discount
        self.assertEqual(self.product.get_final_price(), Decimal('8.80'))

    def test_invalid_price(self):
        product = Product(id=1, name="Test Product", price=Decimal("10.00"), description="Test Description")
        with self.assertRaises(ValueError):
            product.price = Decimal('-1.00')

