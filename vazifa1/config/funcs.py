
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bosh sahifa")

def contact(request):
    return HttpResponse("Aloqa")

def courses(request):
    return HttpResponse("Kurslar")

def students(request):
    return HttpResponse("Talabalar")

def teachers(request):
    return HttpResponse("O'qituvchilar")













