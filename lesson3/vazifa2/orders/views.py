from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.

orders_data = [
    {
        "id": 1,
        "customer": "Aziz Karimov",
        "product": "iPhone 15",
        "quantity": 1,
        "total_price": 1200,
        "status": "Delivered"
    },
    {
        "id": 2,
        "customer": "Ali Valiyev",
        "product": "MacBook Air M2",
        "quantity": 1,
        "total_price": 1500,
        "status": "Pending"
    },
    {
        "id": 3,
        "customer": "Jasur Rahimov",
        "product": "AirPods Pro",
        "quantity": 2,
        "total_price": 500,
        "status": "Delivered"
    },
    {
        "id": 4,
        "customer": "Bekzod Ergashev",
        "product": "iPad Air",
        "quantity": 1,
        "total_price": 700,
        "status": "Cancelled"
    },
    {
        "id": 5,
        "customer": "Sardor Tursunov",
        "product": "Apple Watch",
        "quantity": 3,
        "total_price": 1350,
        "status": "Pending"
    }
]   



def get_orders(request):
    result = ""

    for i in orders_data:
        result += (
            f"ID: {i["id"]}"
            f"Product: {i["product"]}"
            f"Customer: {i["customer"]}"
            f"Total Price: ${i["total_price"]}"
            f"Quantity: {i["quantity"]}"
            f"Status: {i["status"]}<br>")

    return HttpResponse(result)




def get_orders_product(request):
    result = ""

    for i in orders_data:
        result += f"{i["product"]}<br>"

    return HttpResponse(result)



