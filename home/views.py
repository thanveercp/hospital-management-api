from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Department, Doctor, Booking


def home_page(request):
    doctors = Doctor.objects.all().order_by("id")  # You might want to limit this, e.g., [:4]
    departments = Department.objects.all().order_by("name")
    return render(request, "index.html", {"doctors": doctors, "departments": departments})


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    return render(request, "contact.html")


def department_page(request):
    departments = Department.objects.all().order_by("name")
    return render(request, "department.html", {"departments": departments})


def doctors_page(request):
    # ✅ show all doctors (no slicing)
    doctors = Doctor.objects.select_related("department").all().order_by("id")
    return render(request, "doctors.html", {"doctors": doctors})


def booking_page(request):
    departments = Department.objects.all().order_by("name")

    if request.method == "POST":
        patient_name = request.POST.get("patient_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        date_value = request.POST.get("date", "").strip()
        message_text = request.POST.get("message", "").strip()

        department_id = request.POST.get("department") or ""
        doctor_id = request.POST.get("doctor") or ""

        department = Department.objects.filter(id=department_id).first() if department_id.isdigit() else None
        doctor = Doctor.objects.filter(id=doctor_id).first() if doctor_id.isdigit() else None

        if not patient_name or not phone or not date_value:
            messages.error(request, "Patient name, phone, date are required.")
            return redirect("booking")

        # ✅ safety
        if department and doctor and doctor.department_id != department.id:
            messages.error(request, "Selected doctor does not belong to selected department.")
            return redirect("booking")

        Booking.objects.create(
            patient_name=patient_name,
            phone=phone,
            email=email,
            date=date_value,
            department=department,
            doctor=doctor,
            message=message_text,
        )
        messages.success(request, "Booking submitted successfully!")
        return redirect("booking")

    return render(request, "booking.html", {"departments": departments})
