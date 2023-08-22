from django.urls import path
from . import views

urlpatterns = [
    path(route='register/', view=views.register, name='register'),
    path(route='login/', view=views.log_in, name='login'),
    path(route='logout/', view=views.log_out, name='logout'),
    path(route='profile/', view=views.profile, name='profile'),
    path(route='activate/<uidb64>/<token>', view=views.activate, name='activate')
]
