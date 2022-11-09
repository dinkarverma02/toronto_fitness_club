from django.db import models

# Create your models here.
from django.db.models import ImageField

# have to migrate models
class Image(models.Model):
    image = models.ImageField(
        upload_to='studio_images')  # stores it in a file called studio images?


class Studio(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    geographical_location = models.CharField(max_length=200)  # could change
    # type so it's easier to calculate proximity of user to the studio
    postal_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    images = models.ManyToManyField(Image)  # use add to add images
