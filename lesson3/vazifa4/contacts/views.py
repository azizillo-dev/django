from django.http import HttpResponse


def contacts_home(request):
    return HttpResponse("Contacts home")


def contacts_list(request):
    return HttpResponse("Contacts list")
