from django.contrib import admin

from .models import Category, Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'brand', 'color', 'is_available')
    list_filter = ('brand', 'color', 'is_available')
    search_fields = ('name', 'brand', 'color')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'code')