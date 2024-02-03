
from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('',views.index,name="index"),
    path('logout/',views.logout_page,name="logout"),
    path('password_change/',auth_view.PasswordChangeView.as_view(),name="password_change"),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('password_reset',auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
    path('password_reset/done',auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path('reset/<str:uidb64>/<str:token>',auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name='password_reset_confirm'),
] 
