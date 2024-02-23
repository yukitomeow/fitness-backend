from django.contrib import admin
from .models import Profile



class ProfileAdminSettings(admin.ModelAdmin):
    list_display = ('pk', 'email', 'user', 'uuid')
 
admin.site.register(Profile, ProfileAdminSettings)

