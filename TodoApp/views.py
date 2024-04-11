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

