from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegisterForm
from django.views import View


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
            return redirect('dashboard')
        context = {
            "form" : form
        }
        return render(request, 'auth/register.html', context)
    




















