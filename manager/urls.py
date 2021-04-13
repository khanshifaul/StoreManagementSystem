from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='manager'),
    path('stock/', views.stock, name='stock'),
    path('customer/', views.customer, name='customer'),
    path('invoice/', views.invoice, name='invoice'),
    path('preview_pdf_invoice/', views.preview_pdf_invoice, name='preview_pdf_invoice'),
    path('download_pdf_invoice/', views.download_pdf_invoice, name='download_pdf_invoice'),
]