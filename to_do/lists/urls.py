from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists')
]