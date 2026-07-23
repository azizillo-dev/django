from django.shortcuts import render
from .models import Book
# Create your views here.


def book_list(request):
    books = Book.objects.all()

    context = {
        "books" : books
    }
    return render(request, "list.html", context)



def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        count = request.POST.get("count")

        Book.objects.create(title=title, author=author, price=price, desc=desc, count=count)
    return render(request, "add_book.html")





def detail_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        "book" : book
    }
    return render(request, "detail.html", context)



def index_(request):
    return render(request, "index.html")




