from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class SuperuserAndLoginRequiredMixin(AccessMixin):
    """verify that the current user is authenticated and is superuser"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class SuperUserAndStaffMixin(AccessMixin):
    """verify that the current user is authenticated and is an superuser or normal staff"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("login")


class StaffMixin(AccessMixin):
    """verify that the current user is authenticated and is normal staff"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("login")