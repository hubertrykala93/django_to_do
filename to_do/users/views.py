from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST or None)

        if registration_form.is_valid():
            registration_form.save()

            messages.success(request=request,
                             message=f"{registration_form.cleaned_data.get('username')}, "
                                     f"your account has been created! You are now able to log in.")

            return redirect(to='login')

    else:
        registration_form = RegistrationForm()

    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })


def log_in(request):
    if request.method == 'POST':
        user = authenticate(request=request, username=request.POST.get('username'),
                            password=request.POST.get('password1'))

        if user is not None:
            login(request=request, user=user)

            messages.success(request=request,
                             message=f"{request.POST.get('username')}, you have been successfully logged in.")

        return redirect(to='index')

    else:
        login_form = RegistrationForm()

    return render(request=request, template_name='users/login.html', context={
        'title': 'Login',
        'login_form': login_form
    })


def log_out(request):
    logout(request=request)
    return redirect(to='index')
