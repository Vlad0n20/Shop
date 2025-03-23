from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.cart.models import Cart
from apps.order.models import OrderItem
from apps.product.models import Product

User = get_user_model()

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='Test Description'
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            quantity=1,
            price=10.00
        )
        self.cart = Cart.objects.create(
            customer=self.user
        )
        self.cart.products.add(self.order_item)

    def test_cart_creation(self):
        self.assertEqual(self.cart.customer, self.user)
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.products.first(), self.order_item)

    def test_cart_str_method(self):
        expected_str = f"Cart - {self.user.username}"
        self.assertEqual(str(self.cart), expected_str)

    def test_cart_ordering(self):
        cart2 = Cart.objects.create(customer=self.user)
        carts = Cart.objects.all()
        self.assertEqual(carts[0], cart2)  # Newest first due to -created_on ordering 