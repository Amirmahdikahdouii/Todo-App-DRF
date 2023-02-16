from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        pass

    def create_superuser(self, email, password, **kwargs):
        pass
