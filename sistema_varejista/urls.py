"""sistema_varejista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_usuario import views
from app_produtos.views import ProductViewSet
from app_core.views import *

router = routers.DefaultRouter()
router.register(r'^users', views.MyUserViewSet)
router.register(r'^products', ProductViewSet)

urlpatterns = [
    path('calculador/<int:nr_product>/<int:nr_usuer>', calculador, name='calculador'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
admin.site.site_header = 'Administrativo Varejista'
