from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    num_of_pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title