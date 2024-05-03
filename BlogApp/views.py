from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, Blog
from .serializer import BlogSerializer, CategorySerializer

# Create your views here.
class BlogDetailView(APIView):
    def get(self, request):
        data = Blog.objects.all()
        serialized_data = BlogSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = BlogSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

