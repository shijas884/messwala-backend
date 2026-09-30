from django.urls import path

from .views import DeliveryBoyCreateView

urlpatterns = [
    path('messes/<int:mess_id>/delivery-boys/', DeliveryBoyCreateView.as_view()),
]