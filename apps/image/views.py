from rest_framework.permissions import IsAdminUser

from abstract.viewset import CustomModelViewSet

from apps.image.models import Image
from apps.image import serializers


class ImageViewSet(CustomModelViewSet):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageListSerializer
    permission_classes = [IsAdminUser]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ImageListSerializer
        elif self.action == 'retrieve':
            return serializers.ImageDetailSerializer
        elif self.action == 'create':
            return serializers.ImageCreateSerializer
        elif self.action == 'update':
            return serializers.ImageUpdateSerializer
        return serializers.ImageSerializer
