from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView
from django.shortcuts import get_object_or_404

# Create your views here.

# use API for studio page
from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from rest_framework.views import APIView

from studio.models import Studio
from studio.serializers import ImageSerializer, StudioSerializer


class CreateStudioView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudioSerializer


class EditStudioView(RetrieveAPIView, UpdateAPIView):
    serializer_class = StudioSerializer

    def get_object(self):
        return get_object_or_404(Studio, id=self.kwargs['studio_id'])


class DeleteStudio(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudioSerializer

    def get_object(self):
        return get_object_or_404(Studio, id=self.kwargs['studio_id'])

    def delete(self, request, *args, **kwargs):
        studio = Studio.objects.get(id=self.kwargs['studio_id'])
        studio.delete()
        # should do something else instead of returning a http response
        # front end user will have a list of their studios
        return HttpResponse('studio deleted', status=200)
