from socialAuth.views import GoogleSocialAuthView

from django.urls import path


socialAuthurls = [
    path("googleSignin/", GoogleSocialAuthView.as_view())
]
