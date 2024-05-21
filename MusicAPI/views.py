from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Track.objects.all()
        serialized_data = TrackSerializer(queryset, many=True)
        return Response(serialized_data.data)

    def retrieve(self, request, pk=None):
        queryset = Track.objects.all()
        track = get_object_or_404(queryset, pk=pk)
        serialized_data = TrackSerializer(track)
        return Response(serialized_data.data)

class AlbumViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Album.objects.all()
        serialized_data = AlbumSerializer(queryset, many=True)
        return Response(serialized_data.data)

    def retrieve(self, request, pk=None):
        queryset = Album.objects.all()
        album = get_object_or_404(queryset, pk=pk)
        serialized_data = AlbumSerializer(album)
        return Response(serialized_data.data)

class ArtistViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Artist.objects.all()
        serialized_data = ArtistSerializer(queryset, many=True)
        return Response(serialized_data.data)

    def retrieve(self, request, pk=None):
        queryset = Artist.objects.all()
        artist = get_object_or_404(queryset, pk=pk)
        serialized_data = ArtistSerializer(artist)
        return Response(serialized_data.data)




