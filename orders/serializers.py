from orders.models import Customer, Order
from rest_framework import serializers
from authentication.serializers import UserRegistrationSerializer


class CustomerSerializer(serializers.ModelSerializer):
    account = UserRegistrationSerializer()

    class Meta:
        model = Customer
        fields = ['phone_number', "customer_id", "account"]

    def update(self, instance, validated_data):
        method = self.context.get("method")
        print(validated_data.get("phone_number"))
        if not validated_data.get("phone_number") and not validated_data.get("customer_id") and method == "PATCH":
            raise serializers.ValidationError(
                "please provide data to be updated")
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['item', "quantity", "customer", "id"]
