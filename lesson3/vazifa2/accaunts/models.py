from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=30)
    address = models.TextField()
    birthday = models.DateField()
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customers'


class Seller(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=30)
    address = models.TextField()
    birthday = models.DateField()
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
        db_table = 'sellers'    



















