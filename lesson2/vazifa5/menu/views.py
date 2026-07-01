from django.http import HttpResponse


def menu_home(request):
    return HttpResponse("Menu home")


def menu_list(request):
    return HttpResponse("Menu list")
