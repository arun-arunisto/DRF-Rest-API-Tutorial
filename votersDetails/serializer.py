from rest_framework import serializers
from .models import Voters

class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = "__all__"

    #field-level validations
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return value

