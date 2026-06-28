from django.http import HttpResponse


def orders_home(request):
    return HttpResponse("Orders home")


def orders_list(request):
    return HttpResponse("Orders list")
