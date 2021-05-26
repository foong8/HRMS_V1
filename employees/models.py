from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class EmployeePersonalInfo(models.Model):

    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    STATUS = (
        ("S", "Single"),
        ("M", "Married"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employeepersonalinfo_user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=12, blank=True, null=True)
    passport = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=1)
    BOD = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=1, blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    personal_email = models.EmailField(max_length=100, blank=True, null=True)
    income_tax_number = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_person = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Personal Info'


class EmploymentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employmentinfo_user')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    position_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Employment Status'


class EmployeeLeave(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employeeleave_user')
    total_count_leave_per_year = models.PositiveIntegerField(blank=True, null=True, default=12)
    total_count_leave_balance = models.PositiveIntegerField(blank=True, null=True, default=12)
    incremental_leave_per_month = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Employee Leave'


class LeaveRecord(models.Model):

    LEAVE_TYPE = [
        ('1', "ANNUAL LEAVE"),
        ('2', "EMERGENCY LEAVE"),
        ('3', "MEDICAL LEAVE"),
        ('4', "OTHERS")
        ]

    LEAVE_STATUS = [
        ('1', "APPROVED"),
        ('2', "CANCELED"),
        ('3', "PENDING")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leavereocrd_user')
    leave_type = models.CharField(choices=LEAVE_TYPE, max_length=1, default="1")
    leave_start_date = models.DateField(blank=True, null=True)
    leave_end_date = models.DateField(blank=True, null=True)
    leave_total_day = models.PositiveIntegerField(blank=True, null=True)
    leave_message = models.TextField(blank=True, null=True)
    leave_status = models.CharField(default="3", choices=LEAVE_STATUS, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Leave Record'


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)
        EmployeePersonalInfo.objects.create(user=instance)
        EmploymentInfo.objects.create(user=instance)
        EmployeeLeave.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

#  TODO post approve the leave record signal