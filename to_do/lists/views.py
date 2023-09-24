from django.shortcuts import render
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

# @login_required
# def lists(request):
#     categories = Category.objects.filter(user=request.user)
#     tasks = Task.objects.all()
#
#     category = request.POST.get('category', None)
#     print(category)
#
#     if Category.objects.filter(category=category).exists():
#         messages.info(request=request, message='This category already exists.')
#     else:
#         Category.objects.create(user=request.user, category=category)
#
#         messages.success(request=request,
#                          message=f"Category {request.POST.get('category').title()} has been added successfully.")
#
#     return render(request=request, template_name='lists/lists.html', context={
#         'title': 'Lists',
#         'categories': categories,
#         'tasks': tasks
#     })
