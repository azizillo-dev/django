from django.shortcuts import render
from users.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')



def users_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', context={'users': users})

