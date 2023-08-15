from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username', widget=forms.TextInput(attrs={
        'id': 'register-user-name',
        'name': 'Username',
        'type': 'text',
        'placeholder': 'Your Username'
    }))
    email = forms.EmailField(max_length=255, label='E-mail Address', widget=forms.TextInput(attrs={
        'id': 'register-email',
        'name': 'Email Address',
        'type': 'text',
        'placeholder': 'Your E-mail Address'
    }))
    password1 = forms.CharField(max_length=50, label='Password', help_text='', widget=forms.PasswordInput(attrs={
        'id': 'register-password',
        'type': 'password',
        'name': 'Password',
        'placeholder': 'Your Password'
    }))
    password2 = forms.CharField(max_length=50, label='Confirm Password', help_text='',
                                widget=forms.PasswordInput(attrs={
                                    'id': 'register-password-2',
                                    'name': 'Confirm Password',
                                    'type': 'password',
                                    'placeholder': 'Confirm Password'
                                }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email

        raise forms.ValidationError(message=f'Email {email} is already in use')

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username

        raise forms.ValidationError(message=f'Username {username} is already in use')
