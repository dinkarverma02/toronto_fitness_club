from rest_framework import serializers

from studio.models import Studio

class CreateStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['name', 'address', 'geographical_location', 'postal_code',
                  'phone_number', 'images']
