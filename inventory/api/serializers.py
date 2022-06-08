from unicodedata import category
from rest_framework import serializers
from inventory.models import Product, Category, Order, Cart
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'description',
            'price',
            'unit',
            'quantity',
            'barcode',
            'self_price',
            'is_expired',
            'expiration_date',
            'is_available',
            'is_visible',
            'image',
            'get_thumbnail',
            'get_expiration_date'
        )


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = (
            'id',
            'date',
            'user',
            'is_refunded',
            'date_of_refund',
            'is_sold',
        )


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'product',
            'quantity',
            'order_price',
            'cart',
            'quantity_left'
        )


