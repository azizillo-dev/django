from django.contrib import admin
from .models import Clothes, Category


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'color', 'size', 'category', 'price']
    search_fields = ['brand', 'tile', 'description', 'color', 'name']
    list_filter = ['category']
admin.site.register(Category)


