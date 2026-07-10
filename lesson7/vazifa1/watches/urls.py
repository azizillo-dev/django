from django.urls import path
from .views import*


urlpatterns = [
    path('create/', create_watch, name='create_watch'),
    path('', home_page, name='home_page'),
    path('delete/<int:pk>', delete_watch, name="delete"),
]