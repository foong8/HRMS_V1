from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .mixins import SuperuserAndLoginRequiredMixin, SuperUserAndStaffMixin
from .models import (EmployeePersonalInfo,
                     EmploymentInfo,
                     EmployeeLeave,
                     User,
                     LeaveRecord)

from .forms import (EmployeePersonalInfoModelForm,
                    EmploymentInfoModelForm,
                    EmployeeLeaveModelForm,
                    UserModelForm,
                    AdminUpdateLeaveModelForm)

from country.models import (
                    CountryBaseInfo,
                    AnnualCountryLinkDirectory,
                    QuarterCountryLinkDirectory,
                    MonthCountryLinkDirectory,
                    )


class HomeListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "admin_template/admin_lis_home.html"

    def get_queryset(self):

        queryset = AnnualCountryLinkDirectory.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AnnualCLD"] = AnnualCountryLinkDirectory.objects.count()
        context["QuarterCLD"] = QuarterCountryLinkDirectory.objects.count()
        context["MonthCLD"] = MonthCountryLinkDirectory.objects.count()
        context["CountTotalCountry"] = CountryBaseInfo.objects.count()
        context["CountEmployee"] = EmployeePersonalInfo.objects.count()
        context["LeavePendingApprove"] = LeaveRecord.objects.filter(leave_status__exact=3).count()

        return context






class UserListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "admin_template/admin_lis_user.html"
    context_object_name = "personal_info"

    def get_queryset(self):

        queryset = EmployeePersonalInfo.objects.all()
        return queryset


class UserDetailView(SuperUserAndStaffMixin, generic.DetailView):
    template_name = "admin_template/admin_det_user.html"
    model = User
    context_object_name = "object"


class UserCreateView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "admin_template/admin_cre_user.html"
    model = User
    form_class =UserModelForm
    context_object_name = "user"

    def get_success_url(self):
        return reverse("employees:admin_lis_user")

    def get_success_message(self, cleaned_data):
        return "New user has been created"


class UserDeleteView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = 'admin_template/admin_del_user.html'
    model = User
    form_class = UserModelForm
    context_object_name = "user"

    def get_success_url(self):
         return reverse("employees:admin_lis_user")

    def get_success_message(self, cleaned_data):
        return "User has been deleted"


class EmployeePersonalInfoUpdateView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):

    template_name = 'admin_template/admin_upd_employeepersonalinfo.html'
    model = EmployeePersonalInfo
    form_class = EmployeePersonalInfoModelForm
    context_object_name = "object"

    def get_success_url(self):
        return reverse_lazy("employees:admin_upd_emppersonalinfo", kwargs={'pk':self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Employee Personal Info has been updated successfully!"


class EmploymentInfoUpdateView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = 'admin_template/admin_upd_employmentinfo.html'
    model = EmploymentInfo
    form_class = EmploymentInfoModelForm
    context_object_name = 'object'

    def get_success_url(self):
        return reverse_lazy("employees:admin_upd_empinfo", kwargs={'pk': self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Employment Info has been updated successfully!"


class EmployeeLeaveUpdateView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = 'admin_template/admin_upd_employeeleave.html'
    model = EmployeeLeave
    form_class = EmployeeLeaveModelForm
    context_object_name = 'object'

    def get_success_url(self):
        return reverse_lazy("employees:admin_upd_empleave", kwargs={'pk': self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Employee leave has been updated successfully!"


class LeaveManagementListView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = 'admin_template/admin_lis_leave_management.html'
    context_object_name = "object"

    def get_queryset(self):
        leaverecord = LeaveRecord.objects.all()
        queryset = { 'leave_approved': leaverecord.filter(leave_status__exact=1),
                     'leave_canceled': leaverecord.filter(leave_status__exact=2),
                     'leave_pending': leaverecord.filter(leave_status__exact=3)
                     }
        return queryset


class LeaveUpdateView(SuperuserAndLoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):

    context_object_name = 'object'
    form_class = AdminUpdateLeaveModelForm
    model = LeaveRecord
    template_name = "admin_template/admin_upd_leave.html"
    context_object_name = 'object'

    def get_success_url(self):

        return reverse("employees:admin_list_leave_management")

    def get_success_message(self, cleaned_data):
        if cleaned_data['leave_status'] == "1":
            success_msg = "Leave has been approved here"

        elif cleaned_data['leave_status'] == "2":
            success_msg = "Leave has been cancelled"
        else:
            success_msg = "Update Error!"

        return success_msg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employeeleave = EmployeeLeave.objects.get(user__exact=self.object.user)
        context['employeeleave'] = employeeleave

        return context

    def form_valid(self, form):
        if "approve" in self.request.POST:
            form.cleaned_data['leave_status'] = "1"
            form.instance.leave_status = "1"

            # if approved, deduct the total balance leave
            employeeleave = EmployeeLeave.objects.get(user__exact=self.object.user)
            employeeleave.total_count_leave_balance -= form.instance.leave_total_day
            employeeleave.save()

        elif "cancel" in self.request.POST:
            form.instance.leave_status = "2"
            form.cleaned_data['leave_status'] = "2"

        return super(LeaveUpdateView, self).form_valid(form)

