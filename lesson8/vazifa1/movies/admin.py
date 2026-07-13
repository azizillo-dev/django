from django.contrib import admin
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id' ,"title", "year", 'producer', 'category', 'genre']
    search_fields = ['description', 'title', 'genre', 'producer', 'category']
    list_filter = ['producer', 'category']

admin.site.register(Producer)
admin.site.register(Category)



