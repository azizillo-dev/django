from django.contrib import admin
from .models import Computer
# Register your models here.

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name', 'price', 'screen_info', 'created_at', 'gpu']
    list_filter = ['brand', 'price', 'gpu']
    search_fields = ['brand', 'name']
    


