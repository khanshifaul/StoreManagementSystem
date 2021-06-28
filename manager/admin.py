from django.contrib import admin
from manager.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Pharmaceutical)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
