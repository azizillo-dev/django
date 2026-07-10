from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('list/', list_, name="list"),
    path('detail/<int:pk>', detail, name="detail"),
    path('delete/<int:pk>', delete, name="delete"),
    path('create/', create, name="create"),
    path('update/<int:pk>', update, name="update"),
]







