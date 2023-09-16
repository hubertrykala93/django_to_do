from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, TaskForm
from django.contrib import messages
from .models import Category, Task
from django.contrib.auth.decorators import login_required


@login_required
def lists(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        category_form = CategoryForm(data=request.POST, instance=request.user)

        if category_form.is_valid():
            category_form.save()

            messages.success(request=request, message='The category has been added successfully.')

            return redirect(to='lists')

        else:
            messages.error(request=request, message='The category has not been added successfully.')

    # if request.method == 'POST':
    #     if 'user-category' in request.POST:
    #         if category_form.is_valid():
    #             category_form.save()
    #             print(category_form.errors)
    #
    #             messages.success(request=request, message='The category has been added successfully.')
    #
    #             return redirect(to='lists')
    #
    #         else:
    #             print(category_form.errors)
    #             messages.error(request=request, message='The category has not been added successfully.')

    else:
        category_form = CategoryForm()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'category_form': category_form,
        'categories': categories
    })
