from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", project_home, name='home'),
    path("add_project/", add_project, name='add_project'),
    path("edit_project/<int:project_id>/", edit_project, name='edit_project'),
    path("delete_project/<int:project_id>/", delete_project, name='delete_project'),
  path('project_detail/<int:project_id>/', project_detail, name='project_detail'),
        path('add_employee_to_project/<int:project_id>/', add_employee_to_project, name='add_employee_to_project'),


]
