from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 1200,
        "stock": 8
    },
    {
        "id": 2,
        "name": "MacBook Air M2",
        "price": 1500,
        "stock": 3
    },
    {
        "id": 3,
        "name": "AirPods Pro",
        "price": 250,
        "stock": 15
    },
    {
        "id": 4,
        "name": "iPad Air",
        "price": 700,
        "stock": 6
    }
]




def get_products(request):
    result = ""

    for i in products:
        result += f'ID: {i["id"]} Name: {i["name"]} Price: ${i["price"]} Stock: {i["stock"]}<br>'

    return HttpResponse(result)


def get_products_name(request):
    names = ""

    for i in products:
        names += f'{i["name"]}<br>'

    return HttpResponse(names)


