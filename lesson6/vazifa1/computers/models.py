from django.db import models

# Create your models here.


class Computer(models.Model):
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    screen_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    gpu = models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.brand}  {self.name}"
    

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"
        db_table = "computers"









