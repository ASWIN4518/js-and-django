from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    # list_display = (
    #     "name",
    #     "email",
    #     "department",
    #     "role",
    #     "phone",
    #     "created_at",
    # )

    search_fields = (
        "name",
        "email",
        "department",
        "role",
    )