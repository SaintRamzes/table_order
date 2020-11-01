from django.conf import settings
from django.core.mail import send_mail

from reservation.models import Reservation


def send_reservation_email(reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    tables = reservation.tables.values_list('number', flat=True)
    send_mail(
        subject=f"Your reservation on {reservation.date.strftime('%Y-%m-%d')}",
        message=f'Congratulation, you are reserved tables: {list(tables)}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[reservation.email]
    )
