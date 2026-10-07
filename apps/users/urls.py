from django.urls import path
from rest_framework_simplejwt.views import(
    TokenRefreshView
)

from .views import (
    LoginUserView,
    OwnerListCreateView
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('login/', LoginUserView.as_view()),

    path('owner/', OwnerListCreateView.as_view()),
]