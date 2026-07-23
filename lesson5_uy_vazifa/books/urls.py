from django.urls import path
from .views import book_list, create_book, detail_book, index_
urlpatterns = [
    path('book-list/',book_list, name = "list"),
    path('create-book/', create_book),
    path('detail-book/<int:id>/', detail_book, name="detail_book"),
    path('', index_)
]