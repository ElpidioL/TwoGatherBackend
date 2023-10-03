from django.urls import path

from api.modules.user.views import UserListView, UserCreateView, UserUpdateView, UserRetrieveView

urlpatterns = [
    path("<str:user>", UserRetrieveView.as_view(), name="user_info"),
    path("list/", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/<uuid:pk>", UserUpdateView.as_view(), name="user_update"),
]
