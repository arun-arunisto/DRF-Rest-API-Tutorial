from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    duration = models.IntegerField()
    released_year = models.DateField()

    def __str__(self):
        return f"Movie: {self.movie_title}"

class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField(max_length=500)
    review_time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie")

    def __str__(self):
        return f"Movie: {self.movie}"
