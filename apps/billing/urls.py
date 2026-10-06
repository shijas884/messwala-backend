from django.urls import path

from .views import (
    BillListCreateView,
    PaymentListCreateView
)


urlpatterns = [
    path('messes/bill/', BillListCreateView.as_view()),
    path('messes/payment/', PaymentListCreateView.as_view()),
]