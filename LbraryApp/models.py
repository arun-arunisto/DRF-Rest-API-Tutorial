from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Book: {self.book_name}"

class Reader(models.Model):
    reader_name = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    is_returned = models.BooleanField(default=False)
    taken_date = models.DateField()

    def __str__(self):
        return f"Reader: {self.reader_name}"


