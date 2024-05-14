from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Author, Category, Book
from .serializer import AuthorSerializer, CategorySerializer, BookSerializer
from rest_framework import mixins, generics

# Create your views here.
#Generic Views
class BookListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #get method
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #post method
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AuthorListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




#Normal class based views
class BookListView(APIView):
    def get(self, request):
        data = Book.objects.all()
        serialized_data = BookSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = BookSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
