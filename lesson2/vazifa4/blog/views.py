from django.http import HttpResponse


def blog_home(request):
    return HttpResponse("Blog home")


def blog_list(request):
    return HttpResponse("Blog list")
