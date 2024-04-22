from django import forms
from django.db import models
from projects.models import project


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    projects = models.ManyToManyField(project)

    def __str__(self):
        return self.name