from .models import *
from .serializer import BookSerializer, ReaderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .permission import *

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUserOrReadOnly])
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
@permission_classes([IsAdminUserOrReadOnly])
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

@api_view(['GET', 'POST'])
def ReaderListView(request):
    if request.method == "POST":
        serialized_data = ReaderSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    reader_data = Reader.objects.all()
    serialized_data = ReaderSerializer(reader_data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def ReaderDetailView(request, id):
    if request.method == 'PUT':
        reader_data = Reader.objects.get(id=id)
        serialized_data = ReaderSerializer(reader_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reader_data = Reader.objects.get(id=id)
        reader_data.delete()
        return Response({"message":"Deleted Successfully!"}, status=status.HTTP_200_OK)

    reader_data = Reader.objects.get(id=id)
    serialized_data = ReaderSerializer(reader_data)
    return Response(serialized_data.data, status=status.HTTP_200_OK)



