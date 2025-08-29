from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payment_list, name ='payment_list'),
    path('add/', views.create_payment, name ='create_payment'),
    path('<int:pk>:', views.payment_detail, name ='payment_detail'),
]