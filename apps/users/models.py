from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        OWNER = 'OWNER', 'Owner'
        CUSTOMER = 'CUSTOMER', 'Customer'
        DELIVERY_BOY = 'DELIVERY_BOY', 'Delivery Boy'


    role_type = models.CharField(max_length=15, choices=Role.choices)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)