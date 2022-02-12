from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from paddle import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='productos_list'),
    path('products/<int:pk>', views.ProductDetailList.as_view(),
         name='productos_detail'),
    path('courts/', views.CourtList.as_view(), name='canchas_list'),
    path('courts/<int:pk>', views.CourtDetailList.as_view(), name='canchas_detail'),
    path('clients/', views.ClientList.as_view(), name='clientes_list'),
    path('clients/<int:pk>', views.ClientDetailList.as_view(),
         name='clientes_detail'),
    path('stocks/', views.StockMovementList.as_view()),
    path('stocks/<int:pk>', views.StockMovementDetailList.as_view()),
    path('sales/', views.SellList.as_view()),
    path('sales/<int:pk>', views.SellDetailList.as_view()),

]
