from .models import CustomUser
from django.forms import ModelForm, Form


class RegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'year', 'password']







