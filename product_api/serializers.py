from rest_framework import serializers
from .models import Product, Order

# TODO improve and refactor into separate modules
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity_in_stock']


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Nested serializer

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'product', 'created_at']