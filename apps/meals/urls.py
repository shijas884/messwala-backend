from django.urls import path

from .views import MealListCreateView


urlpatterns = [
    path('messes/meals/', MealListCreateView.as_view())
]