from .models import CustomUser
from django.forms import ModelForm, Form
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate



class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'year', 'password']



    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar mos kelmadi !")

        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        data = super().clean()
        password = data.get('password') 
        username = data.get('username') 

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Login yoki parl xato")
        

        return data