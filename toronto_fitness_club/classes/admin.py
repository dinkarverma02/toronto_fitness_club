from django.contrib import admin

from classes.models import Classes


# Register your models here.
class ClassesAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'coach', 'keywords', 'capacity',
              'time']


admin.site.register(Classes)
