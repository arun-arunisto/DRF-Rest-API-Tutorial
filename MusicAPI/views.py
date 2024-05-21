from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
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

    #creare
    def create(self, request):
        serialized_data = TrackSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        track = get_object_or_404(Track, pk=pk)
        serialized_data = TrackSerializer(track, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    def destroy(self, request, pk=None):
        track = get_object_or_404(Track, pk=pk)
        track.delete()
        return Response({"message":"Deleted Successfully"})

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

    def create(self, request):
        serialized_data = AlbumSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    def update(self, request, pk=None):
        album = get_object_or_404(Album, pk=pk)
        serialized_data = AlbumSerializer(album, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    def destroy(self, request, pk=None):
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return Response({"message":"Deleted Successfully!"})

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

    def create(self, request):
        serialized_data = ArtistSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    def update(self, request, pk=None):
        artist = get_object_or_404(Artist, pk=pk)
        serialized_data = ArtistSerializer(artist, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)

    def destroy(self, request, pk=None):
        artist = get_object_or_404(Artist, pk=pk)
        artist.delete()
        return Response({"message":"Deleted Successfully!"})




