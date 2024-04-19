from django.contrib import admin
from .models import Voters

# Register your models here.
class VoterDashboard(admin.ModelAdmin):
    list_display = ["name", "age", "voter_id_no"]
    list_filter = ["name", "age"]

admin.site.register(Voters, VoterDashboard)

