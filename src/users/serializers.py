
from rest_framework import serializers

from .models import *

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = ('id','role')

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = ExtendedUser
        fields = ('id','first_name','last_name','username','email','phone')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
            'role': {'required': True},
        }

