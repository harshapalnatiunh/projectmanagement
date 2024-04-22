from django import forms
from .models import project

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['name', 'project_id', 'project_status']
        
class AddEmployeeForm(forms.Form):
    employee_name = forms.CharField(max_length=100)
    employee_age = forms.IntegerField()
    employee_email = forms.EmailField()
    employee_phone = forms.CharField(max_length=200)
    employee_image = forms.ImageField(required=False)
    employee_gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])  # Assuming gender is a choice field
