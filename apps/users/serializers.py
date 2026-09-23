from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import User


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password',
            'role_type'
        ]
        extra_kwargs = {'password': {'write_ony: True'}}

    def validated_role_type(self, value):
        user = self.context['request'].user

        # ADMIN
        if user.role_type == User.Role.ADMIN:
            if value != User.Role.OWNER:
                raise  serializers.ValidationError('Admin can only create Owner')
        # OWNER
        if user.role_type == User.Role.OWNER:
            if value == User.Role.ADMIN:
                raise serializers.ValidationError('Owner can create only Customer, Delivery-Boy ')

        return value

class UserListSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'email',
            'role_type',
        ]
