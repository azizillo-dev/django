from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

users_data = [
    {
        "id": 1,
        "name": "Aziz",
        "age": 20,
        "city": "Toshkent"
    },
    {
        "id": 2,
        "name": "Ali",
        "age": 22,
        "city": "Samarqand"
    },
    {
        "id": 3,
        "name": "Vali",
        "age": 19,
        "city": "Buxoro"
    },
    {
        "id": 4,
        "name": "Sardor",
        "age": 25,
        "city": "Andijon"
    }
]




def get_users(request):
    result = ""

    for i in users_data:
        result += f"ID: {i["id"]} Name: {i["name"]} Age : {i["age"]} City : {i["city"]}<br>"

    return HttpResponse(result)


def get_users_name(request):
    names = ""
    for i in users_data:
        names += f"{i["name"]}<br>"

    return HttpResponse(names)




def footer(request):
    return HttpResponse("<h1 style = 'color:red'>Bu saytni footer qismi</h1>")






