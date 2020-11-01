from django.db import models


class Table(models.Model):

    SHAPE_CHOICES = (
        (1, 'Rectangle'),
        (2, 'Oval')
    )

    number = models.IntegerField()
    seats = models.IntegerField()
    shape = models.IntegerField(choices=SHAPE_CHOICES, default=1)
    coordinateX = models.IntegerField()
    coordinateY = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return f"{self.id}"


class Reservation(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    date = models.DateField()
    tables = models.ManyToManyField(to=Table)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.date}"
