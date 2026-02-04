import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Doctor

# Mapping of Partial Name -> New File Name
# Note: Using partial match "Mohanlal" will match "Mohanlal"
updates = {
    "Mohanlal": "doctors/mohanlal_centered.png",
    "Mammooty": "doctors/mammooty_centered.png",
    "Nivin Pauly": "doctors/nivin_centered.png",
    "Manju Warrier": "doctors/manju_centered.png",
    "Kunchacko Boban": "doctors/kunchacko_centered.png"
}

print("Batch updating photos...")

for name_key, photo_path in updates.items():
    try:
        doctor = Doctor.objects.get(name__icontains=name_key)
        doctor.image = photo_path
        doctor.save()
        print(f"  [+] Updated {doctor.name} with {photo_path}")
    except Doctor.DoesNotExist:
        # Fallback for "Mammooty" if spelled differently in DB
        print(f"  [!] Doctor {name_key} not found via get().")
    except Doctor.MultipleObjectsReturned:
         print(f"  [!] Multiple matches for {name_key}.")

print("Batch update script finished.")
