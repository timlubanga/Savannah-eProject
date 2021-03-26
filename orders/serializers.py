from orders.models import Customer, Order
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['phone_number']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=['item', "quantity"]
