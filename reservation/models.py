from django.db import models


class Table(models.Model):

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ['number']

    SHAPE_CHOICES = (
        (1, 'Rectangle'),
        (2, 'Oval')
    )

    number = models.IntegerField(verbose_name='Table number')
    seats = models.IntegerField(verbose_name='Seats')
    shape = models.IntegerField(verbose_name='Shape', choices=SHAPE_CHOICES, default=1)
    coordinateX = models.IntegerField(verbose_name='Table coordinate X')
    coordinateY = models.IntegerField(verbose_name='Table coordinate Y')
    length = models.IntegerField(verbose_name='Table length')
    width = models.IntegerField(verbose_name='Table width')

    def __str__(self):
        return f"{self.id}"


class Reservation(models.Model):

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ['-date']

    email = models.EmailField(verbose_name='User email')
    name = models.CharField(verbose_name='User name', max_length=50)
    date = models.DateField(verbose_name='Reservation date')
    tables = models.ManyToManyField(to=Table, verbose_name='Reserved tables')

    def __str__(self):
        return f"{self.name} - {self.email} - {self.date}"
