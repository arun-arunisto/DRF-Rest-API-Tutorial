from rest_framework import serializers
from .models import LoginCredUsers, FileUpload

class LogCredSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginCredUsers
        fields = "__all__"

    #here we will implement the hashing password logic when the time of creating user   
    def create(self, validated_data):
        user = LoginCredUsers(**validated_data)
        user.hash_passwrd(validated_data['pass_wd'])
        user.save()
        return user

    #update method if there will be data present in the validated_data before updating the user
    def update(self, instance, validated_data):
        if 'pass_wd' in validated_data:
            instance.hash_passwrd(validated_data['pass_wd'])
            validated_data['pass_wd'] = instance.pass_wd
        return super().update(instance, validated_data)

class LoginFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    pass_wd = serializers.CharField(write_only=True)
    class Meta:
        model = LoginCredUsers
        exclude = ("mail_id",)

# file upload serializer
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"


### for stackoverflow

        


