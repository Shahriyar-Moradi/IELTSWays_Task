from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    # Your admin configuration
    pass
admin.site.register(UserProfile)
# admin.site.register(UserProfile, UserProfileAdmin)