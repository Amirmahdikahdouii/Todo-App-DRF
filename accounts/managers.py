from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email Field is required")
        if password is None:
            raise ValueError("Password Field is required")
        obj = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        obj.set_password(password)
        obj.save()
        return obj

    def create_superuser(self, email, password, **kwargs):
        obj = self.create_user(email, password, **kwargs)
        obj.is_admin = True
        obj.save()
        return obj
