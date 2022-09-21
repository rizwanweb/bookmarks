from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Function Based Login View
    #path('login', views.user_login, name='login'),

    # A short way for all the urls but i dont like it.
    path("", include('django.contrib.auth.urls')),

    # login and logout urls
    # path('login', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # # Change Password Urls
    # path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # reset Password urls
    # path("password_reset", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("reset/done", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # User Registration URLs
    path("register", views.register, name="register"),



    path('', views.dashboard, name='dashboard'),
]
