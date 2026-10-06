from django.db import models

from apps.customers.models import Customer
from apps.meals.models import Meal

# Create your models here.

class Subscription(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='subscriptions'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    subscription_month = models.DateField(null=True,blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['customer', 'subscription_month'],
                name='unique_customer_subscription_month'
            )
        ]

class SubscriptionMeal(models.Model):

    subscription = models.ForeignKey(
        Subscription, 
        on_delete=models.CASCADE
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.PROTECT,
    )

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )