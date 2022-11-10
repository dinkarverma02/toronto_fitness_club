# from django.contrib.gis.db.models import PointField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.db.models import DecimalField, ImageField


# have to migrate models
class Image(models.Model):
    image = models.ImageField(
        upload_to='studio_images/')  # stores it in a file called studio images?






class Studio(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # for geographical location we want to store longitude and latitude values
    #geographical_location = Location()
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators = [MinValueValidator(-180), MaxValueValidator(180)])
    postal_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    images = models.ImageField()
      # use add to add images, need to fix because doesn't allow to add file
    objects = models.Manager()
