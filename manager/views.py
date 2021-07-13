from re import template

from django.http import response
from django.shortcuts import render, HttpResponse
from django.template.loader import get_template

from manager.forms import *
from manager.models import *

from xhtml2pdf import pisa
# Create your views here.


def dashboard(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    reports = Invoice.objects.all()
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'products': products,
               'customers': customers, 'reports': reports,
               'customerform': customerform, 'productform': productform}
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'md_dashboard.html', context)


def stock(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'md_stock.html', context)


def customer(request, pk):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_customer.html', context)


def invoice(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'customerform': customerform, 'productform': productform}
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'md_invoice.html', context)


def preview_pdf_invoice(request):
    template_path = 'md_invoice_pdf.html'
    invoice_id = Invoice.objects.get(pk=1)
    date = invoice_id.date_created
    customer = Customer.objects.get(pk='01701005355')
    customer_phone = customer.phone
    customer_address = customer.address
    items = InvoiceItem.objects.all()
    intotal = invoice_id.total
    context = {'invoice_id': invoice_id, 'date': date, 'customer': customer,
               'customer_phone': customer_phone, 'customer_address': customer_address,
               'items': items, 'intotal': intotal}
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def download_pdf_invoice(request):
    template_path = 'md_invoice_pdf.html'
    invoice_id = Invoice.objects.get(pk=1)
    date = invoice_id.date_created
    customer = Customer.objects.get(pk='01701005355')
    customer_phone = customer.phone
    customer_address = customer.address
    items = InvoiceItem.objects.all()
    intotal = invoice_id.total
    context = {'invoice_id': invoice_id, 'date': date, 'customer': customer,
               'customer_phone': customer_phone, 'customer_address': customer_address,
               'items': items, 'intotal': intotal}
    response = HttpResponse(content_type='application/pdf')
    filename = 'invoice_' + str(invoice_id) + '.pdf'
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
