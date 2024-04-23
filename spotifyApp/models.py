import datetime
from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    created_at = models.DateField(default=datetime.date.today())

    def __str__(self):
        return f"Album {self.album_name}"

class Tracks(models.Model):
    track_name = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Track {self.track_name}"
