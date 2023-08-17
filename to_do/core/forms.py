from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True, label='Full Name')
    email = forms.CharField(max_length=50, required=True, label='Email Address')
    mobile_phone = forms.CharField(max_length=50, required=False, label='Phone Number')
    message = forms.CharField(max_length=1000, widget=forms.Textarea)
    file = forms.FileField(required=False)
