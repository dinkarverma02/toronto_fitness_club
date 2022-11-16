from django.contrib import admin

from classes.models import Class

from classes.models import Keyword


# Register your models here.
class ClassesAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'coach', 'keywords', 'capacity',
              'day', 'start_time', 'end_time']


admin.site.register(Class)
admin.site.register(Keyword)
