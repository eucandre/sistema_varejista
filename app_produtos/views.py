from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer, Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-expiration_date')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


