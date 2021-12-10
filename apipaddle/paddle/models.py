from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price_buy = models.DecimalField()
    price_sell = models.DecimalField()
    iva = models.DecimalField()
    picture = models.TextField()
    stockeable = models.BooleanField(default=False)


class StockMovement(models.Model):
    product = models.ForeignKey(Product)
    amount = models.DecimalField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField()
    income = models.BooleanField(default=True)


class Client(models.Model):
    name: models.CharField(max_length=100)
    cuit: models.CharField(max_length=100)
    phone: models.CharField(max_length=50)
    email: models.CharField(max_length=50)
    address: models.CharField(max_length=150)
    picture = models.TextField()


class Sell(models.Model):
    product = models.ForeignKey(Product)
    amount = models.DecimalField()
    price = models.DecimalField()
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)


class Court(models.Model):
    name: models.CharField(max_length=100)


class Appointment(models.Model):
    court: models.ForeignKey(Court)
    client: models.ForeignKey(Client)
    date: models.DateField()
    timefrom: models.TimeField()
    timeto: models.TimeField()


class TimeAppointment(models.Model):
    time: models.IntegerField()


class DateAppointment(models.Model):
    name: models.CharField(max_length=15)
