from django.forms import ModelForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError





class RegisterForm(forms.ModelForm):
    conf_pass = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'username', 'password', 'conf_pass']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        conf_pass = cleaned_data.get("conf_pass")
        if password != conf_pass:
            raise ValidationError("Parollar mos emas")
        return cleaned_data






class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise ValidationError("Parol kamida 8 xonali bo'lishi kerak!")
        return password
        


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'address']


    def clean_username(self):
        username = self.cleaned_data['username']
        user = CustomUser.objects.exclude(
            pk=self.instance.pk
            ).filter(username=username).exists() 
        if user:
            raise ValidationError("Bu username band")
        return username
        


        



    











