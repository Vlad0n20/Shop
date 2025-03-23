from rest_framework.permissions import AllowAny, IsAdminUser

from abstract.viewset import CustomModelViewSet

from apps.category.models import Category
from apps.category import serializers


class CategoryViewSet(CustomModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CategoryListSerializer
        elif self.action == 'retrieve':
            return serializers.CategoryDetailSerializer
        elif self.action == 'create':
            return serializers.CategoryCreateSerializer
        elif self.action == 'update':
            return serializers.CategoryUpdateSerializer
        return serializers.CategorySerializer
