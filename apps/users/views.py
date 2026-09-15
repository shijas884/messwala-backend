from rest_framework.generics import ListCreateAPIView

from .models import User
from .serializers import UserCreateSerializer,UserListSerializer


class UserListCreateView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserListSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.role_type == User.Role.ADMIN:
            return User.objects.all()

        return User.objects.none




        


