from django.forms import ModelForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError




class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone','username', 'password']



    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar mos kelmadi")
        
        return data










