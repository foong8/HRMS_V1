from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class EmployeesHome(LoginRequiredMixin, TemplateView):
    template_name = "base.html"


class EmployeeHandbook(LoginRequiredMixin, TemplateView):
    template_name = "handbook.html"