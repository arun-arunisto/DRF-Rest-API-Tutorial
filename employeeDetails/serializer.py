from rest_framework import serializers


#creating serializers based on models field
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.IntegerField()
    address = serializers.CharField()
    designation = serializers.CharField()
    joined_at = serializers.DateField()
    is_active = serializers.BooleanField()