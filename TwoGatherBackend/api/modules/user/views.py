from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import  Response

from api.perms import isAdmin
from api.modules.user.serializers import UserSerializer, PublicUserSerializer
from user.models import User
import uuid

#depois atualizar pra precisar ser admin
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User Created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#não deveria voltar toda as fields.
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = [IsAuthenticated]

#desativada
class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.request.user
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Add custom logic before updating the object, if needed
        # For example, perform some validation or log the update
        
        self.perform_update(serializer)
        
        # Add custom logic after updating the object, if needed
        # For example, send a custom response or perform additional actions
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
        #user = self.kwargs.get('user')
        #if '@' in user:
        #    query =Q(email=user)
        #elif '-' in user:
        #    try:
        #        query = Q(id=uuid.UUID(user))
        #    except:
        #        pass
        #else:
        #    raise Http404("User not found")

        #try:
        #    user = self.queryset.get(query)
        #    return user
        #except Exception as e:
        #    raise Http404("User not found")