"""Module for creating forms."""

from django.forms import (
    Form,
    ModelForm,
    CharField,
    EmailField,
    TextInput,
    EmailInput,
    PasswordInput,
    CheckboxInput
)

from .models import Bucketlist, Items


class LoginForm(Form):
    username = CharField(
        max_length=20,
        error_messages={'required': 'Please enter your name'},
        widget=TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your username'
        }))
    password = CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'enter your password'
        }))


class SignUpForm(Form):
    first_name = CharField(
        max_length=20,
        error_messages={'required': 'Please enter your first name'},
        widget=TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your first name'
        }))
    last_name = CharField(
        max_length=20,
        error_messages={'required': 'Please enter your last name'},
        widget=TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your last name'
        }))
    username = CharField(
        max_length=20,
        error_messages={'required': 'username is required'},
        widget=TextInput(attrs={
            'class': 'input',
            'placeholder': 'enter your username'
        }))
    email_address = EmailField(
        error_messages={'required': 'Email is required'},
        widget=EmailInput(attrs={
            'class': 'input',
            'placeholder': 'enter your email address'
        })
    )
    password = CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'enter your password'
        }))
    password2 = CharField(
        max_length=12,
        error_messages={'required': 'Password is required'},
        widget=PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'confirm your password'
        }))


class BucketListForm(ModelForm):
    class Meta:
        model = Bucketlist
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter name for your bucketlist'
            })
        }


class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'done']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter an item'
            }),
            'done': CheckboxInput(attrs={
                'required': False
            })
        }
