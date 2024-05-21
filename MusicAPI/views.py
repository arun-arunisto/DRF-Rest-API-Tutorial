from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = AlbumSerializer

class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
