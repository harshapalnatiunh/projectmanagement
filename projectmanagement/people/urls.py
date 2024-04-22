from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path("home/", people_home,name='employee_list'),
    path('fetch_people_data/', fetch_people_data, name='fetch_people_data'),

]
