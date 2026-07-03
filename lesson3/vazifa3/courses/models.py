from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    faculty = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"












