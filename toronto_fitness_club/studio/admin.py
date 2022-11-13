from django.contrib import admin

from studio.models import Amenities, Image, Studio


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image']


class AmenitiesInline(admin.TabularInline):
    model = Amenities
    fields = ['type', 'quantity']


class StudioAdmin(admin.ModelAdmin):

    fields = ['name', 'address', 'latitude', 'longitude', 'postal_code',
              'phone_number']

    inlines = [ImageInline, AmenitiesInline]


admin.site.register(Studio, StudioAdmin)
admin.site.register(Image)
admin.site.register(Amenities)
