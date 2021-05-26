from django.contrib import admin
from .models import (EmployeePersonalInfo, EmploymentInfo,
                     EmployeeLeave, LeaveRecord, UserProfile, User
                     )


admin.site.register(EmployeePersonalInfo)
admin.site.register(EmploymentInfo)
admin.site.register(EmployeeLeave)
admin.site.register(LeaveRecord)
admin.site.register(UserProfile)
admin.site.register(User)
