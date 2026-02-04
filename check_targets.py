import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Doctor

targets = ['Mohanlal', 'Mammooty', 'Nivin Pauly', 'Manju Warrier', 'Kunchacko Boban', 'Kalyani']
print("Checking images for targets:")
for name in targets:
    try:
        # Fuzzy match to handle "mamoty" -> "Mammooty", "nivin poly" -> "Nivin Pauly" etc.
        # But here I am using the *correct database names* I previously confirmed.
        d = Doctor.objects.filter(name__icontains=name.split()[0]).first() 
        if d:
            print(f"{d.name}|{d.image}")
        else:
            print(f"{name}|NOT FOUND")
    except Exception as e:
        print(f"{name}|ERROR: {e}")
