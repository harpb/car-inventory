from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 255)

class Brand(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length = 255)

class CarModelOption(models.Model):
    name = models.CharField(max_length = 255)

class CarModel(models.Model):
    brand = models.ForeignKey(Brand)
    color = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    options = models.ManyToManyField(CarModelOption)
    price = models.FloatField()
    year = models.PositiveIntegerField()

