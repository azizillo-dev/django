from django.db import models




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Movie(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    rating = models.FloatField()


    def __str__(self):
        return self.title






