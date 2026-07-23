from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_display = ['first_name', 'username', 'email']
    list_filter = ['is_staff']



