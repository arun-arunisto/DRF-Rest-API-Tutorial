from rest_framework import serializers
from .models import StudentData

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        #choosing fields as a list
        fields = ["name", "degree", "specialization", "joined_at", "passed_out"]
