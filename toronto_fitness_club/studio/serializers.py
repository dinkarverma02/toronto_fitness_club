from rest_framework import serializers

from studio.models import Image, Studio

class CreateStudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio

        fields = ['name', 'address', 'latitude', 'longitude', 'postal_code',
                  'phone_number']
