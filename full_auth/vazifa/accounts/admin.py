from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ['username', 'address', 'phone', 'first_name', 'last_name']
    list_display = ['username', 'first_name', 'is_staff', 'email']
    list_per_page = 10
    list_filter = ['address', 'is_staff']
    