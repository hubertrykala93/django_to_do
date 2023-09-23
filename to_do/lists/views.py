from django.shortcuts import render, redirect
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.contrib import messages


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    if request.method == 'POST':
        task_form = TaskForm(data=request.POST, prefix='user-task')

        if task_form.is_valid():
            task_form.save()

            messages.success(request=request, message='Your task has been added successfully.')

            return redirect(to='lists')

        else:
            messages.error(request=request, message='Your task has not been added successfully.')

    else:
        task_form = TaskForm(prefix='user-task')

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
        'task_form': task_form
    })
