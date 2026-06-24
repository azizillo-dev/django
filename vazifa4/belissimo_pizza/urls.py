from django.contrib import admin
from django.urls import path
from .menu import get_pizzas, get_burgers, get_lavash, get_ichimlik

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', get_pizzas),
    path('burgers/', get_burgers),
    path('lavash/', get_lavash),
    path('ichimlik/', get_ichimlik),
]
