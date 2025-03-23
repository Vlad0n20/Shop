from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.cart.models import Cart
from apps.order.models import OrderItem
from apps.product.models import Product

User = get_user_model()

class CartViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.client.force_authenticate(user=self.user)

    def test_list_carts(self):
        url = reverse('cart-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_cart(self):
        url = reverse('cart-detail', kwargs={'pk': self.cart.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.cart.id)

    def test_create_cart(self):
        url = reverse('cart-list')
        data = {
            'customer': self.user.id,
            'products': [self.order_item.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 2)

    def test_update_cart(self):
        url = reverse('cart-detail', kwargs={'pk': self.cart.pk})
        new_order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,
            price=20.00
        )
        data = {
            'products': [new_order_item.id]
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cart.refresh_from_db()
        self.assertEqual(self.cart.products.first(), new_order_item)

    def test_delete_cart(self):
        url = reverse('cart-detail', kwargs={'pk': self.cart.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cart.objects.count(), 0)

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        url = reverse('cart-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_other_user_cart_access(self):
        other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )
        other_cart = Cart.objects.create(customer=other_user)
        url = reverse('cart-detail', kwargs={'pk': other_cart.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 