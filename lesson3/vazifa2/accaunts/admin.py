from django.contrib import admin
from .models import Seller, Customer
# Register your models here.

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'is_verified')
    list_filter = ('city', 'is_verified')
    search_fields = ('full_name', 'email', 'phone', 'city')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'is_verified')
    list_filter = ('city', 'is_verified')
    search_fields = ('full_name', 'email', 'phone', 'city')
