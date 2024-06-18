from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import LogCredSerializers
from .models import LoginCredUsers
import logging
from rest_framework.viewsets import generics

"""@api_view(['GET', 'POST'])
def advanced_methods(request):
    return Response({"message":"Hello World})"""

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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
    try:
        user_data = LoginCredUsers.objects.get(id=pk)
    except LoginCredUsers.DoesNotExist:
        logger.error(f"User {pk} Doesn't exist!")
        return Response({"error":"User not found!"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serialized_data = LogCredSerializers(user_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        user_data.delete()
    if request.method == "GET":
        serialized_data = LogCredSerializers(user_data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


#class based views
class UserListView(generics.ListCreateAPIView):
    queryset = LoginCredUsers.objects.all()
    serializer_class = LogCredSerializers

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoginCredUsers.objects.all()
    serializer_class = LogCredSerializers
    


