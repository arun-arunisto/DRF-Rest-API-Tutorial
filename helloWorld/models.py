from django.db import models
from datetime import datetime

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    job = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"Sample Data: {self.name}"