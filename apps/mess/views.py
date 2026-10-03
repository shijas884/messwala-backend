from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import MessSerializer
from .models import Mess
from apps.users.permissions import IsOwnerRole

class MessListCreateView(ListCreateAPIView):

    permission_classes = [IsAuthenticated,IsOwnerRole]
    serializer_class = MessSerializer

    def get_queryset(self):
        user = self.request.user
        return Mess.objects.filter(
            owner=user
        )
    


