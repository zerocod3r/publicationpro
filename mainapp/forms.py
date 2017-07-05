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
        role = cleaned_data.get("role")
        # validate email
        if role == 'Author':
            user = UserSignup.objects.filter(email=email)
            if user:
                raise forms.ValidationError(
                    "Email already registered. Try again.")
        elif role == 'Publisher':
            user = PubSignup.objects.filter(email=email)
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


class SaveProfilePublisher(forms.Form):
    profileimage = forms.ImageField()
    fullname = forms.CharField(max_length=100, help_text='Required.')
    companyname = forms.CharField(max_length=254, required=False, help_text='Required.')
    companywebsite = forms.CharField(max_length=254, required=False, help_text='Required.')
    aboutcmpny = forms.CharField(max_length=1000, required=False, help_text='Required.', widget=forms.Textarea)
    address = forms.CharField(max_length=1000, required=False, help_text='Required.', widget=forms.Textarea)
    phoneno = forms.CharField(max_length=1000, required=False, help_text='Required.')


class SaveProfileUser(forms.Form):
    profileimage = forms.ImageField()
    full_name = forms.CharField(max_length=100, help_text='Required.')
    birth_date = forms.CharField(max_length=100, help_text='Required.')
    books_wrote = forms.CharField(max_length=100, help_text='Required.')
    journal_wrote = forms.CharField(max_length=100, help_text='Required.', widget=forms.Textarea)
    experience = forms.CharField(max_length=1000, help_text='Required.', widget=forms.Textarea)
    address = forms.CharField(max_length=1000, required=False, help_text='Required.', widget=forms.Textarea)
    phoneno = forms.CharField(max_length=1000, required=False, help_text='Required.')


class SaveManuscriptDetails(forms.Form):
    title = forms.CharField(max_length=200, help_text='Required.')
    department = forms.CharField(max_length=200, help_text='Required.')
    name = forms.CharField(max_length=200, help_text='Required.')
    phone = forms.CharField(max_length=12, help_text='Required.')
    mtitle = forms.CharField(max_length=1000, help_text='Required.', widget=forms.Textarea)
    mabstract = forms.CharField(max_length=2000, help_text='Required.', widget=forms.Textarea)
    mdocfile = forms.FileField()


class UpdateStatusManuscript(forms.Form):
    status = forms.CharField()
