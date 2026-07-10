from django.db import models

class Mebel(models.Model):
    KATEGORIYA_CHOICES = [
        ('divan', 'Divan'),
        ('stol', 'Stol'),
        ('stul', 'Stul'),
        ('shkaf', 'Shkaf'),
        ('karavot', 'Karavot'),
        ('boshqa', 'Boshqa'),
    ]

    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=KATEGORIYA_CHOICES, default='boshqa')
    material = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    count = models.PositiveIntegerField(default=1)
    desc = models.TextField(blank=True, null=True)
    is_have = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mebel"
        verbose_name_plural = "Mebellar"
