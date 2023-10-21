from django.db.models import Q
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from api.modules.group.serializers import GroupSerializer
from group.models import Group
from user.models import User
import uuid

class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        groups = self.queryset.filter(participants__id=request.user.pk, archive=False, transmission=False)
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupOnlyListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        groups = self.queryset.filter(participants__id=request.user.pk, archive=False, transmission=False, isPrivate=False)
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupArchivedListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        groups = self.queryset.filter(participants__id=request.user.pk, archive=True, isPrivate=False)
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GroupTransmissionListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        groups = self.queryset.filter(participants__id=request.user.pk, isTransmission=True, archive=False)
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupCreateView(CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupUpdateView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class GroupRetrieveView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupUpdateAddParticipantView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        participants = self.request.data.getlist('participants', [])
        instance = serializer.instance
        participants_list = User.objects.filter(id__in=participants)
        instance.participants.add(*participants_list)
        instance.save()

class GroupUpdateRemoveParticipantView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        participants = self.request.data.getlist('participants', [])
        instance = serializer.instance
        participants_list = User.objects.filter(id__in=participants)
        for participant_id in participants_list:
            instance.participants.remove(participant_id)   
        instance.save()

