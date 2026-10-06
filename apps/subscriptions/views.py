from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.customers.models import Customer
from apps.users.permissions import IsOwnerRole
from .models import Subscription,SubscriptionMeal
from .serializers import(
    SubscriptionSerializer,
    SubscriptionMealCreateSerializer,
    SubscriptionMealListSerializer
)

class SubscriptionListCreateView(ListCreateAPIView):

    serializer_class= SubscriptionSerializer
    permission_classes = [IsAuthenticated,IsOwnerRole]

    def get_serializer_context(self):
         
        context = super().get_serializer_context()

        customer = get_object_or_404(
            Customer,
            id=self.kwargs['customer_id'],
            mess__owner = self.request.user
        )

        context['customer']=customer
        return context

    def get_queryset(self):
        return Subscription.objects.filter(
            customer__mess__owner=self.request.user
        )
    



class SubscriptionMealListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SubscriptionMealCreateSerializer
        return SubscriptionMealListSerializer
     
    queryset =  SubscriptionMeal.objects.all()   
          