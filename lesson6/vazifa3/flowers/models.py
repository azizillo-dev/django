from django.db import models

# Create your models here.


class Flower(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    desc = models.TextField()
    is_tikonli = models.BooleanField(default=False)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Flower"
        verbose_name_plural = "Flowers"
        db_table = "flowers"








