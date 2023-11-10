from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password

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

class UserListView(ListAPIView):
    queryset = User.objects.filter(status=1)
    serializer_class = PublicUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = self.queryset.filter(~Q(id=request.user.pk))
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateView(UpdateAPIView): #self update do user, apesar que pelas telas, não vamos usar.
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.request.user
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateAdminView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, isAdmin]

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.kwargs.get('user')
        if '@' in user:
            query =Q(email=user)
        elif '-' in user:
            try:
                query = Q(id=uuid.UUID(user))
            except:
                pass
        else:
            raise Http404("User not found")

        try:
            user = self.queryset.get(query)
            return user
        except Exception as e:
            raise Http404("User not found")
        
class UserUpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            instance = self.request.user
            old_password = self.request.data.get('old_password')
            new_password = self.request.data.get('password')

            if old_password and new_password and check_password(old_password, instance.password):
                instance.set_password(new_password) 
                instance.save()
                return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid old password or new password not provided."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"detail": "An error occurred while processing your request."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)