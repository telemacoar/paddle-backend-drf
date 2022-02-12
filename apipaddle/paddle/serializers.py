from rest_framework import serializers
from paddle.models import Product, Court, StockMovement, Client, Sell, Appointment, DateAppointment, TimeAppointment


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price_buy',
                  'price_sell', 'iva', 'picture', 'stockeable']


class StockMovementSerializer(serializers.HyperlinkedModelSerializer):

    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = StockMovement
        fields = ['id', 'product_id', 'amount', 'date', 'price',
                  'income', 'product', 'type']


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'phone', 'cuit', 'phone', 'picture']


class SellSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')
    client = serializers.ReadOnlyField(source='client.name')

    class Meta:
        model = Sell
        fields = ['id', 'product_id', 'client_id',
                  'amount', 'price', 'date', 'product', 'client']


class TimeAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeAppointment
        fields = ['id', 'time']


class DateAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateAppointment
        fields = ['id', 'name']


class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'court_id', 'client_id', 'timefrom', 'timeto', 'date']
