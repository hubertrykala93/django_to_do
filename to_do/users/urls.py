from django.urls import path
from . import views

urlpatterns = [
    path(route='register/', view=views.register, name='register'),
    path(route='login/', view=views.log_in, name='login')
]
