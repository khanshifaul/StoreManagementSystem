from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from manager.forms import *
from manager.models import *

from xhtml2pdf import pisa
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'products': products,
               'customers': customers, 'reports': reports,
               'customerform': customerform, 'productform': productform}
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'md_dashboard.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'product': product,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_product.html', context)


def products(request):
    products = Product.objects.all()
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'products': products,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_products.html', context)


def customer(request, pk):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_customer.html', context)


def customers(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    customers = Customer.objects.all()
    context = {'customers': customers,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_customers.html', context)


def report(request, pk):
    report = Product.objects.get(id=pk)
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'report': report,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_report.html', context)


def reports(request):
    reports = Invoice.objects.all()
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'reports': reports,
               'customerform': customerform, 'productform': productform}
    return render(request, 'md_reports.html', context)


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


def orderform(request):
    customerform = CustomerForm(request.POST)
    productform = ProductForm(request.POST)
    context = {'customerform': customerform, 'productform': productform}
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'md_orderform.html', context)
