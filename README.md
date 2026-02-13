# Hospital Management System (Django)

A Hospital Management Web Application built using Django and Django REST Framework.

## Features

- Doctor Management
- Department Management
- Appointment Booking
- Contact Form
- Authentication (Login Required for Admin)
- CRUD Operations
- Media & Image Upload
- Pagination (API)
- Admin Panel Support

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML, CSS, Bootstrap

## Project Setup

1. Clone the repository

git clone https://github.com/thanveercp/hospital-management-api.git

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

Windows:
venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Run migrations

python manage.py migrate

6. Run server

python manage.py runserver

## API Endpoints (Sample)

GET /api/doctors/
POST /api/doctors/
GET /api/doctors/<id>/
PUT /api/doctors/<id>/
DELETE /api/doctors/<id>/

## Author

Thanveer C.P  
GitHub: https://github.com/thanveercp
