from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView

# Create your views here.

# use API for studio page
from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from studio.serializers import CreateStudioSerializer


class CreateStudioView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateStudioSerializer

