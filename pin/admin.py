from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Pin)
# admin.site.er(CustomUser)
# admin.site.register(User,CustomUser)