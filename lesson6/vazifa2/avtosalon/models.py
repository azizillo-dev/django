from django.db import models


# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        db_table = "cars"
        












