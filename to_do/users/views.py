import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import User
from .tokens import token_generator
from django.db.models.query_utils import Q

load_dotenv()


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save(commit=True)

            send_mail(
                subject='Activate your account.',
                message=render_to_string(template_name='users/account_activate_email.html',
                                         context={
                                             'user': user,
                                             'domain': get_current_site(request=request),
                                             'uid': urlsafe_base64_encode(s=force_bytes(s=user.pk)),
                                             'token': token_generator.make_token(user=user)
                                         }),
                from_email=os.environ.get('EMAIL_LOGIN'),
                recipient_list=[user.email]
            )

            messages.success(request=request,
                             message=f"{registration_form.cleaned_data.get('username')}, your account has been successfully created. "
                                     f"Now, please check your email and click on the activation link to activate your account.")

            return redirect(to='login')

    else:
        registration_form = RegistrationForm()

    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })


def activate(request, uidb64, token):
    try:
        uid = force_str(s=urlsafe_base64_decode(s=uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and token_generator.check_token(user=user, token=token):
        messages.success(request=request, message='Your account has been activated. You can now log in.')
        user.is_verified = True
        user.save()

        return redirect(to=reverse(viewname='login'))


def log_in(request):
    if request.method == 'POST':
        user = authenticate(request=request, username=request.POST.get('username'),
                            password=request.POST.get('password1'))

        if not user.is_verified:
            messages.info(request=request,
                          message=f"{request.POST.get('username')}, your account is not active. Please check your email and activate your account.")

            return redirect('login')

        if not user:
            messages.info(request=request,
                          message=f"{request.POST.get('username')} doesn't exists. To log in, you need to register.")

            return redirect('register')
        else:
            login(request=request, user=user)

            messages.success(request=request,
                             message=f"{request.POST.get('username')}, you have been successfully logged in.")

            return redirect(to='index')

    else:
        login_form = RegistrationForm()

        return render(request=request, template_name='users/login.html', context={
            'title': 'Login',
            'login_form': login_form,
        })


def log_out(request):
    logout(request=request)
    messages.success(request=request, message='You have been successfully logged out.')

    return redirect(to='index')


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()

            messages.success(request=request, message='Your account has been updated!')

            return redirect(to='profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request=request, template_name='users/profile.html', context={
        'title': 'Profile',
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(user=request.user, data=request.POST)

        if password_change_form.is_valid():
            password_change_form.save()

            messages.success(request=request, message='Your password has been changed.')

            return redirect(to='login')
        else:
            for error in list(password_change_form.errors):
                messages.error(request=request, message=error)

    else:
        password_change_form = PasswordChangeForm(user=request.user)

        for error in list(password_change_form.errors):
            print(error)

    return render(request=request, template_name='users/change_password.html', context={
        'title': 'Reset Password',
        'password_change_form': password_change_form
    })
