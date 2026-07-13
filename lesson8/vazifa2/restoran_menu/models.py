from django.db import models
from django.core.validators import FileExtensionValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uptdated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title




class Tag(BaseModel):   # bu anavi Vegetarian, O'tkir, Achchiq, shirin kabilar uchun
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='media/', 
        default='default.png',
        validators=[
            FileExtensionValidator(allowed_extensions = [
                    'jpg', 'png', 'webp', 'jpeg', 'gif'
                ]
            )
        ]
    )


    def __str__(self):
        return f"{self.name} {self.category.title} {self.tag.title}"


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"






