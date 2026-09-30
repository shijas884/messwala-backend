from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Customer
from apps.users.models import User

class CustomerCreateSerializer(ModelSerializer):
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True, required=False)
    contact_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Customer
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'contact_number',
            'address',
        ]

    def create(self, validated_data):

        user_data = {
            
            'username': validated_data.pop('username'),
            'first_name': validated_data.pop('first_name'),
            'last_name' : validated_data.pop('last_name'),
            'contact_number' : validated_data.pop('contact_number'),
            'address' : validated_data.pop('address'),
            'role_type' : User.Role.CUSTOMER,
            'created_by' : self.context['request'].user,
        }

        user = User.objects.create_user(**user_data)

        mess = self.context['mess']

        custmoer = Customer.objects.create(
            user=user,
            mess=mess
        )

        return custmoer
    