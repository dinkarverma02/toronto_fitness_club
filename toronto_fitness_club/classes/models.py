from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=200, null=False)


class Class(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    coach = models.CharField(max_length=200, null=False)
    keywords = models.ManyToManyField(Keyword)
    capacity = models.IntegerField(null=False)
    day = models.CharField(max_length=100, default="Monday")
    start_time = models.TimeField()
    end_time = models.TimeField()
    studio = models.ForeignKey(to=Studio, related_name="classes", on_delete=CASCADE)

    # day = models.CharField(max_length=100)
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # need to integrate with studio
    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return f'{self.name} '

    def get_class_info(self):
        return {"name": self.name, "description": self.description,
                "coach": self.coach, "day": self.day, "start_time": self.start_time,
                "end": self.end_time}
