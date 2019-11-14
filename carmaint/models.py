from django.db import models

# Create your models here.

class Car(models.Model):
    year = models.CharField(default = '', max_length = 50)
    make = models.CharField(default = '', max_length = 50)
    model = models.CharField(default = '', max_length = 50)
    vin = models.CharField(default = '', blank=True, max_length = 17)

    def __str__(self):
        return f"{self.year} - {self.make} - {self.model}"

class Maintenance(models.Model):
    desc = models.CharField(default = '', max_length = 200)
    due_mileage = models.PositiveIntegerField(default='0')
    is_oem = models.BooleanField
    is_cycle = models.BooleanField
    cycle_mileage = models.PositiveIntegerField(default='0')

    car = models.ForeignKey(Car, default = '', on_delete = 'CASCADE', related_name = 'maintenances')

    def __str__(self):
        return f"{self.desc} for {self.car.model}"
