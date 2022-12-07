from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

        
class User(AbstractUser):
    full_name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=14,null=True)
    user_type = models.CharField(max_length=25,null=True)
    is_poultry_owner = models.BooleanField(null=True)
    is_vet_officer = models.BooleanField(null=True)


    def __str__(self) -> str:
        return f"{self.username}"


