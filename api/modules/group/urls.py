from django.urls import path

from api.modules.group.views import GroupListView, GroupCreateView, GroupUpdateView, GroupRetrieveView, GroupUpdateAddParticipantView, GroupUpdateRemoveParticipantView

urlpatterns = [
    path("<uuid:pk>", GroupRetrieveView.as_view(), name="group_info"),
    path("list/", GroupListView.as_view(), name="group_list"),
    path("create/", GroupCreateView.as_view(), name="group_create"),
    path("update/<uuid:pk>", GroupUpdateView.as_view(), name="group_update"),
    path("update/<uuid:pk>/participant/add", GroupUpdateAddParticipantView.as_view(), name="group_update_add_participant"),
    path("update/<uuid:pk>/participant/remove", GroupUpdateRemoveParticipantView.as_view(), name="group_update_remove_participant"),
]
