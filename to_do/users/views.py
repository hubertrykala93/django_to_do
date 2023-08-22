import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import activation_token
from .models import User

load_dotenv()


def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST or None)

        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.is_active = False
            user.save()

            messages.success(request=request,
                             message=f"{registration_form.cleaned_data.get('username')}, your account has been successfully created. "
                                     f"Now, please check your email and click on the activation link to activate your account.")

            html_message = render_to_string(template_name='users/user_activation_mail.html', context={
                'username': registration_form.cleaned_data.get('username').title(),
                'domain': get_current_site(request=request).domain,
                'uid': urlsafe_base64_encode(s=force_bytes(s=user.pk)),
                'token': activation_token(user)
            }, request=request)

            send_mail(subject='To Do App Registration.',
                      message='',
                      from_email=os.environ.get('EMAIL_LOGIN'),
                      recipient_list=[registration_form.cleaned_data.get('email')], fail_silently=True,
                      html_message=html_message)

            return redirect(to='login')

    else:
        registration_form = RegistrationForm()

    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!',
        'registration_form': registration_form
    })


def activate(request, uidb64, token):
    user = get_user_model()

    try:
        uid = force_str(s=urlsafe_base64_decode(s=uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and activation_token.check_token(user=user, token=token):
        user.is_active = True
        user.save()

        return HttpResponse(content='Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse(content='Activation link is invalid.')


def log_in(request):
    if request.method == 'POST':
        user = authenticate(request=request, username=request.POST.get('username'),
                            password=request.POST.get('password1'))

        if user:
            login(request=request, user=user)

            messages.success(request=request,
                             message=f"{request.POST.get('username')}, you have been successfully logged in.")

            return redirect(to='index')
        else:
            username = request.POST.get('username')
            messages.info(request=request, message=f"{username} doesn't exists. To log in, you need to register.")
            return redirect('login')

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
