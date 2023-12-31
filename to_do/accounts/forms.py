from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django import forms
from .models import User, Profile
from django.core.validators import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username', required=True,
                               widget=forms.TextInput(attrs={
                                   'id': 'register-user-name',
                                   'label': 'required',
                                   'type': 'text',
                                   'placeholder': 'Your Username'
                               }))

    email = forms.EmailField(max_length=255, label='E-mail Address', required=True,
                             validators=[ValidationError],
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your E-mail Address'
                             }))

    password1 = forms.CharField(max_length=50, label='Password', required=True,
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

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username__iexact=username, is_active=True).exists():
            raise ValidationError(message='The user with this name already exists.')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError(message='The user with this address e-mail already exists.')

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Username', required=False,
                               widget=forms.TextInput(attrs={
                                   'id': 'register-user-name',
                                   'label': 'required',
                                   'type': 'text',
                                   'placeholder': 'Your New Username'
                               }))

    email = forms.EmailField(max_length=255, label='E-mail Address', required=False,
                             validators=[ValidationError],
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your New E-mail Address'
                             }))

    class Meta:
        model = User
        fields = ['username', 'email']


class PasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, label='New Password', required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'register-password',
                                        'type': 'password',
                                        'label': 'required',
                                        'placeholder': 'Your New Password'
                                    }))

    new_password2 = forms.CharField(max_length=50, label='Confirm New Password', required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'id': 'register-password-2',
                                        'type': 'password',
                                        'label': 'required',
                                        'placeholder': 'Confirm Your New Password'
                                    }))

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class UserImageUpdateForm(forms.ModelForm):
    image = forms.ImageField(max_length=100, required=False, widget=forms.FileInput(attrs={
        'type': 'file',
        'name': 'file',
        'id': 'id_file',
    }))

    class Meta:
        model = User
        fields = ['image']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, label='First Name', required=False,
                                 widget=forms.TextInput(attrs={
                                     'id': 'register-user-first-name',
                                     'label': 'required',
                                     'type': 'text',
                                     'placeholder': 'Your First Name'
                                 }))

    last_name = forms.CharField(max_length=255, label='Last Name', required=False,
                                widget=forms.TextInput(attrs={
                                    'id': 'register-user-last-name',
                                    'type': 'text',
                                    'placeholder': 'Your Last Name'
                                }))

    gender = forms.Select(choices=(
        ('Not Defined', 'Not Defined'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ))

    date_of_birth = forms.CharField(label='Date of Birth', required=False, widget=forms.TextInput(attrs={
        'id': 'register-user-date-of-birth',
        'type': 'text',
        'placeholder': 'Your Date of Birth'
    }))

    country = forms.CharField(max_length=255, label='Country', required=False,
                              widget=forms.TextInput(attrs={
                                  'id': 'register-user-country',
                                  'type': 'text',
                                  'placeholder': 'Your Country'
                              }))

    province = forms.CharField(max_length=255, label='Province', required=False,
                               widget=forms.TextInput(attrs={
                                   'id': 'register-user-province',
                                   'type': 'text',
                                   'placeholder': 'Your Province'
                               }))

    city = forms.CharField(max_length=255, label='City', required=False,
                           widget=forms.TextInput(attrs={
                               'id': 'register-user-city',
                               'type': 'text',
                               'placeholder': 'Your City'
                           }))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'country', 'province', 'city']


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, label='E-mail Address', required=True,
                             widget=forms.TextInput(attrs={
                                 'id': 'register-email',
                                 'label': 'required',
                                 'type': 'text',
                                 'placeholder': 'Your E-mail Address'
                             }))

    def clean_email(self):
        email = self.cleaned_data['email']

        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError(f"This address e-mail doesn't exists.")

        return email
