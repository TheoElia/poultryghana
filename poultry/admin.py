from django.contrib import admin
from django.contrib.admin import register

from accounts.models import User
from .models import *

# Register your models here.
def is_member(user_id,group_name):
    user = User.objects.get(pk=user_id)
    return user.groups.filter(name=group_name).exists()


@register(Farm)
class FarmAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Farm.objects.all()
        if request.user.is_staff and is_member(request.user.id,"Farmers"):
            return Farm.objects.filter(owner=request.user)
        return None



@register(PoultryRecord)
class PoultryRecordAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        if request.user.is_superuser:
            return PoultryRecord.objects.all()
        if request.user.is_staff and is_member(request.user.id,"Farmers"):
            shop = Farm.objects.get(owner=request.user)
            return PoultryRecord.objects.filter(farm=shop)
        return None