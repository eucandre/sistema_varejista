from rest_framework import serializers
from app_usuario.models import MyUser

class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name','last_name','birtday','city']