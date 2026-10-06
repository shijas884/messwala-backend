from django.db import models

from apps.users.models import User
from apps.mess.models import Mess
from apps.customers.models import Customer
from apps.meals.models import Meal
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

class MealDelivery(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='deliveries'
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.PROTECT
    )

    delivery_boy = models.ForeignKey(
        DeliveryBoy,
        on_delete=models.PROTECT,
        related_name='deliveries'
    )

    delivery_date = models.DateField()