from manager.forms import *
from django.shortcuts import render
from manager.models import *
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def stock(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'stock.html', context)


def customer(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer.html', context)


def invoice(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'customerform': customerform, 'productform': productform}
    return render(request, 'invoice.html', context)
