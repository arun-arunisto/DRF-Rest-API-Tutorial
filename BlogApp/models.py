import random
import string
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category: {self.category_name}"

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    post_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blog_title+" "+self.category.category_name)
            self.slug = base_slug+''.join(random.choice(string.ascii_letters+string.digits) for _ in range(5))
        return super().save(*args, **kwargs)
