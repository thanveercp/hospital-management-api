from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("doctors/", views.doctors_page, name="doctors"),
    path("department/", views.department_page, name="department"),
    path("contact/", views.contact_page, name="contact"),
    path("booking/", views.booking_page, name="booking"),
]
