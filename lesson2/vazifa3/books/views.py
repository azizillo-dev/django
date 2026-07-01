from django.http import HttpResponse


def books_home(request):
    return HttpResponse("Books home")


def books_list(request):
    return HttpResponse("Books list")
