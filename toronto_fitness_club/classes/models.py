from django.db import models

# Create your models here.


class Classes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    capacity = models.IntegerField()
    times = models.TimeField()


