from rest_framework.permissions import IsAuthenticated

from abstract.viewset import CustomModelViewSet


from apps.cart.models import Cart
from apps.cart import serializers


class CartViewSet(CustomModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartListSerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CartListSerializer
        elif self.action == 'retrieve':
            return serializers.CartDetailSerializer
        elif self.action == 'create':
            return serializers.CartCreateSerializer
        elif self.action == 'update':
            return serializers.CartUpdateSerializer
        return serializers.CartSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(customer=self.request.user)
        elif self.request.user.is_superuser:
            return self.queryset
        else:
            return self.queryset.none()
