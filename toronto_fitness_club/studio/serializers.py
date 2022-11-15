from rest_framework import serializers

from studio.models import Amenities, Location, PostalCode, Studio


class GeoProxStudioByPinPointSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    # pin point will be from map
    class Meta:
        model = Location
        fields = ['lat', 'long']


class GeoProxStudioByCurrentLocationSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    # current location may be by tracking
    class Meta:
        model = Location
        fields = ['lat', 'long']


class GeoProxStudioByPostalSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    class Meta:
        model = PostalCode
        fields = ['postal_code']


class StudioSerializer(serializers.ModelSerializer):
    amenities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type'
    )

    class Meta:

        model = Studio
        fields = ['name', 'amenities']

