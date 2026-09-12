from rest_framework.generics import ListCreateAPIView

from .models import User
from .serializers import UserCreateSerializer,UserListSerializer


class UserListCreateView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserListSerializer
    
    queryset = User.objects.all()


