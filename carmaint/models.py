from django.db import models

# Create your models here.

class Car(models.Model):
    year = models.CharField(default = '', max_length = 50)
    make = models.CharField(default = '', max_length = 50)
    model = models.CharField(default = '', max_length = 50)
    trim = models.CharField(default = '', max_length = 50)
    image_url = models.CharField(default = '', blank=True, max_length = 512)

    def __str__(self):
        return f"{self.year} - {self.make} - {self.model}"

class Maintenance(models.Model):
    desc = models.CharField(default = '', max_length = 500)
    total_cost = models.DecimalField(default='0.00', max_digits=8, decimal_places=2)
    mileage = models.PositiveIntegerField(default='0')
    notes = models.TextField(default="", blank=True)
    invoice_img = models.CharField(default = '', blank=True, max_length = 600)
    car = models.ForeignKey(Car, default = '', on_delete = 'CASCADE', related_name = 'maintenances')

    def __str__(self):
        return f"{self.desc} for {self.car.model}"