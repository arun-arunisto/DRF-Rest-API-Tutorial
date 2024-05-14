from django.contrib import admin
from .models import Author, Category, Book

# Register your models here.
class AuthorDashBoard(admin.ModelAdmin):
    list_display = ["id", "author_name"]

class CategoryDashBoard(admin.ModelAdmin):
    list_display = ["id", "category_name"]

class BookDashBoard(admin.ModelAdmin):
    list_display = ["id", "book_title", "author", "published_date"]

admin.site.register(Author, AuthorDashBoard)
admin.site.register(Category, CategoryDashBoard)
admin.site.register(Book, BookDashBoard)
