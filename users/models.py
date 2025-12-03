from django.contrib.auth.models import AbstractUser
from django.db import models
from tenants.models import Vendor

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Store Owner'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.CASCADE)

    def is_owner(self):
        return self.role == 'owner'
