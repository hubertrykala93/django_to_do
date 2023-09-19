from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
    })
