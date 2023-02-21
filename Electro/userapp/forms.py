from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import User


class UserCreationForm(BaseUserCreationForm):
    mobile = forms.CharField(max_length=13, required=True, help_text='Phone number')

    class Meta:
        model = User
        fields = ['first_name','username','email','mobile','password1','password2']