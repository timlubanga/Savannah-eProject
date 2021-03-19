from django.urls import path
from authentication.views import UserRegistrationView


authurlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register")]
