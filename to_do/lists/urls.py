from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists'),
    path(route='add-category', view=views.add_category, name='add-category'),
    path(route='add-task', view=views.add_task, name='add-task')
]
