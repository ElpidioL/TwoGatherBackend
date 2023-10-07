from django.urls import path

from api.modules.role.views import RoleListView, RoleCreateView, RoleUpdateView, RoleRetrieveView

urlpatterns = [
    path("<str:role>", RoleRetrieveView.as_view(), name="role_info"),
    path("list/", RoleListView.as_view(), name="role_list"),
    path("create/", RoleCreateView.as_view(), name="role_create"),
    path("update/<uuid:pk>", RoleUpdateView.as_view(), name="role_update"),
]
