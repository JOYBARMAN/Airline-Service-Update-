from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    fflight = models.CharField(max_length=122)
    ffrom = models.CharField(max_length=122)
    fto = models.CharField(max_length=122)
    date1 = models.DateField()
    date2 = models.DateField()
    adult = models.CharField(max_length=122)
    child = models.CharField(max_length=122)
    fclass = models.CharField(max_length=122)

    def __str__(self):
        return self.fflight


class Book_flight(models.Model):
    sflight = models.CharField(max_length=122)
    passport_num= models.CharField(max_length=122)


    def __str__(self):
        return self.sflight