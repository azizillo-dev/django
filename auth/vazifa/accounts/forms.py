from .models import CustomUser
from django.forms import ModelForm, Form
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(ModelForm):
    confirm_password = forms.CharField()
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'year', 'password']



    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and self.confirm_password and password != self.confirm_password:
            raise ValidationError("Parollar mos kelmadi !")

        return data

