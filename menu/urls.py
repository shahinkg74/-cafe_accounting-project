from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name ='category_list'),
    path('categories/create/', views.category_create, name ='category_create'),
    path('menu/items/', views.menuitem_list, name ='menuitem_list'),
    path('items/create/', views.menuitem_create, name ='menuitem_create'),
]
