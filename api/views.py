from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from home.models import Doctor
from .serializers import DoctorSerializer, BookingCreateSerializer


class DoctorsListAPI(APIView):
    """
    GET /api/doctors/?department=3&search=abc
    """
    def get(self, request):
        qs = Doctor.objects.select_related("department").all().order_by("id")

        dept_id = request.query_params.get("department")
        if dept_id:
            if not str(dept_id).isdigit():
                return Response({"error": "department must be integer"}, status=status.HTTP_400_BAD_REQUEST)
            qs = qs.filter(department_id=int(dept_id))

        search = request.query_params.get("search", "").strip()
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(specialization__icontains=search) |
                Q(department__name__icontains=search)
            )

        data = DoctorSerializer(qs, many=True).data
        return Response({"count": len(data), "results": data}, status=status.HTTP_200_OK)


class BookingCreateAPI(APIView):
    """
    POST /api/bookings/
    """
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response(BookingCreateSerializer(booking).data, status=status.HTTP_201_CREATED)
