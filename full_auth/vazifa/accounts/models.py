from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):

    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', "Female"


    phone = models.CharField(unique=True, blank=True, max_length=20)
    address = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, choices=Gender.choices, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
    











