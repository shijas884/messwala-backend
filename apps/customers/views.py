from rest_framework.generics import CreateAPIView
from  django.shortcuts import get_object_or_404

from .serializers import CustomerCreateSerializer
from apps.users.permissions import IsOwnerRole
from apps.mess.models import Mess
class CustomerCreateView(CreateAPIView):
    permission_classes = [IsOwnerRole]
    serializer_class = CustomerCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        mess = get_object_or_404(
            Mess,
            id=self.kwargs['mess_id'],
            owner=self.request.user
        )

        context['mess'] = mess

        return context
    
