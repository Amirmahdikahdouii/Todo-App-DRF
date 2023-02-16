from django.contrib.auth.backends import BaseBackend
from .models import User


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            return User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
