from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True,null=True, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'





















































