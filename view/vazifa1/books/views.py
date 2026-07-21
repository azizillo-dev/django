from django.shortcuts import render, redirect
from .models import Book, Category, Author
from django.views import View
from .forms import BookForm


app_name = "books"

def home(request):
    return render(request, "home.html")


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()

        return render(request, 'book_list.html', context = {"books":books})
    


class BookCreate(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'book_form.html', context={'form': form})

    def post(self, request):
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
        return render(request, 'book_form.html', context={'form': form})





