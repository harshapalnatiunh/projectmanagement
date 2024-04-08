from django.db import models

# Create your models here.
class project(models.Model):
    name= models.CharField(max_length=200)
    project_id = models.CharField(max_length=200)
    project_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name