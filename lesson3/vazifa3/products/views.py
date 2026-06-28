from django.http import HttpResponse


def products_home(request):
    return HttpResponse("Products home")


def products_list(request):
    return HttpResponse("Products list")
