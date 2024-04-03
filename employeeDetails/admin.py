from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_no", "designation", "joined_at", "is_active")
    search_fields = ("name",)
    list_per_page = 10
    list_editable = ("is_active",)


admin.site.register(Employee, EmployeeAdmin)