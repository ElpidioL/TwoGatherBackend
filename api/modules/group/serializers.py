from group.models import Group
from user.models import User
from api.modules.user.serializers import PublicUserSerializer
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    participants =  PublicUserSerializer(many=True)
    class Meta:
        model = Group
        fields = ('__all__')