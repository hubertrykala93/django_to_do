from string import ascii_letters, digits
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    characters = ','.join([ascii_letters + digits])

    if len(username) <= 4:
        raise ValidationError(_('The username should consist of at least 7 characters.'), params={'username': username})

    for letter in username:
        if letter not in characters:
            raise ValidationError(_(
                'The username can consist only of lowercase letters, uppercase letters, and/or numbers.'),
                params={'username': username})


def validate_email(email):
    if '@' not in email:
        raise ValidationError(_('The email should contains @.'), params={'email': email})
