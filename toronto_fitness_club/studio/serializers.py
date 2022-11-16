from rest_framework import serializers

from studio.models import Amenities, ClickStudio, Location, PostalCode, Studio, \
    StudioToDistance


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

class OgStudioSerializer(serializers.ModelSerializer):
    amenities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type'
    )

    class Meta:
        model = Studio
        fields = ['name', 'amenities', 'address']

class StudioSerializer(serializers.ModelSerializer):

    studio_amenities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type'
    )


    class Meta:

        model = StudioToDistance
        fields = ['studio_id', 'studio_name', 'distance_to_studio', 'studio_amenities']


class StudioClickOn(serializers.ModelSerializer):
    # in front end these will be separated
    class Meta:
        model = ClickStudio
        fields = ['studio_user_click_on']
