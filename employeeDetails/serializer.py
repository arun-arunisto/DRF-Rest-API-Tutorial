from rest_framework import serializers
from .models import Employee

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

    #post request
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    #put request
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.address = validated_data.get('address', instance.address)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.joined_at = validated_data.get('joined_at', instance.joined_at)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance