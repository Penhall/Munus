from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import os
from enum import Enum


class UserRole(Enum):
    MANAGER = "manager"
    ANALYST = "analyst"
    FREE_USER = "free_user"
    PAID_USER = "paid_user"
    SUPPORT = "support"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.MANAGER.value)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractUser):
    objects = UserManager()
    
    role = models.CharField(
        max_length=20, choices=UserRole.choices(), default=UserRole.FREE_USER.value
    )
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Remove username field since we're using email as primary identifier
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

    @property
    def is_manager(self):
        return self.role == UserRole.MANAGER.value

    @property
    def is_analyst(self):
        return self.role == UserRole.ANALYST.value

    @property
    def is_free_user(self):
        return self.role == UserRole.FREE_USER.value

    @property
    def is_paid_user(self):
        return self.role == UserRole.PAID_USER.value

    @property
    def is_support(self):
        return self.role == UserRole.SUPPORT.value


class ManagerProfile(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="manager_profile"
    )
    can_manage_users = models.BooleanField(default=True)
    can_assign_roles = models.BooleanField(default=True)
    can_configure_models = models.BooleanField(default=True)


class AnalystProfile(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="analyst_profile"
    )
    can_upload_files = models.BooleanField(default=True)
    can_train_models = models.BooleanField(default=True)
    can_view_reports = models.BooleanField(default=True)


class SupportProfile(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="support_profile"
    )
    can_reset_passwords = models.BooleanField(default=True)
    can_view_logs = models.BooleanField(default=True)
    can_manage_tickets = models.BooleanField(default=True)


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="uploaded_files",
        null=True, blank=True
    )

    def process_file(self):
        # Implementar lógica de processamento do arquivo aqui
        return f"Pré-visualização do arquivo {os.path.basename(self.file.name)}"
