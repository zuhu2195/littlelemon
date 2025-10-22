from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=300)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
