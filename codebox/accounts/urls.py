from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('dashboard/',user_views.dashboard,name='dashboard'),


    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html') ,name='password_change_done'),


    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    path('password-reset-sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]
