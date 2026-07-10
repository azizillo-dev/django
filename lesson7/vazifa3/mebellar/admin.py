from django.contrib import admin
from .models import Mebel


@admin.register(Mebel)
class MebelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'count', 'is_have', 'created_at')
    list_filter = ('category', 'is_have', 'material')
    search_fields = ('name', 'material', 'color')
    ordering = ('-created_at',)
    list_per_page = 10

