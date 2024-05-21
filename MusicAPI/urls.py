from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tracks', viewset=TrackViewSet, basename="tracks")
router.register(r'albums', viewset=AlbumViewSet, basename="albums")
router.register(r'artists', viewset=ArtistViewSet, basename='artists')
router.register(r'tracks-model-view', viewset=TrackModelView, basename='tracks-model-view')
router.register(r'album--model-view', viewset=AlbumModelView, basename='album-model-view')
router.register(r'artist-model-view', viewset=ArtistModelView, basename='artist-model-view')


urlpatterns = [
    path('', include(router.urls))
]