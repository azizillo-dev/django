from django.shortcuts import render, redirect
from .models import Mebel
from .forms import MebelForm

def home(request):
    return render(request, 'home.html')


def list_(request):
    mebels = Mebel.objects.all()
    context = {
        "mebels" : mebels
    }
    return render(request, "list.html", context)


def detail(request, pk):
    mebel = Mebel.objects.get(id=pk)
    context = {
        "mebel":mebel
    }
    return render(request, "detail.html", context)


def delete(request, pk):
    mebel = Mebel.objects.get(id=pk)
    if request.method == "POST":
        mebel.delete()
        return redirect('list')
    return render(request, "delete.html", {"mebel":mebel})


def create(request):
    form =  MebelForm()
    if request.method == "POST":
        form = MebelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, "create.html", {"form":form})



def update(request, pk):
    mebel = Mebel.objects.get(id=pk)
    form = MebelForm(instance=mebel)
    if request.method == "POST":
        form = MebelForm(data=request.POST, instance=mebel)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, "update.html", {"form": form, "mebel": mebel})







