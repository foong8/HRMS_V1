from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .mixins import SuperuserAndLoginRequiredMixin, SuperUserAndStaffMixin, StaffMixin
from .models import (EmployeePersonalInfo,
                     EmploymentInfo,
                     EmployeeLeave,
                     LeaveRecord,
                     User)
from .forms import (EmployeePersonalInfoModelForm,
                    EmploymentInfoModelForm,
                    EmployeeLeaveModelForm,
                    UserModelForm,
                    StaffApplyLeaveModelForm,
                    StaffUpdateLeaveModelForm,)


class StaffPersonalInfoUpdateView(SuperUserAndStaffMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "staff_template/staff_upd_personalinfo.html"
    model = EmployeePersonalInfo
    form_class = EmployeePersonalInfoModelForm
    context_object_name = 'object'

    def get_success_url(self):
        return reverse_lazy("employees:staff_upd_personalinfo", kwargs={'pk':self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Employee Personal Info has been updated successfully!"


class StaffLeaveListView(StaffMixin, SuccessMessageMixin, generic.ListView):
    template_name = "staff_template/staff_lis_leave.html"
    context_object_name = 'object'

    def get_queryset(self):
        leaverecord = LeaveRecord.objects.filter(user__exact=self.request.user)
        queryset = { 'leave_approved': leaverecord.filter(leave_status__exact=1),
                     'leave_canceled': leaverecord.filter(leave_status__exact=2),
                     'leave_pending': leaverecord.filter(leave_status__exact=3)
                     }
        return queryset


class StaffLeaveCreateView(StaffMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "staff_template/staff_cre_leave.html"
    context_object_name = 'object'
    form_class = StaffApplyLeaveModelForm
    model = LeaveRecord

    def get_success_url(self):
        return reverse("employees:staff_lis_leave")

    def get_success_message(self, cleaned_data):
        return "Leave has been submitted and pending for approval"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StaffLeaveCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        employeeleave = EmployeeLeave.objects.get(user__exact=user)
        context['employeeleave'] = employeeleave
        return context


class StaffLeaveUpdateView(StaffMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "staff_template/staff_upd_leave.html"
    context_object_name = 'object'
    form_class = StaffUpdateLeaveModelForm
    model = LeaveRecord

    def get_success_url(self):
        return reverse("employees:staff_lis_leave")

    def get_success_message(self, cleaned_data):
        return "Leave has been cancelled"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.leave_status = "2"
        form.save()
        return super(StaffLeaveUpdateView, self).form_valid(form)