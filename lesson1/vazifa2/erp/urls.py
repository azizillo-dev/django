from django.contrib import admin
from django.urls import path
from .students import get_students
from .courses import get_courses
from .products import get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_students),
    path('courses/', get_courses),
    path('products/', get_products),
]
