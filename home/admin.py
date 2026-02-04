from django.contrib import admin
from .models import Department, Doctor, Booking


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "department", "specialization")
    list_filter = ("department",)
    search_fields = ("name", "specialization", "department__name")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "patient_name", "phone", "department", "doctor", "date", "status", "created_at")
    list_filter = ("status", "department", "doctor", "date")
    search_fields = ("patient_name", "phone", "email", "department__name", "doctor__name")
    list_editable = ("status",)
    ordering = ("-created_at",)
