from django.shortcuts import render, redirect
from .models import CustomUser
from django.views import View


def home(request):
    return redirect('home')



class RegisterView(View):


    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        year = request.POST.get('year')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        CustomUser.objects.create(
            first_name = first_name, 
            last_name = last_name,
            year = year,
            username = username,
            password = password,
            address = address
        )

        return redirect('home')
    
    


