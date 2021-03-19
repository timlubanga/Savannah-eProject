from rest_framework import serializers
from django.contrib.auth import get_user_model

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
        return UserAccount.objects.create_user(**validated_data)

    def get_tokens(self, obj):
        tokens = obj.tokens()
        return tokens
