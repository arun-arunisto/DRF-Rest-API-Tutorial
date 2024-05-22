from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


# Create your views here.
class ChefModelView(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
