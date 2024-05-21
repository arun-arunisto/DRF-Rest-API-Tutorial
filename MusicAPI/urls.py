from django.urls import path
from .views import *

urlpatterns = [
    path('track-list-create-view/', TrackListCreateView.as_view(), name="track-list-create-view"),
    path('album-list-create-view/', AlbumListCreateView.as_view(), name="album-list-create-view"),
    path('artist-list-create-view/', ArtistListCreateView.as_view(), name='artist-list-create-view')
]