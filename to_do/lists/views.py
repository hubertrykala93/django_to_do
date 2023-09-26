from django.shortcuts import render, redirect
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


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
            messages.info(request=request, message=f'Category {category_name} already exists.')
        else:
            new_category.save()

            messages.success(request=request, message=f'Category {category_name} has been created successfully.')

        return HttpResponse(content='')


def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()

    return redirect(to='lists')
