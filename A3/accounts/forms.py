from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UpdateUserForm(forms.Form):
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        data = super().clean()
        if data.get('password1') != "":
            if len(data.get('password1')) < 8:
                self.add_error('password1',
                               'This password is too short. '
                               'It must contain at least 8 characters')
            if data.get('password1') != data.get('password2'):

                self.add_error('password2',
                               "The two password fields didn't match")
        try:
            validate_email(data.get('email'))
        except ValidationError:
            self.add_error('email', 'Enter a valid email address')
        return data

    def save(self, commit=True):
        password = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if password != "":
            self.user.set_password(password)
        self.user.email = email
        self.user.first_name = first_name
        self.user.last_name = last_name
        if commit:
            self.user.save()
        return self.user


class SignupForm(forms.Form):
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def clean(self):
        data = super().clean()

        if data.get('username') == "" or data.get('username') is None:
            self.add_error('username', 'This field is required')
        if len(data.get('password1')) < 8:
            self.add_error('password1', 'This password is too short. It must '
                                        'contain at least 8 characters')
        if data.get('password1') == "" or data.get('password1') is None:
            self.add_error('password1', 'This field is required')
        if data.get('password2') == "" or data.get('password2') is None:
            self.add_error('password2', 'This field is required')
        if data.get('password1') != data.get('password2'):
            self.add_error('password2', "The two password fields didn't match")
        if User.objects.filter(username=data.get('username')).exists():
            self.add_error('username', 'A user with that username already '
                                       'exists')
        try:
            validate_email(data.get('email'))
        except ValidationError:
            self.add_error('email', 'Enter a valid email address')
        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        data = super().clean()

        if not (user := authenticate(username=data.get('username'),
                                     password=data.get('password'))):
            self.add_error('password', 'Username or password is invalid')

        data['user'] = user

        return data
