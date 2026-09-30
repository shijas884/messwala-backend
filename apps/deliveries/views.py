from rest_framework.generics import CreateAPIView,ListAPIView
from django.shortcuts import get_object_or_404

from .serializers import DeliveryBoyCreateSerializer
from apps.mess.models import Mess
from apps.users.models import DeliveryBoy
from apps.users.permissions import IsOwnerRole


class DeliveryBoyCreateView(CreateAPIView):

    serializer_class = DeliveryBoyCreateSerializer
    permission_classes = [IsOwnerRole]

    def get_serializer_context(self):
        print('views -1')

        context = super().get_serializer_context()

        mess = get_object_or_404(
            Mess,
            id=self.kwargs['mess_id'],
            owner=self.request.user
        )

        context['mess'] = mess
        return context


