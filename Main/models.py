from django.db import models
from django.contrib.auth.models import User

Flight_Type = (
    ("Domestic","Domestic"),
    ("International","International")
)


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
        return self.ffrom +" to "+ str(self.fto) + " | " + str(self.date1)


class Book_flight(models.Model):
    sflight = models.CharField(max_length=122)
    passport_num= models.CharField(max_length=122)


    def __str__(self):
        return self.sflight



class Airlines(models.Model):
    name=models.CharField(max_length=122)
    image=models.ImageField(upload_to="airlines/")
    price = models.PositiveIntegerField()
    flight_type = models.CharField(max_length=255,choices=Flight_Type)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    description=models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "|" + str(self.flight_type)


class Flight_Book (models.Model):
    user = models .ForeignKey(User,on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    airlines =models.ForeignKey(Airlines,on_delete=models.CASCADE)
    created_at =models.DateField(auto_now_add=True)


    def __str__(self):
        return  self.user.username + " | " + str(self.flight.ffrom) + " to " + str(self.flight.fto) + " |  " + str(self.airlines)