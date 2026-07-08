from django.shortcuts import redirect, render
from .models import Computer
# Create your views here.


def create_computer(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        name = request.POST.get("name")
        price = request.POST.get("price")
        screen_info = request.POST.get("screen_info")
        gpu = request.POST.get("gpu")
        created_at = request.POST.get("created_at")

        computer = Computer(
            brand = brand, 
            name = name, 
            price = price, 
            screen_info = screen_info, 
            gpu = gpu, 
            created_at =created_at
        )
        computer.save() 
        return redirect("home_page")

    return render(request, "create_computer.html")
     






def home_page(request):
    computers = Computer.objects.all()
    context = {
        "computers": computers
    }
    return render(request, "home.html", context)




def delete_computer(request, pk):
    computer = Computer.objects.get(id=pk)
    computer.delete()
    return redirect("home_page")






