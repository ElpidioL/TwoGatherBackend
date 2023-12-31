from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from api.modules.message.serializers import MessageSerializer, MessageReadBySerializer
from group.models import Message, Group
from user.models import User
import uuid
from rest_framework.response import Response
from rest_framework import status

class MessageListView(APIView):
    queryset = Message.objects.select_related('idGroup').all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user_groups = Group.objects.filter(participants__id=request.user.pk)

        idSentBy = request.data.get('idSentBy')
        idGroup =  request.data.get('idGroup')

        query = Q()
        if not idSentBy and not idGroup:
            raise Http404("Message not found")
        try:
            if idSentBy:
                query &= Q(idSentBy=uuid.UUID(idSentBy))
            if idGroup:
                query &= Q(idGroup=uuid.UUID(idGroup))
        except Exception as e:
            return HttpResponseBadRequest("UUID not valid")
        
        messages = self.queryset.filter(query, idGroup__in=user_groups)

        messagesNotSeen = messages.filter(~Q(readBy=request.user.pk))      

        for msg in messagesNotSeen:
            msg.readBy.add(request.user.pk)      


        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class MessageUpdateAddReadByView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageReadBySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        participants = self.request.data.get('readBy', [])
        instance = serializer.instance
        participants_list = User.objects.filter(id__in=participants)
        instance.readBy.add(*participants_list)
        instance.save()