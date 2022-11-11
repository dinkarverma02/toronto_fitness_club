from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from studio.models import Image, Studio


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['image']


class StudioSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Studio

        fields = ['name', 'address', 'latitude', 'longitude', 'postal_code',
                  'phone_number', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        studio = Studio.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(studios=studio, **image_data)
        return studio

    def update(self, instance, validated_data):
        print(validated_data)
        images_data = validated_data.pop('images')
        image = (instance.images).all()
        image = list(image)
        instance.name = validated_data.get('name',
                                                 instance.name)
        instance.address = validated_data.get('address',
                                           instance.address)
        instance.latitude = validated_data.get('latitude',
                                           instance.latitude)
        instance.longitude = validated_data.get('longitude',
                                           instance.longitude)
        instance.postal_code = validated_data.get('postal_code',
                                           instance.postal_code)
        instance.phone_number = validated_data.get('phone_number',
                                           instance.phone_number)

        instance.save()

        for image_data in images_data:
            image_ = image.pop(0)
            image_.image = image_data.get('image', image_.name)
            image_.save()
        return instance



