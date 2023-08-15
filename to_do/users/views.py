from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            username = registration_form.cleaned_data.get('username')

            login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')

            messages.success(request=request,
                             message=f'{username}, your account has been created! You are now able to log in.')

            return redirect(to='index')

    else:
        registration_form = RegistrationForm()

        for field in registration_form:
            for error in field.errors:
                pass

    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })
