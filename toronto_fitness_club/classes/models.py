from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Classes(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    coach = models.CharField(max_length=200)
    keywords = ArrayField(models.CharField())
    capacity = models.IntegerField()
    times = ArrayField(models.TimeField())


