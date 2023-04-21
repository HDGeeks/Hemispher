
from rest_framework import serializers

from .models import *

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = ('id','role')

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    class Meta:
        model = ExtendedUser
        #fields = ('id','first_name','last_name','username','email','phone','role')
        fields = '__all__'
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
            'role': {'required': True},
        }
    def create(self, validated_data):
        role_data = validated_data.pop('role')
        role, _ = Role.objects.get_or_create(**role_data)
        user = ExtendedUser.objects.create_user(role=role, **validated_data)
        return user
