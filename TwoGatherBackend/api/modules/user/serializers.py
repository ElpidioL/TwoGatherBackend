from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'photo', 'description', 'idRole', 'lastActive']
    

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

        #remove this on deploy.
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = True
        validated_data['is_active'] = True

        return super(UserSerializer, self).create(validated_data)
    