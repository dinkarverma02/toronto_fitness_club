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

    image = models.FileField(upload_to='studio_images/', null=True, blank=True)
    studios = ForeignKey(to=Studio, related_name= 'images', on_delete=CASCADE)
    objects = models.Manager()




class Amenities(models.Model):
    type = models.CharField(max_length=200)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    studios = ForeignKey(to=Studio, related_name='amenities', on_delete=CASCADE)
    objects = models.Manager()


class PinPoint(models.Model):
    lat = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)], null=False, blank=False)
    long = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)], null=False, blank=False)

class CurrentLocation(models.Model):
    lat = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)], null=False, blank=False)
    long = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)], null=False, blank=False)

class PostalCode(models.Model):

    postal_code = models.CharField(max_length=200, null=False, blank=False)
# have to migrate models



