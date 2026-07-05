from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    desc = models.TextField()
    count = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"


