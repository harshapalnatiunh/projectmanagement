from django.shortcuts import render, redirect, get_object_or_404
from .models import project
from .forms import *
from employee.models import Employee
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse

def add_project(request):
    if request.method == 'POST':
        form = ProjectEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ProjectEditForm()
    return render(request, 'projects/add_project.html', {'form': form})

def project_home(request):
    projects = project.objects.all()  # Retrieve all projects from the database
    return render(request, "projects/home.html", {'projects': projects})

def project_detail(request, project_id):
    proj = get_object_or_404(project, id=project_id)
    employees = proj.employee_set.all()  # Accessing related employees
    return render(request, 'projects/project_detail.html', {'project': proj, 'employees': employees})


def edit_project(request, project_id):
    proj = get_object_or_404(project, id=project_id)
    if request.method == 'POST':
        form = ProjectEditForm(request.POST, instance=proj)
        if form.is_valid():
            proj = form.save(commit=False)
            # Get the employees to remove
            employees_to_remove = form.cleaned_data['employees_to_remove']
            # Remove the employees from the project
            for employee in employees_to_remove:
                employee.projects.remove(proj)
                employee.save()
            proj.save()
            return HttpResponseRedirect(reverse('project_detail', args=[project_id]))
    else:
        form = ProjectEditForm(instance=proj)
    return render(request, 'projects/edit_project.html', {'form': form})

# def edit_project(request, project_id):
#     proj = get_object_or_404(project, id=project_id)
#     employees = proj.employee_set.all() 
#     if request.method == 'POST':
#         # Handle form submission for editing project
#         name = request.POST.get('name')
#         project_id = request.POST.get('project_id')
#         employees = request.POST.getlist('employees')
#         project_status = request.POST.get('project_status') == 'True' 
#         proj.name = name
#         proj.project_status = project_status
#         proj.project_id = project_id
#         proj.employee_set.clear()  # Remove all employees from the project
#         for employee_id in employees:
#             employee = get_object_or_404(Employee, id=employee_id)  # Replace 'Employee' with your actual Employee model
#             proj.employee_set.add(employee)  # Add the employee to the project
#         proj.save()
#         return HttpResponseRedirect(reverse('home'))  # Redirect to home page after editing
#     else:
#         employees = proj.employee_set.all()  # Accessing related employees
#         return render(request, 'projects/edit_project.html', {'proj': proj, 'employees': employees})

def delete_project(request, project_id):
    proj = get_object_or_404(project, id=project_id)
    if request.method == 'POST':
        # Handle form submission for deleting project
        proj.delete()
        return redirect('home')  # Redirect to home page after deletion
    else:
        return render(request, 'projects/delete_project.html', {'proj': proj})
    
def add_employee_to_project(request, project_id):
    proj = get_object_or_404(project, id=project_id)

    if request.method == 'POST':
        print("POST request received")
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            # Extract employee information from the form
            employee_name = form.cleaned_data['employee_name']
            employee_age = form.cleaned_data['employee_age']
            employee_email = form.cleaned_data['employee_email']
            employee_phone = form.cleaned_data['employee_phone']
            employee_image = form.cleaned_data['employee_image']
            employee_gender = form.cleaned_data['employee_gender']

            try:
                # Check if an employee with the same email already exists
                existing_employee = Employee.objects.get(email=employee_email)
                print("Employee already exists")
            except ObjectDoesNotExist:
                # If the employee doesn't exist, create a new one
                try:
                    print("Attempting to create employee")
                    employee = Employee.objects.create(
                        name=employee_name,
                        age=employee_age,
                        email=employee_email,
                        phone_number=employee_phone,
                        image=employee_image,
                        gender=employee_gender
                    )
                    print("Employee created successfully")

                    # Add the employee to the project and save the project
                    proj.employee_set.add(employee)
                    proj.save()
                    print("Employee added to project successfully")
                except IntegrityError as e:
                    print("Error saving employee:", e)
            else:
                # If the employee already exists, you may want to display a message or handle it differently
                print("Employee with this email already exists")

            return redirect('project_detail', project_id=project_id)
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        print("GET request received")
        form = AddEmployeeForm()

    return render(request, 'projects/project_detail.html', {'project': proj, 'form': form})
