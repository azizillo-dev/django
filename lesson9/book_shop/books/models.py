from django.db import models




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name



class Book(BaseModel):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='books'
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    image = models.ImageField(upload_to='media/', default='default1.jpg')
    

    def __str__(self):
        return f"{self.title} {self.category} {self.author}"
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"








