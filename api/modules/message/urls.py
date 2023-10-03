from django.urls import path

from api.modules.message.views import MessageListView, MessageCreateView, MessageUpdateView, MessageUpdateAddReadByView

urlpatterns = [
    path("list/", MessageListView.as_view(), name="message_list"),
    path("create/", MessageCreateView.as_view(), name="message_create"),
    path("update/<uuid:pk>", MessageUpdateView.as_view(), name="message_update"),
    path("update/<uuid:pk>/readBy/add", MessageUpdateAddReadByView.as_view(), name="message_update_add_read_by"),
]
