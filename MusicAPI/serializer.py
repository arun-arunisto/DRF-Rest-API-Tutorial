from rest_framework import serializers
from .models import *

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ["id"]
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        exclude = ["id"]




