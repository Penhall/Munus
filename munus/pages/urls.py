from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .auth_views import (
    login_view,
    signup_view,
    logout_view,
    profile_view,
    change_password_view,
)

urlpatterns = [
    path("", views.home, name="landing"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("upload/", views.upload_file, name="upload"),
    path("data/", views.data, name="data"),
    # Authentication URLs
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("change-password/", change_password_view, name="change_password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
