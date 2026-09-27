from django.urls import path

from .views import (
    LoginUserView,
    UserListCreateView
)

urlpatterns = [
    path('login/', LoginUserView.as_view()),

    path('users/', UserListCreateView.as_view())


]