from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class LoginUserSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not password or not username:
            raise serializers.ValidationError(
                'Both username and password are required'
            )

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                'Invalid username or password '
            )

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        attrs['user'] = user

        return attrs


class OwnerListCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'role_type',
            'created_by',
            'contact_number',
            'address'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required' : False},
            'id' : {'read_only': True}
        }

    def validate_role_type(self, value):
        user = self.context['request'].user

        if user.role_type == User.Role.ADMIN:
            if value != User.Role.OWNER:
                raise serializers.ValidationError(
                    'Admin can only create Owner'
                )

        return value

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return User.objects.create_user(**validated_data)
    
        

        