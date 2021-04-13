from re import template

from django.http import response
from manager.forms import *
from manager.models import *
from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
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
    return render(request, 'customers.html', context)


def invoice(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'customerform': customerform, 'productform': productform}
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'invoice.html', context)


def preview_pdf_invoice(request):
    template_path = 'invoice_pdf.html'
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
    template_path = 'invoice_pdf.html'
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
