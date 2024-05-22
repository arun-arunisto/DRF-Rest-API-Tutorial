from django.db import models

# Create your models here.
class Chef(models.Model):
    chef_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Chef: {self.chef_name}"

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="chef")
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recipe: {self.recipe_name}"

class Review(models.Model):
    rating = models.FloatField()
    comments = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")

