from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('mixmatch/', views.mixmatch_view, name='mixmatch')
]