from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    tasks_list = [
        [task.name for task in tasks if task.category.category == 'Cooking'],
        [task.name for task in tasks if task.category.category == 'Programming'],
        [task.name for task in tasks if task.category.category == 'Shopping'],
        [task.name for task in tasks if task.category.category == 'Travelling']
    ]

    context = {}

    for i, task in enumerate(tasks_list, start=1):
        paginator = Paginator(object_list=task, per_page=8)
        context[f'paginator_{i}'] = paginator

        if not 'page' in context.keys():
            page = request.GET.get('page')
            context['page'] = page
        else:
            continue

    context.update({
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks
    })

    return render(request=request, template_name='lists/lists.html', context=context)
