from django.db import models

from apps.users.models import User
from apps.mess.models import Mess
# Create your models here.

class DeliveryBoy(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='delivery_boy'
    )

    mess = models.ForeignKey(
        Mess,
        on_delete=models.PROTECT,
        related_name='delivery_boys'
    )