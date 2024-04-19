from rest_framework import serializers
from .models import Voters

class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = "__all__"