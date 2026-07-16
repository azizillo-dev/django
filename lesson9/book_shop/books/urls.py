from django.urls import path
from .views import *



urlpatterns = [
    path('', home_page),
    path('create-book/', create_book, name="create"),
    path('detail-book/<int:pk>', detail_book, name = "detail"),
    path('delete-book/<int:pk>', delete_book, name = 'delete'),
    path('book-list/', book_list, name = 'list'),
    path('update-book/<int:pk>', update_book, name = 'update'),
    path('category/<int:pk>', book_category, name='categories'),    path('author/<str:author>', author_books, name='author'),
]