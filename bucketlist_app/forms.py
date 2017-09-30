"""Module for creating forms."""
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your username'
        }))
    password = forms.CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'enter your password'
        }))


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        error_messages={'required': 'Please enter your first name'},
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your first name'
        }))
    last_name = forms.CharField(
        max_length=20,
        error_messages={'required': 'Please enter your last name'},
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your last name'
        }))
    username = forms.CharField(
        max_length=20,
        error_messages={'required': 'username is required'},
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your username'
        }))
    email_address = forms.EmailField(
        error_messages={'required': 'Email is required'},
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'placeholder': 'enter your email address'
        })
    )
    password = forms.CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'enter your password'
        }))
    password2 = forms.CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'confirm your password'
        }))
