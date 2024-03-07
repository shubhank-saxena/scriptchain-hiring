from django.urls import path

from .views import UserAuthenticationViewSet, UserLoginViewSet

urlpatterns = [
    path("", UserAuthenticationViewSet.as_view(), name="user-authentication"),
    path("self", UserLoginViewSet.as_view(), name="user-login"),
]
