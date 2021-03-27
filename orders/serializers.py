from orders.models import Customer, Order
from rest_framework import serializers
from authentication.serializers import UserRegistrationSerializer


class CustomerSerializer(serializers.ModelSerializer):
    account = UserRegistrationSerializer()

    class Meta:
        model = Customer
        fields = ['phone_number', "customer_id", "account"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['item', "quantity"]
