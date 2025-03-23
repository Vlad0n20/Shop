from rest_framework import serializers

from apps.cart.models import Cart


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'products', 'created_on', 'updated_on')


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'products', 'created_on', 'updated_on')
        


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'products', 'created_on', 'updated_on')


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'products', 'created_on', 'updated_on')



