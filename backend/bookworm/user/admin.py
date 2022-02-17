from django.contrib import admin

# Register your models here.
from bookworm.user.data.models import AppUser

admin.site.register(AppUser)
