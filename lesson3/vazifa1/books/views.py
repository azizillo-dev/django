from django.shortcuts import render
from django.http import HttpResponse


# sample in-memory books data (similar to lesson2 example)
books = {
	1: {"title": "Olamning Quloqchasi", "author": "Xurshid Davron", "price": "25000"},
	2: {"title": "Sariq Devni minib", "author": "O'tkir Hoshimov", "price": "18000"},
	3: {"title": "Zulmat va Nur", "author": "Muhammad Yusuf", "price": "22000"},
}


def get_books(request):
	
    result = ""
	
    for book_id, book in books.items():
        result += f"ID: {book_id}, Title: {book['title']}<br>, Author: {book['author']}<br>, Price: {book['price']}<br>"

    return HttpResponse(result)
	


def get_authors(request):
    result = ""

    for book_id, book in books.items():
        result += f"ID: {book_id}: {book['author']}\n"

    return HttpResponse(result)












