from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import BookForm



def home_page(request):
    return render(request, 'home.html')


def book_list(request):
    books = Book.objects.all()  
    context = {
        "books" : books
    }
    return render(request, "list.html", context)


def create_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()

    context = {
        "form": form
    }
    return render(request, 'create.html', context)

def detail_book(request, pk):
    book = get_object_or_404(Book, id=pk)   # ✅ to'g'ri

    context = {
        "book": book
    }
    return render(request, "detail.html", context)




def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect('list')
    context = {
        "book" : book
    }
    return render(request, "delete.html", context)





def update_book(request, pk):
    book = Book.objects.get_object_or_404(id=pk)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form" : form
    }   

    return render(request, "update.html", context)



def book_category(request, pk):
    books = Book.objects.filter(category_id=pk)

    if not books.exists():
        return HttpResponse("Bunday kategoriyadagi kitoblar mavjud emas!")

    return render(request, "book_category.html", {
        "books": books
    })


def author_books(request, author):
    books = Book.objects.filter(author=author)

    if not books:
        return HttpResponse("Bu  authorda kitoblar mavjud emas !")
    return render(request, 'author_book.html', {"books" : books})












