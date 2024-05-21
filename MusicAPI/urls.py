from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tracks', viewset=TrackViewSet, basename="tracks")
router.register(r'albums', viewset=AlbumViewSet, basename="albums")
router.register(r'artists', viewset=ArtistViewSet, basename='artists')

urlpatterns = [
    path('', include(router.urls))
]