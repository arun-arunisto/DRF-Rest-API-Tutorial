from rest_framework import serializers
from .models import Author, Category, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ["id"]

class AuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField()
    author = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        exclude = ["id"]


