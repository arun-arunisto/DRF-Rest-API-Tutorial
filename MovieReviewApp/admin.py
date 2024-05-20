from django.contrib import admin
from .models import *

# Register your models here.
class MovieDashBoard(admin.ModelAdmin):
    list_display = ["id", "movie_title", "director"]

class ReviewDashBoard(admin.ModelAdmin):
    list_display = ["id", "rating", "movie"]

admin.site.register(Movie, MovieDashBoard)
admin.site.register(Review, ReviewDashBoard)