from rest_framework import serializers

from classes.models import Classes, Class


class CreateClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
