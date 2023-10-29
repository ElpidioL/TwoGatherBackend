from group.models import Message
from user.serializers import PublicUserSerializer
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    user_name = PublicUserSerializer(source='user', read_only=True, fields=('name',))
    class Meta:
        model = Message
        fields = '__all__'