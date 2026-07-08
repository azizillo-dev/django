from django.shortcuts import render, redirect
from .models import Car
# Create your views here.


def home_page(request):
    pass




def create_car(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        price = request.POST.get("price")
        year = request.POST.get("year")
        mileage = request.POST.get("mileage")
        color = request.POST.get("color")

        car = Car.objects.create(
            brand = brand,
            model = model,
            price = price,
            year = year,
            mileage = mileage,
            color = color
        )

        return redirect('home_page')

    return render(request, 'create.html')





def home_page(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, "home.html", context)





def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return redirect("home_page")





def detail_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        "car": car
    }
    return render(request, "detail.html", context)

