from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title



class Producer(BaseModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    address = models.TextField()


    def __str__(self):
        return self.full_name



class Movie(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to='movies/', 
        default='default.jpg',
        validators=[
            # MinLengthValidator(1), 
            # MaxLengthValidator(30),
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp'])
        ]
    )
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    rating = models.FloatField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} {self.producer.full_name} {self.category.title}"


    


