from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employee/', views.employee, name="Employee"),
    path('project/', views.project, name="Project")
]