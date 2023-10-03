from django.db.models import Q
from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from api.modules.role.serializers import RoleSerializer
from user.models import Role
import uuid

class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleCreateView(CreateAPIView):
    serializer_class = RoleSerializer

class RoleUpdateView(UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'

class RoleRetrieveView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

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