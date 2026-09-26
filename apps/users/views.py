from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import LoginUserSerializer


class LoginUserView(APIView):

    def post(self, request):
        log_serializer = LoginUserSerializer(request.data)

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
        





        


