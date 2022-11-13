from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from toronto_fitness_club.classes.models import Classes
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from toronto_fitness_club.classes.serializers import CreateClassesSerializer


# Create your views here.

class EditClassesView(RetrieveAPIView, UpdateAPIView):
    serializer_class = CreateClassesSerializer

    def get_object(self):
        return get_object_or_404(Classes, id=self.kwargs['classes_id'])


class CreateClassesView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateClassesSerializer


