from django.http import HttpResponse


def users_home(request):
    return HttpResponse("Users home")


def users_list(request):
    return HttpResponse("Users list")
