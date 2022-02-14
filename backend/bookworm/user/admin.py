from django.contrib import admin

# Register your models here.
from bookworm.user.models import AppUser

admin.register(AppUser)
