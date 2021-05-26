from django.urls import path
from .views import EmployeesHome, EmployeeHandbook

from country.views import (
                        CountryBaseInfoListView,
                        CountryAssignmentListView,
                        CountyLinkDirectoryListView,
                        CountryOperation,
                        CountryQCError,
                        YFileDaily,
                        DailyITTasksStatus)

from .views_admin import (
                    UserListView,
                    UserDetailView,
                    EmployeePersonalInfoUpdateView,
                    EmploymentInfoUpdateView,
                    EmployeeLeaveUpdateView,
                    UserCreateView,
                    UserDeleteView,
                    LeaveManagementListView,
                    LeaveUpdateView,
                    HomeListView,
                    )

from .views_staff import (
                    StaffPersonalInfoUpdateView,
                    StaffLeaveListView,
                    StaffLeaveCreateView,
                    StaffLeaveUpdateView,
                    )

app_name = "employees"

urlpatterns = [
    # general view
    path('', EmployeesHome.as_view(), name="employees_home"),
    path('handbook/', EmployeeHandbook.as_view(), name="employee_handbook"),

    # admin view
    path('admin_list_home/', HomeListView.as_view(), name='admin_home'),
    path('admin_list_leave_management/', LeaveManagementListView.as_view(), name='admin_list_leave_management'),
    path('admin_list_user/', UserListView.as_view(), name='admin_lis_user'),
    path('admin_create_new_user/', UserCreateView.as_view(), name='admin_cre_user'),
    path('admin_update_emp_personal_info/<int:pk>/', EmployeePersonalInfoUpdateView.as_view(), name='admin_upd_emppersonalinfo'),
    path('admin_update_emp_info/<int:pk>/', EmploymentInfoUpdateView.as_view(), name='admin_upd_empinfo'),
    path('admin_update_emp_leave/<int:pk>/', EmployeeLeaveUpdateView.as_view(), name='admin_upd_empleave'),
    path('admin_update_leave/<int:pk>/', LeaveUpdateView.as_view(), name="admin_upd_leave"),
    path('admin_delete_user/<int:pk>/', UserDeleteView.as_view(), name='admin_del_user'),
    path('admin_list_country_base_info/', CountryBaseInfoListView.as_view(), name='admin_lis_country_base_info'),
    path('admin_list_country_assignment/', CountryAssignmentListView.as_view(), name='admin_lis_country_assignment'),
    path('admin_list_country_link_directory/', CountyLinkDirectoryListView.as_view(), name='admin_lis_country_link_directory'),
    path('admin_list_country_operation/', CountryOperation.as_view(), name='admin_lis_country_operation'),
    path('admin_list_country_qcerror/', CountryQCError.as_view(), name='admin_lis_country_qcerror'),
    path('admin_list_country_yfiledaily/', YFileDaily.as_view(), name='admin_lis_y_filedaily'),
    path('admin_list_dailyITTasksStatus/', DailyITTasksStatus.as_view(), name='admin_daily_IT_TasksStatus'),
    # staff view
    path('staff_list_leave/', StaffLeaveListView.as_view(), name='staff_lis_leave'),
    path('staff_create_leave/', StaffLeaveCreateView.as_view(), name='staff_cre_leave'),
    path('staff_update_personal_info/<int:pk>/', StaffPersonalInfoUpdateView.as_view(), name='staff_upd_personalinfo'),
    path('staff_update_leave/<int:pk>/', StaffLeaveUpdateView.as_view(), name='staff_upd_leave'),
]