from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists'),
    path(route='task-details/<int:pk>/', view=views.task_details, name='task-details')
]
