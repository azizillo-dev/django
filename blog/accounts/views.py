from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegisterForm,LoginForm
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin




class DashboarView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'auth/dashboard.html')
    

class LandingPageView(View):
    def get(self, request):
        return render(request, 'landingpage.html')




class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/register.html', {"form" : form})
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                phone = data['phone'],
                username = data['username']
            )
            user.set_password(data['password'])
            user.save()
            return redirect('accounts:login')
        return render(request, 'auth/register.html', {"form" : form})

            

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {"form" : form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('accounts:dashboard')
            form.add_error(None, "Login yoki parol xato")
        
        return render(request, 'auth/login.html', {"form" : form})






























