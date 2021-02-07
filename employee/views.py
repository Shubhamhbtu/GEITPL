from django.shortcuts import render
from .models import Employee, Project
from dateutil import relativedelta


def dashboard(request):
    count_employee = Employee.objects.all().count()
    count_project = Project.objects.all().count()
    context = {
        'Employee': count_employee,
        'Project': count_project,
    }
    return render(request, 'dashboard.html', context)


def employee(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, 'employee.html', context)


def project(request):
    projects = Project.objects.all()
    context = {
            'projects': projects,
    }
    return render(request, 'projects.html', context)
