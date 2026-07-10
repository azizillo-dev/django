from django.shortcuts import render, redirect
from .models import Watch
from .forms import WatchForm

# Create your views here.


def home_page(request):
    watches = Watch.objects.all()
    return render(request, 'home_page.html', context={'watches': watches})



def create_watch(request):
    form = WatchForm()
    if request.method == "POST":
        form = WatchForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context = {
        "form" : form
    }
    return render(request, 'create_watch.html', context)
    #     name = request.POST.get("name")
    #     model = request.POST.get("model")
    #     price = request.POST.get("price")
    #     description = request.POST.get("description")
    #     mexanism = request.POST.get("mexanism")
    #     color = request.POST.get("color")
    #     remenka = request.POST.get("remenka")
    #     shape = request.POST.get("shape")

    #     Watch.objects.create(
    #         name=name,
    #         model=model,
    #         price=price,
    #         description=description,
    #         mexanism=mexanism,
    #         color=color,
    #         remenka=remenka,
    #         shape=shape
    #     )
    #     return redirect('home_page') 
        
    # return render(request, 'create_watch.html')





def delete_watch(request, pk):
    watch = Watch.objects.get(id=pk)
    if request.method == "POST":
        watch.delete()
        return redirect('home_page')
    return render(request, 'delete.html', context={"watch" : watch})


















