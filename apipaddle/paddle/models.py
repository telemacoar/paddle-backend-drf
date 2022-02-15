from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, default=True)
    price_buy = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_sale = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    iva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    picture = models.TextField(blank=True, default=True)
    stockeable = models.BooleanField(default=False)
    type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    income = models.BooleanField(default=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    cuit = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    picture = models.TextField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class SaleItem(models.Model):
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Court(models.Model):
    name = models.CharField(max_length=100)


class Appointment(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    timefrom = models.TimeField()
    timeto = models.TimeField()


class TimeAppointment(models.Model):
    time = models.IntegerField()


class DateAppointment(models.Model):
    name = models.CharField(max_length=15)
