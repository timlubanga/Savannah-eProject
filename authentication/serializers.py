from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

UserAccount = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    tokens = serializers.SerializerMethodField()
    random = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = ["email", "username", "password", "random",
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


class EmailLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):

        login_username = validated_data.get('username', None)
        print(login_username)
        login_password = validated_data.get("password", None)
        user = authenticate(**validated_data)

        if not user:
            raise serializers.ValidationError(
                "Please provide correct username or password")
        tokens = user.tokens()
        return {"tokens": tokens}

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
