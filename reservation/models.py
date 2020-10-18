from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

        
