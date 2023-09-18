from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks_list = Task.objects.all()

    paginator = Paginator(object_list=tasks_list, per_page=8)
    page = request.GET.get('page')
    tasks = paginator.get_page(number=page)

    tasks.number

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks_list': tasks_list,
        'tasks': tasks
    })
