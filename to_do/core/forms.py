from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True, label='Full Name', widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Your Full Name'
    }))
    email = forms.CharField(max_length=50, required=True, label='Email Address', widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Your E-mail Address'
    }))
    message = forms.CharField(max_length=1000, widget=(forms.Textarea(attrs={
        'type': 'text',
        'placeholder': 'Your Message'
    })))
