from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError

def dashboard(request):
    return render(request, 'dashboard.html')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request, 'auth/register.html', context)
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        context = {
            "form" : form
        }
        return render(request, 'auth/register.html', context)
    



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {"form" : form})
    
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Login yoki parol xato")
            login(request, user)
            return redirect('dashboard')



















