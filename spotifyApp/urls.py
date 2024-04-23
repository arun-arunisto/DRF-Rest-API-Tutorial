from django.urls import path
from .views import TracksListView, TrackDetailView


urlpatterns = [
    path('tracks-list-view/', TracksListView.as_view(), name="tracks-list"),
    path('tracks-detail-view/<int:pk>/', TrackDetailView.as_view(), name="track-detail-view")
]