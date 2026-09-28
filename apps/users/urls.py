from django.urls import path
from rest_framework_simplejwt.views import(
    TokenRefreshView
)

from .views import (
    LoginUserView,
    UserListCreateView
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('login/', LoginUserView.as_view()),

    path('users/', UserListCreateView.as_view()),
]