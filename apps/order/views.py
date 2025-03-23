from rest_framework.permissions import IsAuthenticated

from abstract.viewset import CustomModelViewSet


from apps.order.models import Order, OrderItem
from apps.order import serializers


class OrderViewSet(CustomModelViewSet):
    queryset = Order.objects.all()
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.OrderCreateSerializer
        elif self.action == 'update':
            return serializers.OrderUpdateSerializer
        return serializers.OrderListSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(customer=self.request.user)
        elif self.request.user.is_superuser:
            return self.queryset
        else:
            return self.queryset.none()
    


class OrderItemViewSet(CustomModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }
    
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.OrderItemCreateSerializer
        elif self.action == 'update':
            return serializers.OrderItemUpdateSerializer
        return serializers.OrderItemSerializer
    
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(order__customer=self.request.user)
        elif self.request.user.is_superuser:
            return self.queryset
        else:
            return self.queryset.none()
    

