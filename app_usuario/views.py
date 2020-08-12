from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MyUserSerializer, MyUser

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('-birtday')
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated]

