from django.db.models import Q
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from api.modules.role.serializers import RoleSerializer
from user.models import Role
from api.perms import isAdmin
import uuid

class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class RoleCreateView(CreateAPIView):
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, isAdmin]

class RoleUpdateView(UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, isAdmin]

class RoleRetrieveView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        role = self.kwargs.get('role')
        if '-' in role:
            try:
                query = Q(pk=uuid.UUID(role))
            except:
                pass
        else:
            query = Q(name=role)
        try:
            role = self.queryset.get(query)
            return role
        except Exception as e:
            raise Http404("Role not found")