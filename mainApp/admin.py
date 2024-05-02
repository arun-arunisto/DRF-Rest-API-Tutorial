from django.contrib import admin
from .models import AppDetails

# Register your models here.
class MainDashBoard(admin.ModelAdmin):
    list_display = ("name", "info", "endpoints", "connection")
    list_display_links = ("name",)

admin.site.register(AppDetails, MainDashBoard)
