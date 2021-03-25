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
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class EmailLoginView(generics.GenericAPIView):
    serializer_class = EmailLoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status.HTTP_200_OK)
