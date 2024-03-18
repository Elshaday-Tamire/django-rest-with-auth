from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # You can add more fields as per your requirements

class User(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users')
