from django.contrib.auth.backends import BaseBackend
from .models import User


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
