from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'id': 'register-user-name',
        'placeholder': 'Your Username'
    }))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={
        'id': 'register-email',
        'placeholder': 'Your E-mail Address'
    }))
    password1 = forms.CharField(max_length=50, help_text='', widget=forms.PasswordInput(attrs={
        'id': 'register-password',
        'placeholder': 'Your Password'
    }))
    password2 = forms.CharField(max_length=50, help_text='', widget=forms.PasswordInput(attrs={
        'id': 'register-password-2',
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

    def get_placeholder(self):
        placeholders = []

        for field in self.fields:
            placeholders.append(self.fields[field].widget.attrs['placeholder'])

        return
