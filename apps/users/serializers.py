from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import User


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validated_role_type(self, value):
        user = self.context['request'].user

        # ADMIN
        if user.role_type == User.Role.ADMIN:
            if value != User.Role.OWNER:
                raise  serializers.ValidationError('Admin can only create Owner')

        return value

class UserListSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = '__all__' 
