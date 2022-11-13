
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView
from django.shortcuts import get_object_or_404

# Create your views here.

# use API for studio page
from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from studio.models import Studio



