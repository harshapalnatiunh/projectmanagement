from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project_home(request):
    return render(request,"projects/home.html",{}) 


def add_project(request):
    return render(request,"projects/add_project.html",{})