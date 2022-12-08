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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return f"{self.name}"


class VetShop(TimeStamp):
    name = models.CharField(max_length=250,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    address = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=14,null=True)
    cover_image = models.FileField(null=True,upload_to="shops")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.name}"


class Record(TimeStamp):
    pen_no = models.CharField(max_length=255,null=True)
    weight_at_layer = models.FloatField(null=True)
    date_received = models.DateField(null=True)
    month = models.CharField(max_length=255,null=True)
    breed = models.CharField(max_length=255,null=True)
    production_type = models.CharField(max_length=255,null=True)
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE,null=True,related_name="records")
    no_of_birds = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.farm.name} - {self.pen_no}"


class PoultryRecord(TimeStamp):
    record = models.ForeignKey(Record,null=True,on_delete=models.PROTECT,related_name="weekly_records",blank=True)
    culls_plus = models.FloatField(null=True,blank=True)
    culls_minus = models.FloatField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    age = models.FloatField(null=True,help_text="in weeks",blank=True)
    water = models.FloatField(null=True)
    mortality = models.FloatField(null=True)
    egg_production_morning = models.IntegerField(null=True)
    egg_production_afternoon = models.IntegerField(null=True)
    egg_production_evening = models.IntegerField(null=True)
    medication = models.CharField(max_length=255,null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE,null=True,related_name="record_records",blank=True)


    def __str__(self):
        return f"{self.farm.name} - {self.record.pen_no}"


class Product(TimeStamp):
    name = models.CharField(max_length=255,null=True)
    price = models.FloatField(null=True)
    description = models.TextField(null=True,blank=True)
    cover_image = models.FileField(null=True,upload_to="products")
    shop = models.ForeignKey(VetShop,null=True,on_delete=models.CASCADE,related_name="products",blank=True)
    farm = models.ForeignKey(Farm,null=True,on_delete=models.CASCADE,related_name="products",blank=True)

    def __str__(self):
        return f"{self.shop.name} - {self.name}"