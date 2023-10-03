from django.db.models import Q
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from api.modules.user.serializers import UserSerializer
from user.models import User
import uuid


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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