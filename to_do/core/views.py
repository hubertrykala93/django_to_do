from django.shortcuts import render


def index(request):
    return render(request=request, template_name='core/base.html', context={
        'title': 'Homepage'
    })
