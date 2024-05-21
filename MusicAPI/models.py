from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Artist: {self.artist_name}"

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    released_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist")

    def __str__(self):
        return f"Album: {self.album_name}"

class Track(models.Model):
    track_name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Track: {self.track_name}"


