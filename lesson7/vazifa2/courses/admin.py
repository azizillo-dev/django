from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'teacher', 'price']
    search_fields = ['title', 'desc', 'teacher', 'price']
    