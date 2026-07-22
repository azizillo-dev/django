from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegisterForm, LoginForm, ProfileUpdateForm, ChangePassForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
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
            return redirect('accounts:login')
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

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')
            else:
                form.add_error(None, "Login yoki parol xato")
                
        return render(request, 'auth/login.html', {"form" : form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')








class ProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'auth/profile.html', {"user": user})



class ProfileUpdateView(View):
    def get(self, request):
        user = request.user
        form = ProfileUpdateForm(instance=user)
        return render(request, 'auth/profile_update.html', {"form" : form})
    
    def post(self, request):
        user = request.user
        form = ProfileUpdateForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        
        return render(request, 'auth/profile_update.html', {"form" : form})



class ChangePassView(View):
    def get(self, request):
        form = ChangePassForm()
        return render(request, 'auth/change_pass.html', {"form" : form})
    

    def post(self, request):
        form = ChangePassForm(data=request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get("password")
            new_password = form.cleaned_data.get("new_password")

            user = authenticate(request, username=request.user.username, password=old_password)

            if user is None:
                form.add_error('password', "Eski parol xato")
            else:
                user.set_password(new_password)
                user.save()
                return redirect('accounts:profile')
        return render(request, 'auth/change_pass.html', {'form': form})


