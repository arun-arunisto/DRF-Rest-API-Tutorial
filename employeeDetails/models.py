from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    phone_no = models.IntegerField(null=False)
    address = models.TextField(max_length=500, null=True)
    designation = models.CharField(max_length=100, null=True)
    joined_at = models.DateField(null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Employee Name: {self.name}"
