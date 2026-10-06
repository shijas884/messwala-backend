from rest_framework.serializers import ModelSerializer

from .models import Bill,Payment

class BillCreateSerializer(ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'

class BillListSerializer(ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'


class PaymentCreateSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class PaymentListSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'