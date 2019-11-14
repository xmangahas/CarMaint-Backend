from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.CarList.as_view(), name='car_list'),
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('maintenances/', views.MaintenanceList.as_view(), name='maintenance_list'),
    path('maintenances/<int:pk>', views.MaintenanceDetail.as_view(), name='maintenance_detail'),
]