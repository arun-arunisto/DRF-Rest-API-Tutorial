from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
@api_view(['GET', 'POST']) #this decorator only used when we use function based views
@permission_classes([IsAdminUser])
def employee_list(request):
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    all_emp = Employee.objects.all()
    #converting to json using serializer
    serialized_data = EmployeeSerializer(all_emp, many=True) #if we are fetching more than one data we need to add many=True
    return Response(serialized_data.data, status=status.HTTP_200_OK) #status code 200

@api_view(["GET", "PUT", "DELETE"])
def employee_details(request, id):
    if request.method == "PUT":
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response({"message":"Success"}, status=status.HTTP_200_OK)
    emp = Employee.objects.get(id=id)
    serialized_data = EmployeeSerializer(emp)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


