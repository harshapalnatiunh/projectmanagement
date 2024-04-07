
from django.contrib import admin
from django.urls import path,include
from .views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",project_home),
    path("add_project/",add_project)

  
]
