from django.urls import path
from .views import DoctorsListAPI, BookingCreateAPI

urlpatterns = [
    path("doctors/", DoctorsListAPI.as_view(), name="api-doctors"),
    path("bookings/", BookingCreateAPI.as_view(), name="api-bookings"),
]
