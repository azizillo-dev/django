from django.contrib import admin
from .models import Book, Category, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pages_count']
    search_fields = ['desc', 'title', 'author__full_name']    
    list_per_page = 10


admin.site.register(Author)
admin.site.register(Category)



