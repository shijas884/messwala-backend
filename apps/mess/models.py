from django.db import models
from django.conf import settings

# Create your models here.
class Mess(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    owner = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name='messes'
    )