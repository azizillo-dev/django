from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.TextField()
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-id']

class Librarian(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Librarian"
        verbose_name_plural = "Librarians"
        ordering = ['-salary']















