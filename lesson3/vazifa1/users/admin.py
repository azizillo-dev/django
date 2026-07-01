from django.contrib import admin
from .models import User, Librarian
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'birth_date', 'address')
    search_fields = ('full_name', 'email', 'phone', 'course')
    list_filter = ('course',)
    ordering = ('-id',)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'salary', 'experience', 'is_active', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('is_active',)
    ordering = ('-salary',)



