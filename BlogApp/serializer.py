from rest_framework import serializers
from .models import Category, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ["id"]