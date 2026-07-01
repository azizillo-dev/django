from django.contrib import admin
from django.urls import path
from .funcs import home, contact, courses, students, teachers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('contact', contact),
    path('courses/', courses),
    path('students', students),
    path('teachers', teachers)
]
