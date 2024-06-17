from django.contrib import admin
from .models import LoginCredUsers

# Register your models here.
class LoginCredDashboard(admin.ModelAdmin):
    list_display = ("id", "username","mail_id")

admin.site.register(LoginCredUsers, LoginCredDashboard)
