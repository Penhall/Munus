from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from .models import UserRole

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(reverse('login'))
                
            if request.user.role not in roles:
                return HttpResponseForbidden("Você não tem permissão para acessar esta página")
                
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def gerente_required(view_func):
    return role_required(UserRole.GERENTE.value)(view_func)

def analista_required(view_func):
    return role_required(UserRole.ANALISTA.value)(view_func)

def suporte_required(view_func):
    return role_required(UserRole.SUPORTE.value)(view_func)
