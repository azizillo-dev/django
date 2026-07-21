from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create/', BookCreate.as_view(), name='create'),
    path('book-list/', BookListView.as_view(), name='list')
]