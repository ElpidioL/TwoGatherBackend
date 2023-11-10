from group.models import Group
from user.models import User
from api.modules.user.serializers import PublicUserSerializer
from api.modules.message.serializers import MessageSerializer
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, write_only=True)
    members = PublicUserSerializer(many=True, source="participants", read_only=True)
    messages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = ('__all__')

    def get_messages(self, obj):
        messages = obj.message_set.last()
        serializer = MessageSerializer(messages)
        return serializer.data