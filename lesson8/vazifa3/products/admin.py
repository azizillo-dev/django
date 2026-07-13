from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description']
    search_fields = ['name', 'description', 'category']
    list_filter = ['category']
    list_per_page = 10

admin.site.register(Category)