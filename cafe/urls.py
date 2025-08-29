from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include(('menu.urls', 'menu'), namespace='menu')),
    path('', include(('orders.urls', 'orders'), namespace='order')),
    path('', views.add_expense, name='add_expense'),
    path('', include(('inventory.urls', 'inventory'), namespace='inventory')),
    path('', include(('payments.urls', 'payments'), namespace='payments')),
    path('', include(('reports.urls', 'reports'), namespace='reports')),
]