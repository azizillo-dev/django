from django.contrib import admin
from .models import Flower
# Register your models here.

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "color", "is_tikonli"]
    search_fields = ["name", "color", "desc"]
    ordering = ["-id"]

