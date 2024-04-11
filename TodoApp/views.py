from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializer import TodoSerializer


class TodoListView(APIView):
    def get(self, request):
        data = Todo.objects.all()
        serialized_data = TodoSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = TodoSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):
    def get(self, request, id):
        data = Todo.objects.get(id=id)
        serialized_data = TodoSerializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        t_data = Todo.objects.get(id=id)
        serialized_data = TodoSerializer(t_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = Todo.objects.get(id=id)
        data.delete()
        return Response({"message":"Deleted Successfully"}, status=status.HTTP_200_OK)