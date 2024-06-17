from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def advanced_methods(request):
    return Response({"message":"Hello World"})

