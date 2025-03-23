from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.cart.models import Cart
from apps.cart.serializers import CartSerializer, CartListSerializer, CartDetailSerializer, CartCreateSerializer, CartUpdateSerializer
from apps.order.models import OrderItem
from apps.product.models import Product

User = get_user_model()

class CartSerializerTest(TestCase):
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

    def test_cart_list_serializer(self):
        serializer = CartListSerializer(self.cart)
        self.assertIn('id', serializer.data)
        self.assertIn('customer', serializer.data)
        self.assertIn('products', serializer.data)
        self.assertEqual(len(serializer.data['products']), 1)

    def test_cart_detail_serializer(self):
        serializer = CartDetailSerializer(self.cart)
        self.assertIn('id', serializer.data)
        self.assertIn('customer', serializer.data)
        self.assertIn('products', serializer.data)
        self.assertIn('created_on', serializer.data)
        self.assertIn('updated_on', serializer.data)

    def test_cart_create_serializer(self):
        data = {
            'customer': self.user.id,
            'products': [self.order_item.id]
        }
        serializer = CartCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_cart_update_serializer(self):
        new_order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,
            price=20.00
        )
        data = {
            'customer': self.user.id,
            'products': [new_order_item.id]
        }
        serializer = CartUpdateSerializer(self.cart, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_cart = serializer.save()
        self.assertEqual(updated_cart.products.first(), new_order_item) 