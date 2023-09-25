from django.urls import path
from . import views

urlpatterns = [
    path(route='lists/', view=views.lists, name='lists'),
    path(route='update-category/', view=views.update_category, name='update-category'),
    path(route='delete-category/<int:pk>', view=views.delete_category, name='delete-category')
]
