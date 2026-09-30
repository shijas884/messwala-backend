from django.db import models

from apps.mess.models import Mess
from apps.users.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mess = models.ForeignKey(Mess, on_delete=models.PROTECT)
    
    