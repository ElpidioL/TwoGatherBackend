from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class PublicUserSerializer(serializers.ModelSerializer):
    roleName = serializers.StringRelatedField(source='idRole.name')
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'photo', 'description', 'idRole', 'roleName','lastActive', 'status', 'pke']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

    def validate_email(self, value):
        norm_email = value.lower()
        if User.objects.filter(email=norm_email).exists():
            raise serializers.ValidationError("Not unique email")
        return norm_email
    
    def create(self, validated_data):
        norm_email = validated_data['email'].lower()
        if User.objects.filter(email=norm_email).exists():
            raise serializers.ValidationError("Not unique email")
        
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_active'] = True

        return super(UserSerializer, self).create(validated_data)