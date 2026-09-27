from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import (
    LoginUserSerializer,
    UserCreateSerializer,
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


class UserListCreateView(ListCreateAPIView):

    def get_permissions(self):

        if self.request.method == 'POST':
            return [(IsAdminRole | IsAdminRole )()]
        return [(IsAdminRole | IsAdminRole )()]

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()





        


