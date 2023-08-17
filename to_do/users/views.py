from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST or None)

        if registration_form.is_valid():
            user = registration_form.save(commit=True)
            login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')

            username = registration_form.cleaned_data.get('username')

            messages.success(request=request,
                             message=f'{username}, your account has been created! You are now able to log in.')

            return redirect(to='index')

    else:
        registration_form = RegistrationForm()

    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })


def log_in(request):
    login_form = RegistrationForm(data=request.POST)
    return render(request=request, template_name='users/login.html', context={
        'title': 'Login',
        'login_form': login_form
    })
