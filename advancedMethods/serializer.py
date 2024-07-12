from rest_framework import serializers
from .models import *
from .tasks import subscription_terminate_worker

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



### for the permission classes
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields= "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class AdminUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUsers
        fields = "__all__"
    
    def create(self, validated_data):
        admin = AdminUsers(**validated_data)
        admin.hash_passwrd(validated_data['password'])
        admin.save()
        return admin

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.hash_passwrd(validated_data['password'])
            validated_data['password'] = instance.password
        return super().update(instance, validated_data)

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

class AdminLoginFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AdminUsers
        exclude = ("mail_id", "location_id", "name")
### for stackoverflow

## for celery
class PremiumUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumUsers
        fields = "__all__"

class PremiumSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumSubscription
        fields = "__all__"

    def create(self, validated_data):
        premium = PremiumSubscription(**validated_data)
        premium_user = PremiumUsers.objects.get(id=premium.user.id)
        premium_user.premium_status = True
        premium_user.save()
        premium.save()
        subscription_terminate_worker.delay(premium_user.id)
        return premium
