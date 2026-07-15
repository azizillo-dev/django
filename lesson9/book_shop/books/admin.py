from django.contrib import admin
from .models import *



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price']
    search_fields = ['title', 'author', 'category', 'price']
    list_filter = ['category', 'author']
    list_per_page = 10

admin.site.register(Author)
admin.site.register(Category)
