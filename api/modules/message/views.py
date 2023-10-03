from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from api.modules.message.serializers import MessageSerializer
from group.models import Message
from user.models import User
import uuid
from rest_framework.response import Response
from rest_framework import status

class MessageListView(APIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        messages = self.queryset.all()
        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        idSentBy = self.request.POST.get('idSentBy')
        idGroup =  self.request.POST.get('idGroup')

        query = Q()
        if not idSentBy and not idGroup:
            raise Http404("Message not found")
        try:
            if idSentBy:
                query &= Q(idSentBy=uuid.UUID(idSentBy))
            if idGroup:
                query &= Q(idGroup=uuid.UUID(idGroup))
        except Exception as e:
            raise HttpResponseBadRequest("UUID not valid")

        messages = self.queryset.filter(query)
        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer

class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'

class MessageUpdateAddReadByView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_update(self, serializer):
        participants = self.request.data.getlist('readBy', [])
        instance = serializer.instance
        participants_list = User.objects.filter(id__in=participants)
        instance.readBy.add(*participants_list)
        instance.save()