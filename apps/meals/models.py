from django.db import models

from apps.mess.models import Mess

# Create your models here.

class Meal(models.Model):

    class MealType(models.TextChoices):
        LUNCH = "LUNCH", "Lunch"
        DINNER = "DINNER", "Dinner"

    mess = models.ForeignKey(
        Mess,
        on_delete=models.PROTECT,
        related_name="meals"
    )

    meal_type = models.CharField(
        max_length=10,
        choices=MealType.choices
    )

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )