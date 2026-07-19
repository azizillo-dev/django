from django.shortcuts import render
from .models import CustomUser
from django.views import View




class RegisterView(View):


    def get(self, request):
        return render(request, 'auth/register.html')


