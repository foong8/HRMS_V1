from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy


from employees.mixins import SuperuserAndLoginRequiredMixin, SuperUserAndStaffMixin, StaffMixin
from .models import (
                    CountryBaseInfo,
                    CountryAssignment,
                    CountryFiles,
                    CountyLinkDirectory,
                    AnnualCountryLinkDirectory,
                    QuarterCountryLinkDirectory,
                    MonthCountryLinkDirectory,
                    )


class CountryBaseInfoListView(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = 'lis_country_base_info.html'
    context_object_name = "object"

    def get_queryset(self):

        queryset = CountryBaseInfo.objects.all()
        return queryset


class CountryAssignmentListView(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = 'lis_country_assignment.html'
    context_object_name = "object"

    def get_queryset(self):

        queryset = CountryAssignment.objects.all()
        return queryset


class CountyLinkDirectoryListView(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = 'lis_country_link_directory.html'

    def get_queryset(self):

        queryset = AnnualCountryLinkDirectory.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AnnualCLD"] = AnnualCountryLinkDirectory.objects.all()
        context["QuarterCLD"] = QuarterCountryLinkDirectory.objects.all()
        context["MonthCLD"] = MonthCountryLinkDirectory.objects.all()

        return context


class CountryOperation(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = "lis_country_operation.html"
    context_object_name = "object"

    def get_queryset(self):

        queryset = CountryAssignment.objects.all()
        return queryset


class CountryQCError(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = "lis_country_qcerror.html"
    context_object_name = "object"

    def get_queryset(self):
        queryset = CountryAssignment.objects.all()
        return queryset


class YFileDaily(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = "lis_yfiledaily.html"
    context_object_name = "object"

    def get_queryset(self):
        queryset = CountryAssignment.objects.all()
        return queryset


class DailyITTasksStatus(SuperUserAndStaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = "lis_daily_IT_tasks_status.html"
    context_object_name = "object"

    def get_queryset(self):
        queryset = CountryAssignment.objects.all()
        return queryset
