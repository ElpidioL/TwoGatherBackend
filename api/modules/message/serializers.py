from group.models import Message
from user.serializers import PublicUserSerializer
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = Message
        fields = '__all__'