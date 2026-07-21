from django.db import models
from django.core.validators import FileExtensionValidator




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
    

class Category(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Book(BaseModel):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    desc = models.TextField()
    published_year = models.DateField()
    pages_count = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='books/', 
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'jpg', 'png', 'webp', 'jpeg'
            ])
        ]
    )




















