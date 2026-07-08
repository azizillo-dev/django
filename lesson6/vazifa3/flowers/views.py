from django.shortcuts import render, redirect
from .models import Flower
# Create your views here.


def create_flower(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        color = request.POST.get("color")
        is_tikonli = request.POST.get("is_tikonli")== "on"

        Flower.objects.create(
            name = name,
            price = price,
            desc = desc,
            color = color,
            is_tikonli = is_tikonli
        )
        return redirect("home_page")
    return render(request, 'create.html')
        



def home_page(request):
    
    flowers = Flower.objects.all()
    context = {
        "flowers" : flowers
    }
    return render(request, "home.html", context)



def delete(request, id):
    flower = Flower.objects.get(id=id)
    if request.method == "POST":
        flower.delete()
        return redirect("home_page")

    context = {
        "flower": flower
    }

    return render(request, "delete.html", context)


def detail(request, id):
    flower = Flower.objects.get(id=id)
    context = {
        "flower" : flower
    }
    return render(request, "detail.html", context)  










