from django.db import models

from apps.mess.models import Mess
from apps.customers.models import Customer
from apps.meals.models import Meal
from apps.subscriptions.models import Subscription

# Create your models here.
class Bill(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed" 

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="bills"
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name="bills"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )


class Payment(models.Model):

    bill = models.ForeignKey(
        Bill,
        on_delete=models.PROTECT,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid_at = models.DateTimeField(
        auto_created=True
    )