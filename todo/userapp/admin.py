from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from userapp.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = list(BaseUserAdmin.fieldsets) + [(None, {"fields": ("age", )})]
