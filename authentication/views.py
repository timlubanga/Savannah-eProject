from django.shortcuts import render
from authentication.serializers import UserRegistrationSerializer, EmailLoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class EmailLoginView(generics.GenericAPIView):
    serializer_class = EmailLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(user, status.HTTP_200_OK)
