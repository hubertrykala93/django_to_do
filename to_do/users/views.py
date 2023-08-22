import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
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

load_dotenv()


def send_action_mail(request, user):
    current_site = get_current_site(request=request)
    subject = 'Activate your account.'
    email_body = render_to_string(
        template_name='users/account_activate_email.html',
        context={
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(s=force_bytes(s=user.pk)),
            'token': token_generator.make_token(user=user)
        }
    )

    send_mail(
        subject=subject,
        message=email_body,
        from_email=os.environ.get('EMAIL_LOGIN'),
        recipient_list=[user.email]
    )


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST or None)

        if registration_form.is_valid():
            user = registration_form.save(commit=True)

            send_action_mail(request=request, user=user)

            messages.success(request=request,
                             message=f"{registration_form.cleaned_data.get('username')}, your account has been successfully created.")

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


def activate(request, uidb64, token):
    try:
        uid = force_str(s=urlsafe_base64_decode(s=uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and token_generator.check_token(user=user, token=token):
        user.is_verified = True
        user.save()

        return redirect(to=reverse(viewname='login'))
