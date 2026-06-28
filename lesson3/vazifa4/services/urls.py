from django.urls import path
from .views import home, list_items

urlpatterns = [
    path('', home, name='home'),
    path('list/', list_items, name='list_items'),
]
