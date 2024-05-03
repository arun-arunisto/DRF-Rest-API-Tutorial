from rest_framework import serializers
from .models import Album, Tracks

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = "__all__"

#Serializer for Album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ["id"]
