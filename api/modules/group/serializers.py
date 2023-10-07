from group.models import Group
from user.models import User
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Group
        fields = ('__all__')