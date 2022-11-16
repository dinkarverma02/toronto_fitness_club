import requests

# Create your views here.

# use API for studio page
from django.http import HttpResponseRedirect
from geopy import distance #doesn't identify it when migrations made
from rest_framework.generics import CreateAPIView, ListAPIView, \
    ListCreateAPIView

from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# username: thaksha password: water
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters, response, status

from studio.models import Amenities, GeoProx, Image, Studio, StudioToDistance
from studio.serializers import GeoProxStudioByCurrentLocationSerializer, \
    GeoProxStudioByPinPointSerializer, \
    GeoProxStudioByPostalSerializer, StudioClickOn, \
    StudioSerializer



def calculate_proximity(lat, long):

    all_studios = []

    for studio in Studio.objects.all():
        studio_to_distance = [studio.id, distance.geodesic((lat, long), (
            studio.latitude, studio.longitude)).km, studio.name]
        all_studios.append(studio_to_distance)
    return all_studios


def user_to_studio_distance(user_id: str, lat: float, long: float):

    # [[studio_id, distance, name],...]
    studioID_distance_studio = calculate_proximity(lat, long)

    current_user = user_id

    # delete other call user made to get studio by specific location
    for instance in GeoProx.objects.all():
        if instance.user_id == current_user:
            instance.delete()

    # create a new geoprox object for user
    user_to_studio = GeoProx()
    user_to_studio.user_id = current_user
    user_to_studio.current_lat = lat
    user_to_studio.current_long = long
    user_to_studio.save()

    # add to user_id distance to each studio
    for studio in studioID_distance_studio:
        studio_obj = StudioToDistance()
        studio_obj.studio_id = studio[0]
        studio_obj.distance_to_studio = studio[1]
        studio_obj.studio_name = studio[2]
        studio_obj.save()
        for item in Amenities.objects.all():
            if item.studios.id == studio[0]:
                studio_obj.studio_amenities.add(item)

        user_to_studio.studio_to_distance.add(studio_obj)


class GeoProxStudioByCurrentLocation(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByCurrentLocationSerializer

    def get(self, request):
        response = Response()
        response.data = {}
        response.status_code = status.HTTP_200_OK
        return response

    def post(self, request, *args, **kwargs):
        lat = request.data['lat']
        long = request.data['long']

        user_to_studio_distance(str(request.user.id), lat, long)

        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/studio/search_studio/')
class GeoProxStudioByPinPoint(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPinPointSerializer

    def get(self, request):
        response = Response()
        response.data = {}
        response.status_code = status.HTTP_200_OK
        return response

    def post(self, request, *args, **kwargs):
        lat = request.data['lat']
        long = request.data['long']

        user_to_studio_distance(str(request.user.id), lat, long)

        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/studio/search_studio/')

class GeoProxStudioByPostal(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPostalSerializer

    def get(self, request):
        response = Response()
        response.data = {}
        response.status_code = status.HTTP_200_OK
        return response

    def post(self, request, *args, **kwargs):
        postal_code = request.data["postal_code"].replace(' ', '%')

        # when convert could lead to error if not a valid postal code,
        # validate postal code when user enter before its posted maybe
        # using regex
        # convert postal code to long lat and call calculate_proximity
        # need to validate postal code !!!!!
        geocode_data = requests.get(
            f'https://geocoder.ca/{postal_code}?json=1')
        geodata = geocode_data.json()

        lat = geodata["latt"]
        long = geodata["longt"]

        user_to_studio_distance(str(request.user.id), lat, long)

        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/studio/search_studio/')


class SearchStudio(ListCreateAPIView):

    serializer_class = StudioSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search also needs to include 'nitish' stuff
    search_fields = ['studio_name', 'studio_amenities__type']
    filterset_fields = ['studio_name', 'studio_amenities__type']

    def get_queryset(self):

        geoprox_of_user = GeoProx.objects.filter(
            user_id=str(self.request.user.id)).first()

        if geoprox_of_user:
            return geoprox_of_user.studio_to_distance.all().order_by(
                'distance_to_studio')
        else:
            return set()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return StudioClickOn
        return StudioSerializer

    def post(self, request, *args, **kwargs):

        studio_user_clicked_on = request.data['studio_user_click_on']
        geoprox_of_user = GeoProx.objects.filter(
            user_id=str(self.request.user.id)).first()
        responsee = Response()
        responsee.data = {}
        if geoprox_of_user:
            user_lat = geoprox_of_user.current_lat
            user_long = geoprox_of_user.current_long
            studio_info = {}
            studio = Studio.objects.all().filter(id=studio_user_clicked_on).first()

            studio_info['name'] = studio.name
            studio_info['address'] = studio.address
            studio_info['phone_number'] = studio.phone_number
            studio_info['location'] = f'{studio.latitude}, {studio.longitude}'

            amenities = []
            for amenity in Amenities.objects.all():

                if str(amenity.studios.id) == studio_user_clicked_on:
                    amenities.append(amenity.type)
            studio_info['amenities'] = f'{amenities}'
            link_to_directions = f'https://www.google.com/maps/dir/?api=1&origin={user_lat},{user_long}&' \
            f'destination={studio.latitude},{studio.longitude}&travelmode=driving'
            studio_info['link_to_directions'] = link_to_directions

            images = []
            for image in Image.objects.all():

                if str(image.studios.id) == studio_user_clicked_on:
                    images.append(image.image.name)
            studio_info['images'] = f'{images}'

            responsee.data = studio_info
            responsee.status_code = status.HTTP_200_OK
            return responsee

        return response.Response(
            {'message': "UNAUTHORIZED"},
            status=status.HTTP_401_UNAUTHORIZED)




