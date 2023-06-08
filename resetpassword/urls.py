

from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
  

    path('', PasswordResetView.as_view(template_name='reset_pass/reset_pass.html'), name='password_reset'),
    
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='reset_pass/reset_pass_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_pass/reset_confirm.html'), name='password_reset_confirm'),
    
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='reset_pass/reset_pass_complete.html'), name='password_reset_complete'),
]
