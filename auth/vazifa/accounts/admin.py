from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'address', 'year', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Qoshimcha malumot', {'fields': ('address', 'year')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)