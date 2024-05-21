from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Track.objects.all()
        serialized_data = TrackSerializer(queryset, many=True)
        return Response(serialized_data.data)

class AlbumViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Album.objects.all()
        serialized_data = AlbumSerializer(queryset, many=True)
        return Response(serialized_data.data)

class ArtistViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Artist.objects.all()
        serialized_data = ArtistSerializer(queryset, many=True)
        return Response(serialized_data.data)



