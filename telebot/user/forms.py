from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=100, 
        label='Email',
        error_messages={
            'required': 'Email is required',
        }
    )

    password = forms.CharField(
        max_length=50,
        label='Password',
        error_messages={
            'required': 'Password is required',
        },
        widget=forms.PasswordInput
    )

    re_password = forms.CharField(
        max_length=50,
        label='Re-Password',
        error_messages={
            'required': 'Re-Password is required',
        },
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                raise forms.ValidationError('Password does not match')
            else:
                user = User(
                    email=cleaned_data.get('email'),
                    password=cleaned_data.get('password')
                )
                user.save()

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        label='Email',
        error_messages={
            'required': 'Email is required',
        }
    )
    password = forms.CharField(
        max_length=50,
        label='Password',
        error_messages={
            'required': 'Password is required',
        },
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if password and email:
            try:
                user = User.objects.get(email=email)
                if user.password != password:
                    raise forms.ValidationError('Password does not match')
                else:
                    self.email = user.email
            except User.DoesNotExist:
                raise forms.ValidationError('User does not exist')
