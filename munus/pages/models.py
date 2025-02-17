from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import os
from enum import Enum


class UserRole(Enum):
    GERENTE = "gerente"
    ANALISTA = "analista"
    SUPORTE = "suporte"
    CLIENTE = "cliente"
    USUARIO = "usuario"

    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls]


from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRole.GERENTE.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    objects = UserManager()

    role = models.CharField(
        max_length=20, choices=UserRole.choices(), default=UserRole.USUARIO.value
    )
    email = models.EmailField(_("email address"))
    created_at = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_users",
    )
    approval_date = models.DateTimeField(null=True, blank=True)

    # Remove username field since we're using email as primary identifier
    username = None

    phone = models.CharField(
        max_length=15, verbose_name="Telefone", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

    @property
    def is_gerente(self):
        return self.role == UserRole.GERENTE.value

    @property
    def is_analista(self):
        return self.role == UserRole.ANALISTA.value

    @property
    def is_suporte(self):
        return self.role == UserRole.SUPORTE.value

    @property
    def is_cliente(self):
        return self.role == UserRole.CLIENTE.value

    @property
    def is_usuario(self):
        return self.role == UserRole.USUARIO.value


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
        UserProfile,
        on_delete=models.CASCADE,
        related_name="uploaded_files",
        null=True,
        blank=True,
    )

    def process_file(self):
        # Implementar lógica de processamento do arquivo aqui
        return f"Pré-visualização do arquivo {os.path.basename(self.file.name)}"
