from django.urls import path

from .views import SubscriptionListCreateView,SubscriptionMealListCreateView


urlpatterns = [
    path('messes/<int:customer_id>/subscriptions/', SubscriptionListCreateView.as_view()),
    path('messes/meals/subscriptions/', SubscriptionMealListCreateView.as_view()),


]