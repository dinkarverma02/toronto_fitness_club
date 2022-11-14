from rest_framework import serializers

from studio.models import CurrentLocation, PinPoint, PostalCode


class GeoProxStudioByPinPointSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    class Meta:
        model = PinPoint
        fields = ['lat', 'long']

class GeoProxStudioByCurrentLocationSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    class Meta:
        model = CurrentLocation
        fields = ['lat', 'long']

class GeoProxStudioByPostalSerializer(serializers.ModelSerializer):
    # in front end these will be separated
    class Meta:
        model = PostalCode
        fields = ['lat', 'long']



