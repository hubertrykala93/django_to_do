from django.urls import path
from . import views

urlpatterns = [
    path(route='login/', view=views.login, name='login'),
    path(route='register/', view=views.register, name='register')
]
