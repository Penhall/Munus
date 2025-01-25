from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    UserProfile,
    ManagerProfile,
    AnalystProfile,
    SupportProfile,
    UploadedFile,
)
from .forms import CustomSignupForm, ProfileEditForm


class UserProfileAdmin(UserAdmin):
    form = ProfileEditForm
    add_form = CustomSignupForm

    list_display = ("email", "role", "is_active", "last_access")
    list_filter = ("role", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "role")}),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "role", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "can_manage_users",
        "can_assign_roles",
        "can_configure_models",
    )
    search_fields = ("user__email",)


@admin.register(AnalystProfile)
class AnalystProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "can_upload_files", "can_train_models", "can_view_reports")
    search_fields = ("user__email",)


@admin.register(SupportProfile)
class SupportProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "can_reset_passwords",
        "can_view_logs",
        "can_manage_tickets",
    )
    search_fields = ("user__email",)


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_by", "uploaded_at")
    search_fields = ("uploaded_by__email",)


admin.site.register(UserProfile, UserProfileAdmin)
