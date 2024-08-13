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
    title = models.CharField(max_length=255)
    date_up = models.DateTimeField(auto_now_add=True)
    days_activation = models.PositiveSmallIntegerField(default=0)

#creating admin and location for the fetching data from the database using authentication permissions
class Location(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location: {self.name}"

class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.name}"

class AdminUsers(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    mail_id = models.EmailField(unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def hash_passwrd(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()
        return self.password

    def __str__(self):
        return f"Admin user: {self.name}"

class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    admin_id = models.ForeignKey(AdminUsers, on_delete=models.SET_NULL, null=True)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(LoginCredUsers, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=((0, "Pending"),
                                          (1, "Delivered"),
                                          (2, "Cancelled"),
                                          (3, "Accepted")), null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.id}"

#for celery and redis
class PremiumUsers(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    mail_id = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    premium_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Premium user: {self.name}"

class PremiumSubscription(models.Model):
    user = models.ForeignKey(PremiumUsers, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Premium subscription: {self.user.name}"
    

class BikeModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    company = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.name}"

class Bike(models.Model):
    register_no = models.CharField(max_length=100, blank=False, null=False, unique=True)
    model = models.ForeignKey(BikeModel, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Register No: {self.register_no}"

class Booking(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking: {self.bike.register_no}"

class BlockReview(models.Model):
    block_reason = models.IntegerField(choices=((1, "Service"), (2, "brake down"), (3, "puncture")), null=False, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, blank=False)
    block_status = models.IntegerField(choices=((0, "Pending"), (1, "rejected"), (2, "accepted")), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Block review: {self.block_reason}"

class Rides(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride: {self.bike.register_no}"

#for bulk image upload
class Images(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to="uploads/")

class Trip(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip: {self.id}"
    
class TripImages(models.Model):
    path = models.CharField(max_length=500, blank=True, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=False, blank=False)
    image_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip image: {self.id}"