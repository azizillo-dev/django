from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField()
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-published_date']








