from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializer import *

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecipeSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"No data available"}, status=status.HTTP_204_NO_CONTENT)


class ChefListCreateView(generics.ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ChefSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"No data available"}, status=status.HTTP_204_NO_CONTENT)
