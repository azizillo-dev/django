from django.contrib import admin
from django.urls import path
from .books import get_books, get_authors, get_prices, get_titles, get_count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_books),
    path('authors/', get_authors),
    path('prices/', get_prices),
    path('titles/', get_titles),
    path('count/', get_count),
]
