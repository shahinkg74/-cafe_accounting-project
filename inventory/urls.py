from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name ='list'),
    path('create/', views.inventory_create, name ='create'),
    path('update/<int:pk>', views.inventory_update, name ='update')
]