from django.contrib import admin
from django.urls import path
from .views import project_home, add_project, edit_project, delete_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", project_home, name='home'),
    path("add_project/", add_project, name='add_project'),
    path("edit_project/<int:project_id>/", edit_project, name='edit_project'),
    path("delete_project/<int:project_id>/", delete_project, name='delete_project'),
]
