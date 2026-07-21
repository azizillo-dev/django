from django.shortcuts import render, redirect
from .models import Clothes
from django.views import View
from .forms import ClothesForm

def home(request):
    return render(request, 'home.html')



class ClothesListView(View):
    def get(self, request):
        clothes = Clothes.objects.all()

        context = {
            "clothes" : clothes
        }
        return render(request,'list.html', context)
    


class CreateClothes(View):
    def get(self, request):
        form = ClothesForm()
        return render(request, 'clothes_create.html', {"form" : form})


    def post(self, request):
        form = ClothesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        
        return render(request, 'clothes_create.html', {"form" : form})
