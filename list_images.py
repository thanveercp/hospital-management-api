import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Doctor

names = ['Nivin Pauly', 'Kunchacko Boban', 'Jayasurya', 'Dulquer Salmaan', 'Manju Warrier']
with open('doctor_images_list.txt', 'w') as f:
    for d in Doctor.objects.filter(name__in=names):
        f.write(f"{d.name}: {d.image}\n")

print("List written to doctor_images_list.txt")
