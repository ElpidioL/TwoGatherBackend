from django.urls import path

from api.modules.user.views import UserListView, UserUpdateView, UserRetrieveView, RegisterView, UserUpdateAdminView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("<str:user>", UserRetrieveView.as_view(), name="user_info"),
    path("list/", UserListView.as_view(), name="user_list"),
    #path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/", UserUpdateView.as_view(), name="user_update"),
    path("update/<uuid:pk>/admin/", UserUpdateAdminView.as_view(), name="user_update_admin"),

]
