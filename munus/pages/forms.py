from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django.utils.translation import gettext_lazy as _
from .models import UserProfile, UserRole


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": _("Email")}
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": _("Password")}
        ),
    )


class CustomSignupForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome"}),
        max_length=30,
        required=True,
    )
    last_name = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Sobrenome"}
        ),
        max_length=30,
        required=True,
    )
    phone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "(99) 99999-9999"}
        ),
        max_length=15,
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "seu@email.com"}
        ),
    )

    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "phone", "email", "password1", "password2")

    error_messages = {
        "password_mismatch": "As senhas não coincidem.",
        "password_too_short": "A senha deve conter pelo menos 8 caracteres.",
        "password_common": "A senha é muito comum.",
        "password_entirely_numeric": "A senha não pode ser apenas números.",
    }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Current Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password1 = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


from .models import UploadedFile


class UploadFileForm(forms.ModelForm):
    description = forms.CharField(
        label=_("File description"),
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": _("Optional description of the file contents"),
            }
        ),
    )

    class Meta:
        model = UploadedFile
        fields = ["file"]
        widgets = {
            "file": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": ".csv, .xlsx, .txt"}
            )
        }
