import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Doctor

try:
    doctor = Doctor.objects.get(name__icontains="Fahadh Faasil")
    if doctor:
        doctor.image = "doctors/fahadh_centered.png"
        doctor.save()
        print(f"[+] Successfully updated photo for {doctor.name}")
    else:
        print("[!] Doctor Fahadh Faasil not found.")

except Exception as e:
    print(f"Error: {e}")
