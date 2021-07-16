from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product/<str:pk>/', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('customers/', views.customers, name='customers'),
    path('report/<str:pk>/', views.report, name='report'),
    path('reports/', views.reports, name='reports'),
    path('orderform/', views.orderform, name='orderform'),
    path('invoice/', views.invoice, name='invoice'),
    path('preview_pdf_invoice/', views.preview_pdf_invoice,
         name='preview_pdf_invoice'),
    path('download_pdf_invoice/', views.download_pdf_invoice,
         name='download_pdf_invoice'),
]
