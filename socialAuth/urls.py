from socialAuth.views import GoogleSocialAuthView, FacebookSocialAuthView

from django.urls import path


socialAuthurls = [
    path("google/", GoogleSocialAuthView.as_view()),
    path("facebook/", FacebookSocialAuthView().as_view())

]
