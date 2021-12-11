from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from paddle import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetailList.as_view()),
    path('courts/', views.CourtList.as_view()),
    path('courts/<int:pk>', views.CourtDetailList.as_view()),
]
