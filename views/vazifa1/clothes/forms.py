from django.forms import ModelForm
from .models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'brand', 'price', 'color', 'category', 'size', 'description']

        

    






