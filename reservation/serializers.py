from rest_framework import serializers
from reservation.models import Table, Reservation
from reservation.utils import send_reservation_email


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        exclude = ()


class ReservedTableSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='tables__id')

    class Meta:
        model = Reservation
        fields = ('id',)


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('email', 'name', 'date', 'tables')

    def create(self, validated_data):
        if Reservation.objects.filter(tables__in=validated_data.get('tables'), date=validated_data.get('date')):
            raise serializers.ValidationError('One of tables already reserved, please select another one')
        else:
            tables = validated_data.pop('tables')
            reservation = Reservation.objects.create(**validated_data)
            for table in tables:
                reservation.tables.add(table)
            send_reservation_email(reservation.id)
            return reservation
