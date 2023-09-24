from django.shortcuts import render, redirect
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
from django.contrib import messages


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    if request.method == 'POST':
        category_form = CategoryForm(data=request.POST)

        if not Category.objects.filter(category=request.POST.get('category', None)).exists():
            if category_form.is_valid():
                category = category_form.save(commit=False)
                category.user = request.user
                category.save()

                messages.success(request=request, message='Your category has been added successfully.')

                redirect(to='lists')

            else:
                messages.error(request=request, message='Your category has not been added successfully.')

        else:
            messages.info(request=request, message=f"Category {request.POST.get('category', None)} already exists.")

    else:
        category_form = CategoryForm()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
        'category_form': category_form
    })


def add_category(request):
    pass


def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()

    return redirect(to='lists')
