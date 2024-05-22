from rest_framework import serializers
from .models import *

class RecipeSerializer(serializers.ModelSerializer):
    chef = serializers.StringRelatedField(read_only=True) #This is the line we added
    class Meta:
        model = Recipe
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
