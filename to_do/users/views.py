from django.shortcuts import render


def login(request):
    return render(request=request, template_name='users/login.html', context={
        'title': 'Log In'
    })


def register(request):
    return render(request=request, template_name='users/register.html', context={
        'title': 'Sign Up for Free!'
    })
