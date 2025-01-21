from email.policy import default

from django import forms
from django.contrib.auth.models import User
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.get(username=username)
        if user:
            return username
        raise forms.ValidationError("Username does not exist")

    def check_user(self):
        user = User.objects.get(username=self.cleaned_data["username"])
        if user.check_password(self.cleaned_data["password"]):
            return user
        raise forms.ValidationError("Wrong password")
