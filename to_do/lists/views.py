from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, CategoryForm
from django.contrib import messages
from django.http import JsonResponse


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    if request.method == 'POST':
        category_form = CategoryForm(data=request.POST)

        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.user = request.user
            category.save()

            messages.success(request=request, message='Your category has been added successfully.')

        else:
            messages.error(request=request, message='Your category has not been added successfully')

    else:
        category_form = CategoryForm()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
        'category_form': category_form
    })
