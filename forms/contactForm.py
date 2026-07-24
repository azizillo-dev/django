from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(unique=True)
    subject = forms.CharField(max_length=100)
    message = forms.Textarea()



    def claen_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("Name must be minimal 3 characters")
        return name





