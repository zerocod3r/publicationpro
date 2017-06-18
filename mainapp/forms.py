from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=100, required=False, help_text='Required.')
    password = forms.CharField(max_length=1000, required=False, help_text='Required.')
    role = forms.CharField()

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # validate email
        user = UserSignup.objects.filter(email=email)
        if user:
            raise forms.ValidationError(
                "Email already registered. Try again.")

    class Meta:
        model = UserSignup
        fields = ('email', 'name', 'password')


class LoginForm(forms.Form):
    loginemail = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    loginpassword = forms.CharField(max_length=1000, required=False, help_text='Required.')
    role = forms.CharField()
