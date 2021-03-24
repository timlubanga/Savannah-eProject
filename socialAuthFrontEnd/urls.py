
from django.urls import path
from socialAuthFrontEnd.views import googleLogin


googleurlpatterns = [
    path('', googleLogin)
]
