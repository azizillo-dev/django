from django.forms import ModelForm
from .models import Mebel
from django.core.exceptions import ValidationError

class MebelForm(ModelForm):
    class Meta:
        model = Mebel
        fields = "__all__"



def clean_price(self):
    price = self.cleaned_data.get('price')    
    if price <= 0:
        raise ValidationError("Narx 0 dan katta bo'lishi kerak")
    return price

def clean_count(self):
    count = self.cleaned_data.get('count')
    if count < 0:
        raise ValidationError("Soni manfiy bo'lishi mumkin emas")
    return count










