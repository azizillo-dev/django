from django.contrib import admin
from .models import Student, Teacher
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'phone_number', 'faculty', 'gpa')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'faculty')
    ordering = ('last_name', 'first_name')



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'phone_number', 'department', 'salary')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'department')
    ordering = ('last_name', 'first_name')





    

