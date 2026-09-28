from rest_framework.generics import ListCreateAPIView

from .serializers import MessSerializer
from .models import Mess
from apps.users.permissions import IsOwnerRole

class MessListCreateView(ListCreateAPIView):

    queryset = Mess.objects.all()
    permission_classes = [IsOwnerRole]
    serializer_class = MessSerializer
    


