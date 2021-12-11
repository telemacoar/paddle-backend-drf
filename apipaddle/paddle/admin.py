from django.contrib import admin
from .models import Product, Court, TimeAppointment, DateAppointment, Appointment, Client, StockMovement

admin.site.register(Product)
admin.site.register(Court)
admin.site.register(TimeAppointment)
admin.site.register(DateAppointment)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(StockMovement)
