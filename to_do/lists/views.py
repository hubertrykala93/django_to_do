from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def lists(request):
    categories = Category.objects.filter(user=request.user)
    tasks = Task.objects.all()

    return render(request=request, template_name='lists/lists.html', context={
        'title': 'Lists',
        'categories': categories,
        'tasks': tasks,
    })


@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category', None)

        if Category.objects.filter(category=category_name).exists():
            return JsonResponse(data={
                "valid": False,
                "message": f"Category '{category_name}' already exists."
            })

        else:
            new_category = Category(user=request.user, category=category_name)
            new_category.save()

            return JsonResponse(data={
                "valid": True,
                "message": f"Category '{category_name}' has been created successfully."
            })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The addition of a new category was unsuccessful."
        })


@csrf_exempt
def delete_category(request):
    if request.method == 'POST':
        id = request.POST.get('data-cid')

        category = Category.objects.get(pk=id)
        category.delete()

        return JsonResponse(data={
            "valid": True,
            "message": f"The '{category.category}' category has been successfully deleted."
        })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The deletion was unsuccessful."
        })
