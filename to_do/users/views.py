from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            email = registration_form.cleaned_data.get('email')
            raw_password = registration_form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)

            login(request=request, user=user)

            messages.success(request=request,
                             message=f'{username}, your account has been created! You are now able to log in.')

            return redirect(to='register')

    else:
        registration_form = RegistrationForm()

        for field in registration_form:
            pass

    return render(request=request, template_name='core/index.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })
