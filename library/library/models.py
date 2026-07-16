from django.db import models
from django.core.validators import FileExtensionValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.full_name
    

class Genre(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Book(BaseModel):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    desc = models.TextField()
    published_year = models.DateField()
    pages_count = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='books/', 
        default="defaul1.jpg",
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'jpg', 'png', 'webp', 'jpeg'
            ])
        ]
    )
















