from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
    })


def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category', None)

        new_category = Category(user=request.user, category=category_name)

        if Category.objects.filter(category=category_name).exists():
            return JsonResponse(data={
                'valid': False,
                'message': f'Category {category_name} already exists.'
            })
        else:
            new_category.save()

            return JsonResponse(data={
                'valid': True,
                'message': f'Category {category_name} has been created successfully.'
            })


def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task-name', None)
        task_description = request.POST.get('task-description', None)

        return HttpResponse(content='')

        # new_task = Task(name=task_name, description=task_description)
        #
        # if Task.objects.filter(name=task_name).exists():
        #     return JsonResponse(data={
        #         'valid': False,
        #         'message': f"Task '{task_name}' already exists."
        #     })
        # else:
        #     new_task.save()
        #
        #     return JsonResponse(data={
        #         'valid': True,
        #         'message': f"Task '{task_name} for category has been created successfully."
        #     })
