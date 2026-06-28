"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import *
from products.views import *
from orders.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_users),
    path('names/', get_users_name),
    path('products/', get_products),
    path('product_names/', get_products_name),
    path('orders/', get_orders),
    path('orders_name/', get_orders_product)
]
