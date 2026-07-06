from django.urls import path
from .views import book_list, create_book
urlpatterns = [
    path('book-list/',book_list),
    path('create-book/', create_book)
]