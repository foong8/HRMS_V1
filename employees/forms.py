from crispy_forms import helper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Field, Div
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput
from .models import (EmployeePersonalInfo,
                     EmploymentInfo,
                     EmployeeLeave,
                     User,
                     LeaveRecord,)


class DateInput(forms.DateInput):
    input_type = 'date'


class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class EmployeePersonalInfoModelForm(forms.ModelForm):
    class Meta:
        model = EmployeePersonalInfo
        fields = '__all__'
        exclude = ['user',
                   'income_tax_number']


class EmploymentInfoModelForm(forms.ModelForm):
    class Meta:
        model = EmploymentInfo
        fields = '__all__'
        exclude = ['user']


class EmployeeLeaveModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeave
        fields = '__all__'
        exclude = ['user']


class StaffApplyLeaveModelForm(forms.ModelForm):
    class Meta:
        model = LeaveRecord
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'leave_status']
        widgets = {
            'leave_start_date': DateInput(),
            'leave_end_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit',
                                     'Submit',
                                     css_class='btn-success',
                                     style="margin-top:10px",
                                     ))
        self.helper.layout = Layout(
                Field('leave_type', css_class='col-md-6 mb-0'),
                Field('leave_start_date', css_class='col-md-6 mb-0'),
                Field('leave_end_date', css_class='col-md-6 mb-0'),
                Field('leave_total_day', css_class='col-md-6 mb-0'),
                Field('leave_message', placeholder='Leave your message here', css_class='col-md-6 mb-0'),
        )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data_end_date = cleaned_data['leave_end_date']
        cleaned_data_start_date = cleaned_data['leave_start_date']

        if cleaned_data_end_date is None or cleaned_data_start_date is None:
            raise forms.ValidationError("Leave start date and end date cant be blank")

        if cleaned_data_end_date < cleaned_data_start_date:
            raise forms.ValidationError("Leave end date must be later than leave start date")


class StaffUpdateLeaveModelForm(forms.ModelForm):
    class Meta:
        model = LeaveRecord
        fields = []


class AdminUpdateLeaveModelForm(forms.ModelForm):
    class Meta:
        model = LeaveRecord
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(AdminUpdateLeaveModelForm, self).__init__(*args, **kwargs)
        self.fields['leave_type'].widget.attrs['readonly'] = True
        self.fields['leave_start_date'].widget.attrs['readonly'] = True
        self.fields['leave_end_date'].widget.attrs['readonly'] = True
        self.fields['leave_total_day'].widget.attrs['readonly'] = True
        self.fields['leave_message'].widget.attrs['readonly'] = True
        self.fields['leave_status'].widget.attrs['readonly'] = True