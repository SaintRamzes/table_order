import datetime

from rest_framework.generics import ListAPIView, CreateAPIView

from reservation.models import Reservation
from reservation.serializers import TableSerializer, ReservedTableSerializer, ReservationSerializer


class TableListView(ListAPIView):
    serializer_class = TableSerializer


class ReservedTableListView(ListAPIView):
    serializer_class = ReservedTableSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', '')
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return []
        return Reservation.objects.filter(date=date).select_related('tables').values('tables__id')


class ReservationCreateView(CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
