from django.contrib import admin
from .models import *



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'pages_count']
    search_fields = ['desc', 'title', 'author__full_name', 'genre__name']    
    list_per_page = 10

admin.site.register(Author)
admin.site.register(Genre)









