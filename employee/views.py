from django.shortcuts import render
from django.http import HttpResponse


def employee(request):
    return HttpResponse("This is the employee's page")


def profile(request):
    return render(request, "employee/profile.html")
