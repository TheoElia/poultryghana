from django.contrib import admin
from django.contrib.admin import register
from .models import *

@register(User)
class UserAdmin(admin.ModelAdmin):
    pass