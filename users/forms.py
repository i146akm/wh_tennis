from django import forms
from django.contrib.auth.models import User
from . import models


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your username'
        }
    ))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your password'
        }
    ))

    def check_account(self):
        user = User.objects.get(username=self.cleaned_data["username"])
        if user.check_password(self.cleaned_data["password"]):
            return user
        return False