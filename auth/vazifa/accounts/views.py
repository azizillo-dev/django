from django.shortcuts import render, redirect
from .models import CustomUser
from django.views import View
from django.core.exceptions import ValidationError
from .forms import RegisterForm









def home(request):
    return render(request, 'home.html')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/register.html', {"form" : form})
    

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
        return render(request, 'auth/register.html', {"form" : form})


    # bu bitta usul edi

    # def post(self, request):
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     year = request.POST.get('year')
    #     address = request.POST.get('address')
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     confrim_password = request.POST.get('confirm_password')
    #     if confrim_password != password:
    #         raise ValidationError("Parollar mos emas")

    #     # CustomUser.objects.create_user(
    #     #     first_name = first_name, 
    #     #     last_name = last_name,
    #     #     year = year,
    #     #     username = username,
    #     #     password = password,
    #     #     address = address
    #     # )


    #     user = CustomUser(
    #         first_name = first_name, 
    #         last_name = last_name,
    #         year = year,
    #         username = username,
    #         password = password,
    #         address = address
    #     )
    #     user.set_password(password)
    #     user.save()

    #     return redirect('home')
    
    


