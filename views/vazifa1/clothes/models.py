from django.db import models
from django.core.validators import FileExtensionValidator

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Clothes(BaseModel):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    descrition = models.TextField()
    color = models.CharField(max_length=45)
    size = models.CharField(max_length=5)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='clothes/', 
        null=True,
        blank=True,
        default='💖',
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'jpg', 'png', 'webp', 'jpeg'
            ])
        ]
    )


    def __str__(self):
        return f"{self.name}  {self.color}  {self.brand}"
    
    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"
        db_table = 'clothes'














