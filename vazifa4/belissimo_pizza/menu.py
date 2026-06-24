from django.http import HttpResponse

pizzas = {
    1: {"name": "Margherita", "price": "35000"},
    2: {"name": "Pepperoni", "price": "42000"},
    3: {"name": "Four Cheese", "price": "48000"}
}

burgers = {
    1: {"name": "Classic Burger", "price": "30000"},
    2: {"name": "Cheese Burger", "price": "34000"},
    3: {"name": "Double Burger", "price": "42000"}
}

lavashlar = {
    1: {"name": "Chicken Lavash", "price": "28000"},
    2: {"name": "Beef Lavash", "price": "30000"},
    3: {"name": "Vegetable Lavash", "price": "26000"}
}

ichimliklar = {
    1: {"name": "Coca-Cola", "price": "8000"},
    2: {"name": "Fanta", "price": "8000"},
    3: {"name": "Mineral Water", "price": "6000"}
}


def get_pizzas(request):
    result = ""
    for item_id, item in pizzas.items():
        result += f"ID: {item_id} Name: {item['name']} Price: {item['price']}<br>"
    return HttpResponse(result)


def get_burgers(request):
    result = ""
    for item_id, item in burgers.items():
        result += f"ID: {item_id} Name: {item['name']} Price: {item['price']}<br>"
    return HttpResponse(result)


def get_lavash(request):
    result = ""
    for item_id, item in lavashlar.items():
        result += f"ID: {item_id} Name: {item['name']} Price: {item['price']}<br>"
    return HttpResponse(result)


def get_ichimlik(request):
    result = ""
    for item_id, item in ichimliklar.items():
        result += f"ID: {item_id} Name: {item['name']} Price: {item['price']}<br>"
    return HttpResponse(result)
