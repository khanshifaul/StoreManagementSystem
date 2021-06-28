from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='manager'),
    path('stock/', views.stock, name='stock'),
    path('customer/', views.customer, name='customer'),
    path('invoice/', views.invoice, name='invoice'),
]