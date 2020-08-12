from django.http import JsonResponse
from django.shortcuts import render
from app_usuario.serializers import *
from app_produtos.serializers import *
from app_produtos.models import *
from app_usuario.models import *
from datetime import date

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-expiration_date')
    serializer_class = ProductSerializer
