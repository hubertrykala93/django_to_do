import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

load_dotenv()


def index(request):
    return render(request=request, template_name='core/index.html')


def support(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            messages.success(request=request,
                             message='Your email message has been sent successfully. '
                                     'We will respond as soon as possible.')

            html_message = render_to_string(template_name='core/support_mail.html', context={
                'full_name': contact_form.cleaned_data['full_name'],
                'email': contact_form.cleaned_data['email'],
                'message': contact_form.cleaned_data['message'],
            }, request=request)

            send_mail(
                subject=f"Message from To Do App.",
                message=contact_form.cleaned_data['message'],
                from_email=contact_form.cleaned_data['email'],
                recipient_list=[os.environ.get('EMAIL_HOST_USER')],
                fail_silently=True,
                html_message=html_message
            )

            return redirect(to='index')

    else:
        contact_form = ContactForm()

    return render(request=request, template_name='core/support.html', context={
        'title': 'Support',
        'contact_form': contact_form
    })
