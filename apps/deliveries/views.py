from rest_framework.generics import CreateAPIView,ListAPIView
from django.shortcuts import get_object_or_404

from .serializers import DeliveryBoyCreateSerializer,DeliveryBoyListSerializer
from apps.mess.models import Mess
from .models import DeliveryBoy
from apps.users.permissions import IsOwnerRole


class DeliveryBoyCreateView(CreateAPIView):

    serializer_class = DeliveryBoyCreateSerializer
    permission_classes = [IsOwnerRole]

    def get_serializer_context(self):

        context = super().get_serializer_context()

        mess = get_object_or_404(
            Mess,
            id=self.kwargs['mess_id'],
            owner=self.request.user
        )

        context['mess'] = mess
        return context


class DeliveryBoyListView(ListAPIView):
    serializer_class = DeliveryBoyListSerializer
    permission_classes = [IsOwnerRole]

    def get_queryset(self):
        user = self.request.user
        return DeliveryBoy.objects.filter(
            mess__owner = user
        )