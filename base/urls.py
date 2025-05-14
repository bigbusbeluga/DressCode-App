from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
    path('mixmatch/', views.mixmatch, name='mixmatch'),
    path('mixmatch/addClothing/', views.addClothing, name='add-Clothing'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)