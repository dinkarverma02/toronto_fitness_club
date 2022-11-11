from django.contrib import admin

from studio.models import Image, Studio

class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image']


class StudioAdmin(admin.ModelAdmin):

    fields = ['name', 'address', 'latitude', 'longitude', 'postal_code',
              'phone_number']

    inlines = [ImageInline]


admin.site.register(Studio, StudioAdmin)
admin.site.register(Image)


