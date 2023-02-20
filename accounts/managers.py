from django.contrib.auth.models import BaseUserManager
from django.db import models


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

    # Method to check email exists or not
    def check_email_exist(self, email_value):
        return self.filter(email=self.normalize_email(email_value)).exists()


class VerifyEmailManager(models.Manager):
    def email_exists(self, email):
        """
        This Method will check existing email is True or not
        """
        return self.filter(email=email).exists()

    def check_email_verification(self, email):
        """
        This method will check existing email and verification
        """
        return self.filter(email=email, is_verified=True).exists()
