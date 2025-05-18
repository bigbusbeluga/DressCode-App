from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name="landing"),
    path('homepage/', views.homepage, name="homepage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('wardrobe/', views.wardrobe, name='wardrobe'),
    path('laundry/', views.laundry, name='laundry'),
    
    path('mixmatch/', views.mixmatch, name='mixmatch'),
    path('wardrobe/deleteClothing/<str:pk>/', views.deleteClothing, name='delete-Clothing'),
    path('addClothing/', views.addClothing, name='add-Clothing'),
    path('mixmatch/save-outfit/', views.saveOutfit, name='save-outfit'),
    path('wardrobe/edit-outfit-date/<int:pk>/', views.edit_outfit_date, name='edit-outfit-date'),

    path('edit-outfit-date/<int:pk>/', views.edit_outfit_date, name='edit_outfit_date'),
    path('edit-outfit-name/<int:pk>/', views.edit_outfit_name, name='edit_outfit_name'),

    path('clothing/<int:pk>/edit/', views.edit_clothing, name='edit_clothing'),
    path('clothing/<int:pk>/delete/', views.delete_clothing, name='delete_clothing'),
    path('clothing/<int:pk>/update/', views.update_clothing, name='update_clothing'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)