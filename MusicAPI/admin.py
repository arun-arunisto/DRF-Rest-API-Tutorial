from django.contrib import admin
from .models import *

# Register your models here.
class ArtistDashboard(admin.ModelAdmin):
    list_display = ["id", "artist_name"]

class AlbumDashBoard(admin.ModelAdmin):
    list_display = ["id", "album_name"]

class TrackDashBoard(admin.ModelAdmin):
    list_display = ["id", "track_name"]

admin.site.register(Artist, ArtistDashboard)
admin.site.register(Album, AlbumDashBoard)
admin.site.register(Track, TrackDashBoard)
