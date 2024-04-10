from .models import StudentData
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "POST":
        serialized_data = StudentSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    student_data = StudentData.objects.all()
    serialized_data = StudentSerializer(student_data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    if request.method == "PUT":
        student_data = StudentData.objects.get(id=id)
        serialized_data = StudentSerializer(student_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        student_data = StudentData.objects.get(id=id)
        student_data.delete()
        return Response({"Message":"Deleted Successfully"}, status=status.HTTP_200_OK)
    student_data = StudentData.objects.get(id=id)
    serialized_data = StudentSerializer(student_data)
    return Response(serialized_data.data, status=status.HTTP_200_OK)
