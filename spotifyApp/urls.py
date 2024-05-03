from django.urls import path
from .views import TracksListView, TrackDetailView, AlbumListView


urlpatterns = [
    path('tracks-list-view/', TracksListView.as_view(), name="tracks-list"),
    path('tracks-detail-view/<int:pk>/', TrackDetailView.as_view(), name="track-detail-view"),
    path('album-list-view/', AlbumListView.as_view(), name='album-list')
]