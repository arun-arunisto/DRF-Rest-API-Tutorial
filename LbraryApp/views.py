from .models import *
from .serializer import BookSerializer, ReaderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == "POST":
        serialized_data = BookSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    books = Book.objects.all()
    serialized_data = BookSerializer(books, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, id):
    if request.method == 'PUT':
        book_data = Book.objects.get(id=id)
        serialized_data = BookSerializer(book_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book_data = Book.objects.get(id=id)
        book_data.delete()
        return Response({"message":"Deleted Successfully!"}, status=status.HTTP_200_OK)

    book_data = Book.objects.get(id=id)
    serialized_data = BookSerializer(book_data)
    return Response(serialized_data.data, status=status.HTTP_200_OK)




