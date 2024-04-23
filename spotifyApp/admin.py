from django.contrib import admin
from .models import Album, Tracks

# Register your models here.
class AlbumDash(admin.ModelAdmin):
    list_display = ["album_name", "created_at"]

class TrackDash(admin.ModelAdmin):
    list_display = ["track_name", "artist_name", "created_at"]

admin.site.register(Album, AlbumDash)
admin.site.register(Tracks, TrackDash)
