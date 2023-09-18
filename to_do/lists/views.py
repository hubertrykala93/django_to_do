from django.shortcuts import render, redirect
from .forms import CategoryForm, TaskForm
from django.contrib import messages
from .models import Category, Task
from django.contrib.auth.decorators import login_required


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks
    })
