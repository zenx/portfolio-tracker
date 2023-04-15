# django imports
from django.urls import path, include

# project imports
from portfolio import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('add/', views.order_create, name='order_create'),
    path('orders/', views.order_list, name='order_list'),
]