from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists'),
    path(route='add-category', view=views.add_category, name='add-category'),
    path(route='edit-category', view=views.edit_category, name='edit-category'),
    path(route='delete-category', view=views.delete_category, name='delete-category'),
    path(route='add-task', view=views.add_task, name='add-task'),
    path(route='edit-task', view=views.edit_task, name='edit-task'),
    path(route='delete-task', view=views.delete_task, name='delete-task'),
]
