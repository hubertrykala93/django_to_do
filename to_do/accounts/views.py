import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, ResetPasswordForm, UserImageUpdateForm, \
    PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import User, Profile
from .tokens import token_generator
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator

load_dotenv()


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save(commit=True)

            send_mail(
                subject='Activate your account.',
                message=render_to_string(template_name='accounts/account_activate_email.html',
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
                             message=f"{registration_form.cleaned_data.get('username')}, "
                                     f"your account has been successfully created. "
                                     f"Now, please check your email and click on the activation link"
                                     f" to activate your account.")

            return redirect(to='index')

    else:
        registration_form = RegistrationForm()

    return render(request=request, template_name='accounts/register.html', context={
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

        if user is not None:
            if not user.is_verified:
                messages.info(request=request,
                              message=f"{request.POST.get('username')}, your account is not active. "
                                      f"Please visit your inbox and activate your account.")

                return redirect(to='login')
            else:
                login(request=request, user=user)

                messages.success(request=request,
                                 message=f"{request.POST.get('username')}, you have been successfully logged in.")

                return redirect(to='index')
        else:
            messages.info(request=request,
                          message=f"The user {request.POST.get('username')} does not exist, create an account.")

            return redirect(to='register')

    login_form = RegistrationForm()

    return render(request=request, template_name='accounts/login.html', context={
        'title': 'Login',
        'login_form': login_form
    })


def log_out(request):
    logout(request=request)
    messages.success(request=request, message='You have been successfully logged out.')

    return redirect(to='index')


@login_required
def account_settings(request):
    form_1 = UserUpdateForm(data=request.POST, instance=request.user, prefix='user-update')
    form_2 = PasswordChangeForm(user=request.user, data=request.POST, prefix='user-password-change')

    form_4 = ProfileUpdateForm(data=request.POST, files=request.FILES, prefix='profile-update',
                               instance=request.user.profile)

    if request.method == 'POST':
        if 'user-update' in request.POST:
            if form_1.is_valid():
                form_1.save()

                messages.success(request=request, message='Your account has been updated successfully.')

                return redirect(to='account-settings')

            else:
                messages.error(request=request, message='Your account has not been updated successfully.')

        elif 'user-password-change' in request.POST:
            if form_2.is_valid():
                form_2.save()

                update_session_auth_hash(request=request, user=request.user)

                messages.success(request=request, message='Your account has been updated successfully.')

                return redirect(to='account-settings')

            else:
                messages.error(request=request, message='Your account has not been updated successfully.')

        elif 'profile-update' in request.POST:
            if form_4.is_valid():
                print(form_4.is_valid())
                print(form_4.errors)
                form_4.save()

                messages.success(request=request, message='Your account has been updated successfully.')

                return redirect(to='account-settings')

            else:
                print(form_4.is_valid())
                print(form_4.errors)
                messages.error(request=request, message='Your account has not been updated successfully.')

    else:
        form_1 = UserUpdateForm(instance=request.user, prefix='user-update')
        form_2 = PasswordChangeForm(user=request.user, prefix='user-password-change')
        form_4 = ProfileUpdateForm(instance=request.user.profile, prefix='profile-update')

        print(form_4.is_valid())
        print(form_4.errors)

    # current_user_id = User.objects.get(id=request.user.id)

    return render(request=request, template_name='accounts/account-settings.html', context={
        'title': 'Account Settings',
        'form_1': form_1,
        'form_2': form_2,
        'form_4': form_4
    })


def reset_password(request):
    if request.method == 'POST':
        reset_form = ResetPasswordForm(data=request.POST)

        if reset_form.is_valid():
            email = reset_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=email))

            if user_email.exists():
                for user in user_email:
                    parameters = {
                        'email': user_email,
                        'domain': get_current_site(request=request),
                        'uid': urlsafe_base64_encode(s=force_bytes(s=user.pk)),
                        'token': default_token_generator.make_token(user=user),
                        'protocol': 'http'
                    }

                    html_message = render_to_string(
                        template_name='accounts/password_reset_email.html',
                        context=parameters
                    )

                    try:
                        messages.success(request=request,
                                         message=f"An email with password reset instructions has been sent "
                                                 f"to your email address {email}.")
                        messages.warning(request=request, message='Your activation link will expire after two days.')
                        send_mail(
                            subject='Reset your Password',
                            message=html_message,
                            from_email=os.environ.get('EMAIL_LOGIN'),
                            recipient_list=[email],
                            fail_silently=False
                        )
                    except ConnectionError:
                        HttpResponse('Invalid Header')

                    return redirect(to='index')

    else:
        reset_form = ResetPasswordForm()

    return render(request=request, template_name='accounts/reset-password.html', context={
        'title': 'Reset Password',
        'reset_form': reset_form
    })


def complete(request):
    messages.success(request=request,
                     message=f'Your password has been changed successfully. You can now to log in again.')

    return redirect(to='login')
