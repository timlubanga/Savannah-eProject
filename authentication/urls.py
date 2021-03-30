from django.urls import path
from authentication.views import UserRegistrationView, EmailLoginView



authurlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="emailregister"),
    path('login/', EmailLoginView.as_view(), name="emaillogin")]
