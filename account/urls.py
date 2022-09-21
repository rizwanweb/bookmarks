from django.urls import path
from . import views

urlpatterns = [
    # Post Views
    path('login', views.user_login, name='login'),
]
