from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('cars/', views.car_list, name='car_list'),
    path('maintenances/', views.maintenance_list, name='maintenance_list'),
    path('cars/<int:pk>', views.car_detail, name='car_detail'),
    path('maintenances/<int:pk>', views.maintenance_detail, name='maintenance_detail'),
    path('cars/new', views.car_create, name='car_create'),
    path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete', views.car_delete, name='car_delete'),
    path('maintenances/new', views.maintenance_create, name='maintenance_create'),
    path('maintenances/<int:pk>/edit', views.maintenance_edit, name='maintenance_edit'),
    path('maintenances/<int:pk>/delete', views.maintenance_delete, name='maintenance_delete'),
]