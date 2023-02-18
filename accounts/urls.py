from django.urls import path

# Views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegisterUserAPIView

app_name = 'accounts'
urlpatterns = [
    path("api/register/", RegisterUserAPIView.as_view(), name="api-register"),
    path("api/token/", TokenObtainPairView.as_view(), name="api-get-token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="api-refresh-token"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="api-verify-token"),
]
