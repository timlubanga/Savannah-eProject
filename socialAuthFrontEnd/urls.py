
from django.urls import path
from socialAuthFrontEnd.views import googleLogin, facebookLogin


googleurlpatterns = [
    path('google', googleLogin),
    path('facebook', facebookLogin)

]
