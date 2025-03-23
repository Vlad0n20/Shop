from abstract.viewset import CustomModelViewSet

from apps.product.models import Product
from apps.product.serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, ProductUpdateSerializer


class ProductViewSet(CustomModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        elif self.action == 'update':
            return ProductUpdateSerializer
        return ProductListSerializer