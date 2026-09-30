from django.urls import path

from .views import DeliveryBoyCreateView,DeliveryBoyListView

urlpatterns = [
    path('messes/<int:mess_id>/delivery-boys/', DeliveryBoyCreateView.as_view()),
    path('messes/delivery-boys/', DeliveryBoyListView.as_view()),
]