from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from .forms import PasswordChangeForm
from .models import User

urlpatterns = [
    path(route='register/', view=views.register, name='register'),
    path(route='login/', view=views.log_in, name='login'),
    path(route='logout/', view=views.log_out, name='logout'),
    path(route='account-settings/', view=views.account_settings, name='account-settings'),
    path(route='activate/<uidb64>/<token>', view=views.activate, name='activate'),
    path(route='reset-password/', view=views.reset_password, name='reset-password'),
    path(route='confirm/<uidb64>/<token>/',
         view=auth_views.PasswordResetConfirmView.as_view(template_name='accounts/confirm.html',
                                                          extra_context={
                                                              'title': 'Confirm',
                                                              'password_change_form': PasswordChangeForm(user=User),
                                                          }, success_url=reverse_lazy('complete')),
         name='confirm'),
    path(route='complete/', view=views.complete, name='complete'),
]
