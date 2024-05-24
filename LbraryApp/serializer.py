from rest_framework import serializers
from .models import *
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"

