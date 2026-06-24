from django.http import HttpResponse

products = {
    1: {
        "name": "Daftar",
        "price": "12000",
        "description": "Yozish uchun chiroyli daftar"
    },
    2: {
        "name": "Ruchka",
        "price": "6000",
        "description": "Qalin siyohli ruchka"
    },
    3: {
        "name": "Termos",
        "price": "45000",
        "description": "Issiqlikni uzoq saqlovchi termos"
    }
}


def get_products(request):
    result = ""

    for product_id, product in products.items():
        result += (
            f"ID: {product_id} "
            f"Name: {product['name']} "
            f"Price: {product['price']} "
            f"Description: {product['description']}<br>"
        )

    return HttpResponse(result)
