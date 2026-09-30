from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.users.models import User, DeliveryBoy

class DeliveryBoyCreateSerializer(ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True, required=False)
    contact_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = DeliveryBoy
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'contact_number',
            'address',
        ]
             
    def create(self, validated_data):

        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password', None),
            'first_name': validated_data.pop('first_name'),
            'contact_number': validated_data.pop('contact_number'),
            'role_type': User.Role.DELIVERY_BOY,
            'created_by':self.context['request'].user
        }

        user = User.objects.create_user(**user_data)

        mess = self.context['mess']

        delivery_boy = DeliveryBoy.objects.create(
            user=user,
            mess=mess
        )

        return delivery_boy