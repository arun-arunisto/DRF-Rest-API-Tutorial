from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET']) #this decorator only used when we use function based views
def employee_list(request):
    all_emp = Employee.objects.all()
    #converting to json using serializer
    serialized_data = EmployeeSerializer(all_emp, many=True) #if we are fetching more than one data we need to add many=True
    return Response(serialized_data.data)

@api_view(["GET"])
def employee_details(request, id):
    emp = Employee.objects.get(id=id)
    serialized_data = EmployeeSerializer(emp)
    return Response(serialized_data.data)


