# from django.contrib.gis.db.models import PointField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib import admin

# Create your models here.
from django.db.models import CASCADE, DecimalField, ForeignKey, ImageField, \
    OneToOneField, \
    SET_NULL

class Studio(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # for geographical location we want to store longitude and latitude values
    # geographical_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)])
    postal_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    # use add to add images, need to fix because doesn't allow to add
    # multiple files
    #images = models.ForeignKey(Image, )

    objects = models.Manager()

class Image(models.Model):
    #studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='studio_images/')
    studios = ForeignKey(to=Studio, on_delete=CASCADE)
    # stores it in a file called studio images?





# have to migrate models


class Location(models.Model):
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)])
