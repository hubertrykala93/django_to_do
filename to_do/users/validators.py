from string import ascii_letters, digits
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    characters = ascii_letters + digits

    if len(username) <= 4:
        raise ValidationError(_('The username should consist of at least 7 characters.'), params={'username': username})

    for letter in username:
        if letter not in characters:
            raise ValidationError(message=_(
                'The username can consist only of lowercase letters and/or uppercase letters, and/or numbers.'),
                params={'username': username})


def validate_email(email):
    if '@' not in email:
        raise ValidationError(message=_("The email should contains @."), params={'email': email})

    if email.count('@') > 1:
        raise ValidationError(message=_("The email should contains only one '@' symbol."), params={'email': email})

    if ' ' in email:
        raise ValidationError(message=_("The email shouldn't contains ' '."), params={'email': email})

    domain = email[email.rfind('@') + 1:email.rfind('.')]

    for letter in domain:
        if letter not in ascii_letters + digits:
            raise ValidationError(
                message=_('The domain can consist only of lowercase letters and/or uppercase letters, and/or numbers.'),
                params={'email': email})

    domain_extension = email[email.rfind('.') + 1:]

    for letter in domain_extension:
        if letter not in ascii_letters:
            raise ValidationError(
                message=_('The domain extension can consist only of lowercase letters and/or uppercase letters.'),
                params={'email': email})

    return email


def validate_password(password):
    if len(password) < 8:
        print('The password must consists of at least 8 characters.')

    lower_letters = []
    upper_letters = []
    numbers = []
    symbols = []

    for letter in password:
        if letter.islower():
            lower_letters.append(letter)

        if letter.isupper():
            upper_letters.append(letter)

        if letter.isdigit():
            numbers.append(letter)

        if letter.isprintable() and not letter.isupper() and not letter.islower() and not letter.isdigit():
            symbols.append(letter)

    if len(lower_letters) < 1:
        raise ValidationError(message=_('The password must contains at least one lowercase letter.'),
                              params={'password': password})

    if len(upper_letters) < 1:
        raise ValidationError(message=_('The password must contains at least one uppercase letter.'),
                              params={'password': password})

    if len(numbers) < 1:
        raise ValidationError(message=_('The password must contain at least one digit.'), params={'password': password})

    if len(symbols) < 1:
        raise ValidationError(message=_("The password must contains at least one symbol like '!, @, #, $'."),
                              params={'password': password})

    return password
