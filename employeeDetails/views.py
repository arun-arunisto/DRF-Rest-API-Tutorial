from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse

# Create your views here.
def employee_list(request):
    data = {
        "App Name":"Employee Details",
        "Method":"employee_details",
        "End Point":"/api/employee-details-api/employee-list"
    }

    return JsonResponse(data)
