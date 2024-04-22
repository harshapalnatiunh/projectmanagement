from django.db import models
from projects.models import project


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    projects = models.ManyToManyField(project)

    def __str__(self):
        return self.name