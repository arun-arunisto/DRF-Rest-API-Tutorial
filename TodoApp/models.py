from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    created_at = models.DateField(default=datetime.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Todo - {self.title}"
