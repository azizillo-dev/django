from django.db import models
from django.contrib.auth.models import AbstractUser, User



class CustomUser(AbstractUser):
    address = models.CharField(max_length=40)
    year = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return self.username
    

    






