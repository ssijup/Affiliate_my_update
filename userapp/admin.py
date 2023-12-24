from django.contrib import admin

from .models import UserData,UserDetails

admin.site.register(UserData),
admin.site.register(UserDetails)
