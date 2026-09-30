from django.urls import path

from .views import CustomerCreateView,CustomerListView

urlpatterns = [
    path('messes/<int:mess_id>/customers/', CustomerCreateView.as_view()),
    path('messes/customers/', CustomerListView.as_view())
]