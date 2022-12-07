from django.conf import settings
from django.db import models

from accounts.models import TimeStamp

# Create your models here.
class Farm(TimeStamp):
    name = models.CharField(max_length=250,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    address = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=14,null=True)
    cover_image = models.FileField(null=True,upload_to="farms")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.name}"


class PoultryRecord(TimeStamp):
    pen_no = models.CharField(max_length=255,null=True)
    weight_at_layer = models.FloatField(null=True)
    date_received = models.DateField(null=True)
    date = models.DateField(null=True)
    age = models.FloatField(null=True)
    month = models.CharField(max_length=255,null=True)
    breed = models.CharField(max_length=255,null=True)
    production_type = models.CharField(max_length=255,null=True)
    no_of_animals = models.IntegerField(null=True)
    water = models.FloatField(null=True)
    mortality = models.FloatField(null=True)
    egg_production_morning = models.IntegerField(null=True)
    egg_production_afternoon = models.IntegerField(null=True)
    egg_production_evening = models.IntegerField(null=True)
    medication = models.CharField(max_length=255,null=True)
    remarks = models.TextField(null=True)
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE,null=True,related_name="records")


    def __str__(self):
        return f"{self.pen_no}"