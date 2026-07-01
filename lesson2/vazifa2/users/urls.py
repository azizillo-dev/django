from django.urls import path
from .views import *



urlpatterns = [
    path('', footer),
    path('users_name', get_users_name),
    path('all_users', get_users)
]



