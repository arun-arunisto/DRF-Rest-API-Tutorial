from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField()
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recipe: {self.recipe_name}"

class Review(models.Model):
    rating = models.FloatField()
    comments = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

