from rest_framework import serializers

from classes.models import Classes


class CreateClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['name', 'description', 'coach', 'keywords',
                  'capacity', 'times']
