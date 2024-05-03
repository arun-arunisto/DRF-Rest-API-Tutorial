from django.contrib import admin
from .models import Blog, Category

# Register your models here.
class BlogDashBoard(admin.ModelAdmin):
    list_display = ["id", "blog_title", "blog_description", "category", "is_public"]
    list_editable = ["is_public"]

class CategoryDashBoard(admin.ModelAdmin):
    list_display = ["id", "category_name"]

admin.site.register(Blog, BlogDashBoard)
admin.site.register(Category, CategoryDashBoard)

