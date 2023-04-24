
from rest_framework import serializers

from .models import *

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = ('id','role')

class UserSerializer(serializers.ModelSerializer):
    #role = RoleSerializer()
    class Meta:
        model = ExtendedUser
        fields = ('id','first_name','last_name','username','email','phone','is_staff','is_active','groups','password')
        #fields = '__all__'
        # extra_kwargs = {
        #     'username': {'required': True},
        #     'email': {'required': True},
        #     'phone': {'required': True},
        #     'role': {'required': True},
        # }
   
# from djoser.serializers import UserCreateSerializer

# class MyUserCreateSerializer(UserCreateSerializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)

#     class Meta(UserCreateSerializer.Meta):
#         fields = ('email', 'username', 'password', 'first_name', 'last_name')