from django import forms
from .models import project
from employee.models import Employee
from django.core.exceptions import ValidationError


class ProjectEditForm(forms.ModelForm):
    employees_to_remove = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = project
        fields = ['name', 'project_id', 'project_status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If this is an existing project
            self.fields['employees_to_remove'].queryset = self.instance.employee_set.all()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 6 or len(name) > 20:
            raise ValidationError("Project name should be more than 6 characters and less than 20 characters.")
        if self.instance:
            if project.objects.filter(name=name).exclude(id=self.instance.id).exists():
                raise ValidationError("Project with this name already exists.")
        else:
            if project.objects.filter(name=name).exists():
                raise ValidationError("Project with this name already exists.")
        return name

    def clean_project_id(self):
        project_id = self.cleaned_data.get('project_id')
        if self.instance:
            if project.objects.filter(project_id=project_id).exclude(id=self.instance.id).exists():
                raise ValidationError("Project with this ID already exists.")
        else:
            if project.objects.filter(project_id=project_id).exists():
                raise ValidationError("Project with this ID already exists.")
        return project_id


class AddEmployeeForm(forms.Form):
    employee_name = forms.CharField(max_length=100)
    employee_age = forms.IntegerField()
    employee_email = forms.EmailField()
    employee_phone = forms.CharField(max_length=200)
    employee_image = forms.ImageField(required=False)
    # Assuming gender is a choice field
    employee_gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')])

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = project
