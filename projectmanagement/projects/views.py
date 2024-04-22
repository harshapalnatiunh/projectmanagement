from django.shortcuts import render, redirect, get_object_or_404
from .models import project
from .forms import *
from employee.models import Employee
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


def add_project(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        project_id = request.POST.get('project_id')
        new_project = project.objects.create(name=name, project_id=project_id)
        return redirect('home')  # Redirect to home page after form submission
    else:
        return render(request, "projects/add_project.html", {})

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
        # Handle form submission for editing project
        name = request.POST.get('name')
        project_id = request.POST.get('project_id')
        proj.name = name
        proj.project_id = project_id
        proj.save()
        return redirect('home')  # Redirect to home page after editing
    else:
        return render(request, 'projects/edit_project.html', {'proj': proj})

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
