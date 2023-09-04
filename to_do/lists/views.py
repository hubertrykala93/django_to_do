from django.shortcuts import render


def lists(request):
    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists'
    })
