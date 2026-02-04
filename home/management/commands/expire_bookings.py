from django.core.management.base import BaseCommand
from datetime import date
from home.models import Booking

class Command(BaseCommand):
    help = "Mark past scheduled bookings as expired"

    def handle(self, *args, **options):
        count = Booking.objects.filter(
            date__lt=date.today(),
            status="scheduled"
        ).update(status="expired")

        self.stdout.write(self.style.SUCCESS(f"Expired {count} bookings"))
