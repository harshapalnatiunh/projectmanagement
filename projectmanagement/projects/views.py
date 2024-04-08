from django.shortcuts import render, redirect, get_object_or_404
from .models import project

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