import json
from datetime import timedelta, datetime

from django.http import HttpResponse, response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from classes.models import Keyword, Class
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from classes.serializers import CreateClassesSerializer


# Create your views here.
# class ClassesView()
# class CreateClassesView(RetrieveAPIView, UpdateAPIView):
#     serializer_class = CreateClassesSerializer
#
#     def get_object(self):
#         return get_object_or_404(Classes, id=self.kwargs['classes_id'])
#
# class CreateClassesView(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class =  CreateClassesSerializer
#
# class ClassesListCreateAPIView(ListCreateAPIView):
# @csrf_exempt
# def ClassesCreate(request):
#     if request.method == "POST":
#         class_info = json.load(request.body)
#         name = class_info.get('name')
#         description = class_info.get('description')
#         coach = class_info.get('coach')
#         capacity = int(class_info.get('capacity'))
#         keywords = class_info.get('keywords')
#         day = class_info.get('day')
#         start_time = class_info.get('start_time')
#         end_time = class_info.get('end_time')
#
#         new_classes = Classes(name=name, description=description, coach=coach, capacity=capacity, day=day)
#         new_classes.save()

# @api_view(['GET'])
# def ClassesList(request):
#     classes = Classes.objects.all()
#     serializer = CreateClassesSerializer(classes, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def ClassesCreate(request):
#     serializer = CreateClassesSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def ClassCreate(request, pk):
#     classes = Classes.objects.get(id=pk)
#     serializer = CreateClassSerializer(instance=classes, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)

class ClassesView(ListAPIView):
    queryset = Class.objects.all().order_by('start_time')
    serializer_class = CreateClassesSerializer
    permission_classes = [IsAuthenticated]







