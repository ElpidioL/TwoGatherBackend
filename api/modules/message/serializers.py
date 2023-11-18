from group.models import Message
from user.models import User
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='idSentBy.name')
    readByAll = serializers.SerializerMethodField(read_only=True)
    readBy = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    date =  serializers.DateTimeField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_queryset(self):
        return Message.objects.select_related('idGroup')
    
    def get_readByAll(self, obj):
        return obj.readBy.count() == obj.idGroup.participants.count()
    
    def get_date(self, obj):
        return obj.date