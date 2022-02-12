from django.shortcuts import render
from paddle.models import Product, Court, Client, StockMovement, Sell
from paddle.serializers import ProductSerializer, CourtSerializer, ClientSerializer, StockMovementSerializer, SellSerializer
from rest_framework import generics


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CourtList(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class StockMovementList(generics.ListCreateAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class StockMovementDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class SellList(generics.ListCreateAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer


class SellDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
