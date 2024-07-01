from django.db import models
import hashlib


# Create your models here.
#login Credential for custom authendicated login  
class LoginCredUsers(models.Model):
    username = models.CharField(max_length=50, unique=True)
    pass_wd = models.CharField(max_length=100)
    mail_id = models.EmailField()

    def hash_passwrd(self, password):
        self.pass_wd = hashlib.sha256(password.encode()).hexdigest()
        return self.pass_wd

    def __str__(self):
        return f"User : {self.username}"

#for file upload
class FileUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


#for the stack overflow
class Process(models.Model):
    title = models.Charfield(max_length=255)
    date_up = models.DateTimeField(auto_now_add=True)
    days_activation = models.PositiveSmallIntegerField(default=0)

#creating admin and location for the fetching data from the database using authentication permissions
class Location(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location: {self.name}"

class Products(models.Model):
    name = models.CharField(unique=True, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.name}"

class AdminUsers(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL)
    mail_id = models.EmailField(unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def hash_passwrd(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()
        return self.password

    def __str__(self):
        return f"Admin user: {self.name}"

class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL)
    admin_id = models.ForeignKey(AdminUsers, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(LoginCredUsers, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=((0, "Pending"),
                                          (1, "Delivered"),
                                          (2, "Cancelled"),
                                          (3, "Accepted")), null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.id}"
    