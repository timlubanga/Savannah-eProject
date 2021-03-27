from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from orders.customer import createCustomer

UserAccount = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = UserAccount
        fields = ["email", "username", "password",
                  "confirm_password", "tokens"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if not attrs["password"] or not ["username"]:
            raise serializers.ValidationError(
                "password or username cannot be null")

        if attrs["confirm_password"] != attrs["password"]:
            raise serializers.ValidationError(
                "please ensure the passwords match")
        return attrs

    def create(self, validated_data):
        data = validated_data.pop("confirm_password")
        user = UserAccount.objects.create_user(**validated_data)
        createCustomer(user=user)
        return user

    def get_tokens(self, obj):
        tokens = obj.tokens()
        return tokens


class EmailLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["username", "password"]
        extra_kwargs = {'password': {'style': {'input_type': 'password'}}}

    def save(self):
        login_username = self.validated_data.get('username', None)
        print(login_username)
        login_password = self.validated_data.get("password", None)
        user = authenticate(username=login_username, password=login_password)

        if not user:
            raise serializers.ValidationError(
                "Please provide correct username or password")
        tokens = user.tokens()
        return {"tokens": tokens,
                "email": user.email,


                }

    def validate(self, attrs):
        return attrs

    # def get_tokens(self, obj):
    #     print(self.validated_data)
    #     # login_username = self.validated_data["username"]
    #     # login_password = self.validate_data["password"]
    #     # print(login_password, login_username)
    #     # user = authenticate(username=login_username, password=login_password)

    #     # if not user:
    #     #     raise serializers.ValidationError(
    #     #         "Please provide correct username or password")
    #     # tokens = user.tokens()
    #     # return tokens
