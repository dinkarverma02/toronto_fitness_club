import requests
import geopy.distance
from django.db.migrations import serializer
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
from rest_framework import response, status

from studio.models import Studio

# return list with studio id ordered from closest to furthest user can go to
# -> need to store direction to use for link to get direction -> need to
# store as will apply filters on this user get a page where they do filter of
# studios
# enter the studio page they want to go to, then a respose
# is return with the studio id, link to direction, ..
from studio.serializers import GeoProxStudioByCurrentLocationSerializer, \
    GeoProxStudioByPinPointSerializer, \
    GeoProxStudioByPostalSerializer


# class StoreView(APIView):
#     def get(self, request, *args, **kwargs):
#         store = get_object_or_404(Store, id=kwargs['store_id'])
#         return Response({
#             'id': store.id,
#             'name': store.name,
#             'description': store.description,
#             'url': store.url,
#             'email': store.email
#         })

# check if dict empty as then they are no studio for user to go to
def calculate_proximity(lat, long):
    # {studio_id: distance to the studio}
    studio_to_distance = {}
    for studio in Studio.objects.all():
        studio_to_distance[studio.id] = geopy.distance.geodesic((lat, long), (studio.latitude, studio.longitude)).km
        # source for sorting dictionary code "{k: v for k, v in sorted(
        # studio_to_distance.items(), key=lambda item: item[1])}" from
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a
        # -dictionary-by-value
    return {k: v for k, v in sorted(studio_to_distance.items(), key=lambda item: item[1])}


class GeoProxStudioByCurrentLocation(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByCurrentLocationSerializer

    def post(self, request, format=None):
        #  use this in get and let user pick a studio id they want to see the page of

        lat = request.data['current_location_lat']
        long = request.data['current_location_long']
        calculate_proximity(lat, long)

        response = Response()
        response.data = calculate_proximity(lat, long)
        response.status_code = status.HTTP_200_OK

        return response


class GeoProxStudioByPostal(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPostalSerializer

    def post(self, request, format=None):

        postal_code = request.data["postal_code"].replace(' ', '%')

        if postal_code:
            # when convert could lead to error if not a valid postal code,
            # validate postal code when user enter before its posted maybe
            # using regex
            # convert postal code to long lat and call calculate_proximity
            #need to validate postal code !!!!!
            geocode_data = requests.get(f'https://geocoder.ca/{postal_code}?json=1')
            geodata = geocode_data.json()

            lat = geodata["latt"]
            long = geodata["longt"]
            calculate_proximity(lat, long)
        response = Response()
        response.data = calculate_proximity(lat, long)
        response.status_code = status.HTTP_200_OK

        return response


class GeoProxStudioByPinPoint(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPinPointSerializer

    def post(self, request, format=None):
        lat = request.data["pinpoint_lat"]
        long = request.data["pinpoint_long"]
        calculate_proximity(lat, long)

        response = Response()
        response.data = calculate_proximity(lat, long)
        response.status_code = status.HTTP_200_OK

        return response




