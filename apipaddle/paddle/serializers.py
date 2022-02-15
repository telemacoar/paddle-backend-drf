from rest_framework import serializers
from paddle.models import Product, Court, StockMovement, Client, Sale, Appointment, DateAppointment, TimeAppointment, SaleItem, ProductType


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price_buy',
                  'price_sale', 'iva', 'picture', 'stockeable']


class StockMovementSerializer(serializers.HyperlinkedModelSerializer):

    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = StockMovement
        fields = ['id', 'product_id', 'amount', 'date', 'price',
                  'income', 'product']


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'phone', 'cuit', 'phone', 'picture']


class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = SaleItem
        fields = ['id', 'product_id', 'amount', 'price', 'product']


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.ReadOnlyField(source='client.name')
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id',  'client_id', 'date',  'client', 'items']


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
