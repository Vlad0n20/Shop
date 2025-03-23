from rest_framework import serializers

from apps.image.models import Image


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_url', 'alt_text', 'image_type', 'image_size', 'created_on', 'updated_on')


class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_url', 'alt_text', 'image_type', 'image_size', 'created_on', 'updated_on')
        


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_url', 'alt_text', 'image_type', 'image_size', 'created_on', 'updated_on')


class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_url', 'alt_text', 'image_type', 'image_size', 'created_on', 'updated_on')



