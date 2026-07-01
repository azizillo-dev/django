from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'

        



















