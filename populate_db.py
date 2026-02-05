import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Management.settings')
django.setup()

from home.models import Department, Doctor

def populate():
    print("Populating database...")

    # 1. Create Departments
    departments_data = [
        {"name": "Cardiology", "desc": "Heart health"},
        {"name": "Neurology", "desc": "Brian and nerves"},
        {"name": "Pediatrics", "desc": "Child care"},
        {"name": "Orthopedics", "desc": "Bones and muscles"},
        {"name": "Gynecology", "desc": "Women's health"},
        {"name": "Oncology", "desc": "Cancer treatment"},
        {"name": "ENT", "desc": "Ear, Nose, Throat"},
        {"name": "Psychiatry", "desc": "Mental health"},
        {"name": "General Surgery", "desc": "Surgical procedures"},
        {"name": "Dermatology", "desc": "Skin care"},
        {"name": "General Medicine", "desc": "Primary care"},
    ]

    dept_objs = {}
    for d in departments_data:
        obj, created = Department.objects.get_or_create(
            name=d["name"],
            defaults={"description": d["desc"]}
        )
        dept_objs[d["name"]] = obj
        if created:
            print(f"Created Department: {d['name']}")
        else:
            print(f"Department already exists: {d['name']}")

    # 2. Create Doctors
    doctors_data = [
        {
            "name": "Dr. Mohanlal",
            "spec": "Senior Cardiologist",
            "dept": "Cardiology",
            "img": "doctors/mohanlal_centered.png"
        },
        {
            "name": "Dr. Mammooty",
            "spec": "Senior Neurologist",
            "dept": "Neurology",
            "img": "doctors/mammooty_centered.png"
        },
        {
            "name": "Dr. Manju Warrier",
            "spec": "Gynecologist",
            "dept": "Gynecology",
            "img": "doctors/manju_centered.png"
        },
        {
            "name": "Dr. Nivin Pauly",
            "spec": "Pediatrician",
            "dept": "Pediatrics",
            "img": "doctors/nivin_centered.png"
        },
        {
            "name": "Dr. Kunchacko Boban",
            "spec": "Orthopedic Surgeon",
            "dept": "Orthopedics",
            "img": "doctors/kunchacko_centered.png"
        },
         {
            "name": "Dr. Dulquer Salmaan",
            "spec": "Oncologist",
            "dept": "Oncology",
            "img": "doctors/dulquer_centered.png"
        },
        {
            "name": "Dr. Jayasurya",
            "spec": "ENT Specialist",
            "dept": "ENT",
            "img": "doctors/jayasurya_centered.png"
        },
        # NEW DOCTORS
        {
            "name": "Dr. Fahadh Faasil",
            "spec": "Psychiatrist",
            "dept": "Psychiatry",  # New Dept
            "img": "doctors/fahadh_centered.png"
        },
        {
            "name": "Dr. Prithviraj Sukumaran",
            "spec": "General Surgeon",
            "dept": "General Surgery", # New Dept
            "img": "doctors/prithviraj_centered.png"
        },
        {
            "name": "Dr. Tovino Thomas",
            "spec": "Sports Medicine Specialist",
            "dept": "Orthopedics",
            "img": "doctors/tovino_centered.png"
        },
        {
            "name": "Dr. Parvathy Thiruvothu",
            "spec": "Dermatologist",
            "dept": "Dermatology", # New Dept
            "img": "doctors/parvathy_centered.png"
        },
        {
            "name": "Dr. Bhavana",
            "spec": "Cosmetologist",
            "dept": "Dermatology",
            "img": "doctors/bhavana_centered.png"
        },
        {
            "name": "Dr. Kalyani Priyadarshan",
            "spec": "Child Psychologist",
            "dept": "Pediatrics",
            "img": "doctors/kalyani_centered.png"
        }
    ]

    for doc in doctors_data:
        dept = dept_objs.get(doc["dept"])
        if dept:
            obj, created = Doctor.objects.get_or_create(
                name=doc["name"],
                defaults={
                    "specialization": doc["spec"],
                    "department": dept,
                    "image": doc["img"]
                }
            )
            if created:
                 print(f"Created Doctor: {doc['name']}")
            else:
                 print(f"Doctor already exists: {doc['name']}")
        else:
            print(f"Skipping {doc['name']} - Department {doc['dept']} not found (unexpected).")

    print("Population complete.")

if __name__ == '__main__':
    populate()
