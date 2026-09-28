from django.db import models

from apps.users.models import User
# Create your models here.
class Mess(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)