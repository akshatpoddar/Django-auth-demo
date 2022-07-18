from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signUp_user, name='signup'),
    path('signin', views.signIn_user, name='signin'),
    path('logout', views.logout_user, name='logout'),
]
