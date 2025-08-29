from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='list'),
    path('create/', views.create_order, name='create'),
    path('print/<int:order_id>', views.print_order, name='print_order'),
]
