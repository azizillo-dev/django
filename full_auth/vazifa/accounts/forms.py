from django.forms import ModelForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate




class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone','username',     'address', 'password']



    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar mos kelmadi")
        
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        username = data.get('userneme')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar mos emas")
        user = authenticate(password=password, username=username)
        
        if not user:
            raise ValidationError("Login yoki parol xato")
        return data







