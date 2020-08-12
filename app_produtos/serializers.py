from rest_framework import serializers, viewsets
from app_produtos.models import Product
from datetime import date

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title','description','manufacturer','price','unity','expiration_date']



class Calculador(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['price',]