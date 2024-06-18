from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import LogCredSerializers
from .models import LoginCredUsers

"""@api_view(['GET', 'POST'])
def advanced_methods(request):
    return Response({"message":"Hello World})"""

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == "POST":
        serialized_data = LogCredSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors)
    
    data = LoginCredUsers.objects.all().order_by("-id")
    serialized_data = LogCredSerializers(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_user(request, pk):
    if request.method == "PUT":
        user_data = LoginCredUsers.objects.get(id=pk)
        serialized_data = LogCredSerializers(user_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        data = LoginCredUsers.objects.get(id=pk)
        data.delete()
    data = LoginCredUsers.objects.get(id=pk)
    serialized_data = LogCredSerializers(data)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

    


