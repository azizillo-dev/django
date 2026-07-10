from django.contrib import admin
from .models import Watch
# Register your models here.


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'mexanism', 'color', 'remenka', 'shape')
    search_fields = ('name', 'model', 'mexanism', 'color', 'remenka', 'shape')
    list_filter = ('mexanism', 'color', 'remenka', 'shape')


    




