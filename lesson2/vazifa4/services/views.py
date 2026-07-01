from django.http import HttpResponse


def services_home(request):
    return HttpResponse("Services home")


def services_list(request):
    return HttpResponse("Services list")
