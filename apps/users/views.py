from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView,Response,status
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import (
    LoginUserSerializer,
    OwnerListCreateSerializer,
)
from .permissions import IsAdminRole, IsOwnerRole


class LoginUserView(APIView):

    def post(self, request):
        log_serializer = LoginUserSerializer(data=request.data)

        if log_serializer.is_valid():
            return Response(
                {
                    'access' : log_serializer.validated_data['access'],
                    'refresh' : log_serializer.validated_data['refresh'],
                    'username' : log_serializer.validated_data['user'].username,
                },
                status=status.HTTP_200_OK
            )
        return Response(
            log_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class OwnerListCreateView(ListCreateAPIView):

    
    serializer_class = OwnerListCreateSerializer

    def get_permissions(self):
       if self.request.method == 'POST':
           return [IsAdminRole()]
       return [(IsAdminRole | IsOwnerRole)()]

    def get_queryset(self):
        user = self.request.user

        if user.role_type == User.Role.ADMIN:
            return User.objects.all()

        if user.role_type == User.Role.OWNER:
            return User.objects.filter(
                created_by = user

            )
        
        return User.objects.none()





        


