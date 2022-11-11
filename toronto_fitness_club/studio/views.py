from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView
from django.shortcuts import get_object_or_404

# Create your views here.

# use API for studio page
from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from studio.models import Studio
from studio.serializers import CreateStudioSerializer


class CreateStudioView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateStudioSerializer


