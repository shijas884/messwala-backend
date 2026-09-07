from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        VENDOR = "OWNER", "Owner"

    email = models.EmailField(unique=True)
    role_type = models.CharField(
        max_length=15, choices=Role.choices, default=Role.VENDOR
    )
    
