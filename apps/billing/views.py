from rest_framework.generics import ListCreateAPIView
# Create your views here.

from .models import Bill,Payment
from .serializers import(
    BillCreateSerializer,
    BillListSerializer,
    PaymentCreateSerializer,
    PaymentListSerializer,
)

class BillListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BillCreateSerializer
        return BillListSerializer
     
    queryset =  Bill.objects.all()   


class PaymentListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentCreateSerializer
        return PaymentListSerializer
     
    queryset =  Payment.objects.all()   
       