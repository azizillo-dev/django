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

    # def clean(self):
    #     data = super().clean()
    #     username = data.get('username')
    #     password = data.get('password')

    #     user = authenticate(password=password, username=username)
        
    #     if not user:
    #         raise ValidationError("Login yoki parol xato")
    #     return data



class ProfileUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone','username','address', 'image']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists()
        if user:
            raise ValidationError("Bu username band")
        return username





class ChangePassForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise ValidationError("Yangi parollar mos emas.")

        return cleaned_data












