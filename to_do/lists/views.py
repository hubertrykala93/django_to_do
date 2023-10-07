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

        if len(category_name.strip()) == 0:
            return JsonResponse(data={
                "valid": False,
                "message": "The category cannot be empty.",
            })

        else:
            if Category.objects.filter(user=request.user, category=category_name.strip()).exists():
                return JsonResponse(data={
                    "valid": False,
                    "message": f"Category '{category_name.strip()}' already exists.",
                })

            else:
                new_category = Category(user=request.user, category=category_name.strip())
                new_category.save()

                return JsonResponse(data={
                    "valid": True,
                    "message": f"Category '{new_category.category}' has been created successfully.",
                    "category_id": new_category.pk,
                    "category_name": new_category.category,
                })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The addition of a new category was unsuccessful.",
        })


@csrf_exempt
def edit_category(request):
    if request.method == 'POST':
        id = request.POST.get('categoryId', None)
        name = request.POST.get('name', None)

        if len(name.strip()) == 0:
            return JsonResponse(data={
                "valid": False,
                "message": "The category cannot be empty.",
            })

        else:
            if Category.objects.filter(user=request.user, category=name.strip()).exists():
                return JsonResponse(data={
                    'valid': False,
                    'message': f"The category named '{name.title().strip()}' already exists.",
                })

            else:
                category = Category.objects.get(id=id)
                category.category = name.strip()
                category.save()

                return JsonResponse(data={
                    "valid": True,
                    "message": f"The category name has been successfully changed to {name.title().strip()}.",
                })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The editing was not successful."
        })


@csrf_exempt
def delete_category(request):
    if request.method == 'POST':
        id = request.POST.get('categoryId', None)

        category = Category.objects.get(user=request.user, pk=id)
        category.delete()

        return JsonResponse(data={
            "valid": True,
            "message": f"The '{category.category}' category has been successfully deleted.",
        })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The deletion was unsuccessful.",
        })


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        category_id = request.POST.get('categoryId')
        category_name = Category.objects.get(id=category_id)
        task_name = request.POST.get('name')
        task_description = request.POST.get('description')

        if len(task_name.strip()) == 0:
            return JsonResponse(data={
                "valid": False,
                "message": "The task cannot be empty.",
            })

        else:
            if Task.objects.filter(name=task_name.strip()).exists():
                return JsonResponse(data={
                    "valid": False,
                    "message": f"Task '{task_name.strip()}' already exists.",
                })

            else:
                new_task = Task(category_id=category_id, name=task_name.strip(), description=task_description.strip())
                new_task.save()

                return JsonResponse(data={
                    "valid": True,
                    "message": f"The task has been successfully assigned to the {category_name.category} category.",
                    "new_task_id": new_task.pk,
                    "new_task_created_at": new_task.created_at,
                    "new_task_name": new_task.name,
                    "new_task_description": new_task.description,
                })

    else:
        return JsonResponse(
            data={
                "valid": False,
                "message": "The addition of a new task was unsuccessful.",
            }
        )


@csrf_exempt
def edit_task(request):
    if request.method == 'POST':
        category_id = request.POST.get('categoryId')
        id = request.POST.get('taskId')
        name = request.POST.get('taskName')
        description = request.POST.get('taskDescription')

        if len(name) == 0:
            return JsonResponse(data={
                "valid": False,
                "message": "The task name cannot be empty.",
            })

        elif len(description) == 0:
            return JsonResponse(data={
                "valid": False,
                "message": "The task description cannot be empty.",
            })

        else:
            if Task.objects.filter(category_id=category_id, id=id, name=name).exists():
                return JsonResponse(data={
                    "valid": False,
                    "message": f"The task named '{name.strip()}' already exists.",
                })

            else:
                new_task = Task.objects.get(id=id)
                new_task.name = name
                new_task.description = description
                new_task.save()

                return JsonResponse(data={
                    "valid": True,
                    "message": f"The task name has been successfully changed to {name.strip()}.",
                    "new_task_name": new_task.name,
                    "new_task_description": new_task.description,
                })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The editing was not successful.",
        })


@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        id = request.POST.get('taskId')

        task = Task.objects.get(id=id)
        task.delete()

        return JsonResponse(data={
            "valid": True,
            "message": f"The '{task.name}' has been successfully deleted.",
        })

    else:
        return JsonResponse(data={
            "valid": False,
            "message": "The deletion was unsuccessful.",
        })
