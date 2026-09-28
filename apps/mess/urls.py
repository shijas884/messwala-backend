from django.urls import path

from .views import MessListCreateView

urlpatterns = [
    path('mess/', MessListCreateView.as_view())
]