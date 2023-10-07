from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("user/", include('api.modules.user.urls')),
    path("role/", include('api.modules.role.urls')),
    path("group/", include('api.modules.group.urls')),
    path("message/", include('api.modules.message.urls')),

    #token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]