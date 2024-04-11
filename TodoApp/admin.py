from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoDash(admin.ModelAdmin):
    list_display = ["id", "title", "description", "is_active", "created_at"]
    list_filter = ["title", "is_active", "created_at"]
    list_editable = ["is_active"]
    list_display_links = ["title"]

admin.site.register(Todo, TodoDash)