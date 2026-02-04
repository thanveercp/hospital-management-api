from datetime import date
from rest_framework import serializers
from home.models import Doctor, Booking


class DoctorSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = Doctor
        fields = ["id", "name", "specialization", "image", "department", "department_name"]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "patient_name",
            "phone",
            "email",
            "department",
            "doctor",
            "date",
            "message",
            "created_at",
        ]

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Date cannot be in the past.")
        return value

    def validate(self, attrs):
        dept = attrs.get("department")
        doc = attrs.get("doctor")

        if dept and doc and doc.department_id != dept.id:
            raise serializers.ValidationError({
                "doctor": "Selected doctor does not belong to the selected department."
            })
        return attrs
