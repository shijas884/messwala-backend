from django.urls import path

from .views import CustomerCreateView

urlpatterns = [
    path('messes/<int:mess_id>/customers/', CustomerCreateView.as_view())
]