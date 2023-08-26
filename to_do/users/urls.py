from django.urls import path, reverse_lazy, reverse
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views
from .forms import PasswordChangeForm
from .models import User
from django.contrib import messages

urlpatterns = [
    path(route='register/', view=views.register, name='register'),
    path(route='login/', view=views.log_in, name='login'),
    path(route='logout/', view=views.log_out, name='logout'),
    path(route='profile/', view=views.profile, name='profile'),
    path(route='activate/<uidb64>/<token>', view=views.activate, name='activate'),
    path(route='change_password/', view=views.change_password, name='change-password'),
    path(route='reset_password/', view=views.reset_password, name='reset-password'),
    path(route='done/',
         view=auth_views.PasswordResetDoneView.as_view(template_name='users/done.html'),
         name='done'),
    path(route='confirm/<uidb64>/<token>/',
         view=auth_views.PasswordResetConfirmView.as_view(template_name='users/confirm.html',
                                                          extra_context={
                                                              'title': 'Confirm',
                                                              'password_change_form': PasswordChangeForm(user=User),
                                                          }, success_url=reverse_lazy('complete')),
         name='confirm'),
    path(route='complete/', view=views.complete, name='complete')
]
