import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Doctor

try:
    # Trying exact match first, then fuzzy
    try:
        doctor = Doctor.objects.get(name__iexact="Bhavana")
    except Doctor.DoesNotExist:
        doctor = Doctor.objects.filter(name__icontains="Bhavana").first()

    if doctor:
        doctor.image = "doctors/bhavana_centered.png"
        doctor.save()
        print(f"[+] Successfully updated photo for {doctor.name}")
    else:
        print("[!] Doctor Bhavana not found.")

except Exception as e:
    print(f"Error: {e}")
