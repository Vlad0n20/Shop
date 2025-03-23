from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.cart.views import CartViewSet
from apps.category.views import CategoryViewSet
from apps.order.views import OrderViewSet
from apps.product.views import ProductViewSet
from apps.user.views import UserViewSet
from apps.image.views import ImageViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet, basename='category')
router.register('carts', CartViewSet, basename='cart')
router.register('orders', OrderViewSet, basename='order')
router.register('images', ImageViewSet, basename='image')

api_urlpatterns = [
    path('api/', include(router.urls)),
]
