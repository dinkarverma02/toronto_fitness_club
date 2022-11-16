from django.db import models


# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=200, null=False)


class Class(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Keyword)
    capacity = models.IntegerField(null=False)
    space = models.IntegerField(null=False)
    day = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    studio = models.CharField(max_length=150,null=False, blank=False)

    def __str__(self):
        return f'{self.name} starting at {self.start_time} and ending at {self.end_time}'

    def get_class_info(self):
        return {"id": self.id, "name": self.name, "description": self.description,
                "coach": self.coach, "space": self.space, "day": self.day, "start_time": self.start_time,
                "end_time": self.end_time}


class Classes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Keyword)
    capacity = models.IntegerField()
    # day = models.CharField(max_length=100)
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    class_instances = models.ManyToManyField(Class, default=None)
    # need to integrate with studio

    def __str__(self):
        return f'{self.name} '
