from django.contrib import admin
from .models import StudentData

# Register your models here.
class StudentDash(admin.ModelAdmin):
    list_display = ["id", "name", "degree", "specialization", "passed_out"]
    list_editable = ["passed_out"]
    list_filter = ["name", "degree"]
    list_display_links = ["name"]

admin.site.register(StudentData, StudentDash)