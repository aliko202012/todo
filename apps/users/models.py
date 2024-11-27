from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def _str_(self):
        return self.username