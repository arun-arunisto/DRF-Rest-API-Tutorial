from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, null=False)
    specialization = models.CharField(max_length=50, null=False)
    joined_at = models.DateField(null=False)
    passed_out = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.name}"


