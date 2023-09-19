from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    paginator = Paginator(object_list=tasks, per_page=8)
    page = paginator.page(number=2)

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
        'page': page
    })
