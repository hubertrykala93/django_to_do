from django.shortcuts import render, redirect
from .forms import CategoryForm, TaskForm
from django.contrib import messages


def lists(request):
    category_form = CategoryForm(data=request.POST, prefix='user-category', instance=request.user)
    task_form = TaskForm(data=request.POST, prefix='category-task', instance=request.user)

    if request.method == 'POST':
        if 'user-category' in request.POST:
            if category_form.is_valid():
                category_form.save()

                messages.success(request=request, message='The category has been added successfully.')

                return redirect(to='lists')

            else:
                messages.error(request=request, message='The category has not been added successfully.')

        elif 'category-task' in request.POST:
            if task_form.is_valid():
                task_form.save()

                messages.success(request=request, message='The task has been added successfully.')

                return redirect(to='lists')

            else:
                messages.error(request=request, message='The task has not been added successfully.')

    else:
        category_form = CategoryForm(prefix='user-category', instance=request.user)
        task_form = TaskForm(prefix='category-task', instance=request.user)

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'category_form': category_form,
        'task_form': task_form
    })
