import uuid
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, validators=())
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Pharmaceutical(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    generic_name = models.CharField(max_length=200, null=True)
    pharmaceutical_name = models.ForeignKey(
        Pharmaceutical, on_delete=SET_NULL, null=True)
    product_type_choices = [
        ('TABLET', 'Tablet'),
        ('SYRUP', 'Syrup'),
        ('Oral Suspension', 'Oral Suspension'),
        ('IV Infusion', 'IV Infusion'),
        ('Capsule', 'Capsule'),
        ('Injection', 'Injection'),
        ('Powder for Suspension', 'Powder for Suspension'),
        ('Oral Gel', 'Oral Gel')
    ]
    product_type = models.TextField(choices=product_type_choices, null=True)
    price = models.FloatField()
    instock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_code = models.UUIDField(default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    valid = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    status_choices = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('DRAFT', 'Draft'),
    ]
    status = models.TextField(choices=status_choices, null=False)

    def __str__(self):
        return str(self.id)

    def total_items(self):
        total = 0
        items = self.invoiceitem_set.all()

        for item in items:
            total += item.cost * item.qty

        return total

    def total(self):
        items = self.total_items()
        return items

    def paid(self):
        return self.status == 'Paid'

    def unpaid(self):
        return self.status == 'Unpaid'

    def draft(self):
        return self.status == 'Draft'


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=CASCADE, null=True)
    cost = models.FloatField()
    qty = models.IntegerField(default=1, null=False)

    def __str__(self):
        return str(self.id) + '. ' + str(self.product)

    def total(self):
        return self.cost * self.qty
