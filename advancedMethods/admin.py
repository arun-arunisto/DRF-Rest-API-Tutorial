from django.contrib import admin
from .models import *

# Register your models here.
class LoginCredDashboard(admin.ModelAdmin):
    list_display = ("id", "username","mail_id")

class LocationDashboard(admin.ModelAdmin):
    list_display = ("id", "name")

class ProductsDashboard(admin.ModelAdmin):
    list_display = ("id", "name", "location_id", "price")

class AdminUsersDashboard(admin.ModelAdmin):
    list_display = ("id", "name", "location_id", "mail_id")

class OrdersDashboard(admin.ModelAdmin):
    list_display = ("id", "product_id", "admin_id", "location_id", "user_id", "status")


admin.site.register(LoginCredUsers, LoginCredDashboard)
admin.site.register(Location, LocationDashboard)
admin.site.register(Products, ProductsDashboard)
admin.site.register(AdminUsers, AdminUsersDashboard)
admin.site.register(Orders, OrdersDashboard)
