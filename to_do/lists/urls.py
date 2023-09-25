from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists'),
    path(route='add-category/', view=views.add_category, name='add-category'),
    path(route='delete-category/<int:pk>', view=views.delete_category, name='delete-category')
]
