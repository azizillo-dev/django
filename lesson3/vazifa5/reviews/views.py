from django.http import HttpResponse


def reviews_home(request):
    return HttpResponse("Reviews home")


def reviews_list(request):
    return HttpResponse("Reviews list")
