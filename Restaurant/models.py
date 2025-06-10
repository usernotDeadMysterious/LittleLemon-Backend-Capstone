from django.db import models

# Create your models here.
# class Menu (models.Model):
#     id = models.IntegerField()
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     inventory = models.IntegerField()

class Menu(models.Model):
    # id = models.IntegerField()
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"