from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django import forms
from .models import User, Profile
from .validators import username_validate, email_validate, password_validate


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username', required=True, validators=[username_validate],
                               widget=forms.TextInput(attrs={
                                   'id': 'register-user-name',
                                   'label': 'required',
                                   'type': 'text',
                                   'placeholder': 'Your Username'
                               }))

    email = forms.EmailField(max_length=255, label='E-mail Address', required=True, validators=[email_validate],
                             error_messages=None,
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your E-mail Address'
                             }))

    password1 = forms.CharField(max_length=50, label='Password', required=True, validators=[password_validate],
                                widget=forms.PasswordInput(attrs={
                                    'id': 'register-password',
                                    'type': 'password',
                                    'label': 'required',
                                    'placeholder': 'Your Password'
                                }))

    password2 = forms.CharField(max_length=50, label='Confirm Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'id': 'register-password-2',
                                    'type': 'password',
                                    'label': 'required',
                                    'placeholder': 'Confirm Password'
                                }))
    first_name = forms.CharField(max_length=255, label='First Name', required=True,
                                 widget=forms.TextInput(attrs={
                                     'id': 'register-user-first-name',
                                     'label': 'required',
                                     'type': 'text',
                                     'placeholder': 'Your First Name'
                                 }))

    gender = forms.Select(attrs={
        'class': 'form-control'
    }, choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'gender']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, label='First Name', required=True,
                                 widget=forms.TextInput(attrs={
                                     'id': 'register-user-first-name',
                                     'label': 'required',
                                     'type': 'text',
                                     'placeholder': 'Your First Name'
                                 }))

    username = forms.CharField(max_length=255, label='Username', required=True, validators=[username_validate],
                               widget=forms.TextInput(attrs={
                                   'id': 'register-user-name',
                                   'label': 'required',
                                   'type': 'text',
                                   'placeholder': 'Your Username'
                               }))

    email = forms.EmailField(max_length=255, label='E-mail Address', required=True, validators=[email_validate],
                             error_messages=None,
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your New E-mail Address'
                             }))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'first_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class PasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, label='New Password', required=True, validators=[password_validate],
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'register-password',
                                        'type': 'password',
                                        'label': 'required',
                                        'placeholder': 'Your New Password'
                                    }))

    new_password2 = forms.CharField(max_length=50, label='Confirm New Password', required=True,
                                    validators=[password_validate], widget=forms.PasswordInput(attrs={
            'id': 'register-password-2',
            'type': 'password',
            'label': 'required',
            'placeholder': 'Confirm Your New Password'
        }))

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, label='E-mail Address', required=True, validators=[email_validate],
                             error_messages=None,
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your E-mail Address'
                             }))
