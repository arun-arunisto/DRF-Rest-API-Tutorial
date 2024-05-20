from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
class MovieSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(max_length=50)
    movie = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"

