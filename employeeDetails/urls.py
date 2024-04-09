from django.urls import path
from . import views

urlpatterns = [
    path('employee-list/', views.employee_list, name="employee-list"),
    path('employee-details/<int:id>', views.employee_details, name="employee-details")
]