from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Model Managers
from .managers import CustomUserManager, VerifyEmailManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=250)
    first_name = models.CharField(blank=True, null=True, max_length=100)
    last_name = models.CharField(blank=True, null=True, max_length=100)
    birthday = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    join_date = models.DateField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # We Will handle this later
        return True

    def has_module_perms(self, app_label):
        # We Will handle this later
        return True


class VerifyEmail(models.Model):
    email = models.EmailField(unique=True, max_length=250)
    verify_key = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    verification_time = models.DateTimeField(auto_now=True)

    objects = VerifyEmailManager()

    def __str__(self):
        return self.email
